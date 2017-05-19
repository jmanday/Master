package com.jesusgarciamanday.playquestion;

import android.annotation.TargetApi;
import android.content.DialogInterface;
import android.database.Cursor;
import android.media.AudioAttributes;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.media.SoundPool;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class GameActivity extends AppCompatActivity {

    private static final String RES_PREFIX = "android.resource://com.jesusgarciamanday.practica5/";
    private static final int NUM_BUTTONS = 4;
    private static final int NUM_GAMES = 7;
    private static final int LONG_DELAY = 3500; // 3.5 seconds
    private static final int SHORT_DELAY = 2500; // 2.5 seconds

    private ArrayList<Button> listButtons;
    private ArrayList<Integer> listNumbers;
    private TextView textViewQuestion;
    private ImageView imageViewQuestion;
    private PresenterDataSource pDataBase;
    private ArrayList<Question> listQuestions;
    private MediaPlayer mediaPlayer;
    private int responseCorrect;
    private SoundPool soundPool;
    private int idAcierto, idFallo, numAciertos, numFallos, numQuestion;
    private boolean loaded = true, acierto = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_games);

        listButtons = new ArrayList<>();
        listButtons.add((Button) findViewById(R.id.response1));
        listButtons.add((Button) findViewById(R.id.response2));
        listButtons.add((Button) findViewById(R.id.response3));
        listButtons.add((Button) findViewById(R.id.response4));
        textViewQuestion = (TextView) findViewById(R.id.question);
        imageViewQuestion = (ImageView) findViewById(R.id.image_question);

        listNumbers = new ArrayList<>();

        // defino el reproductor de sonido en función de la API
        createSoundPool();

        // obtengo la instancia de la base de datos
        this.pDataBase = ImplPresentDataSource.getInstance(this);

        setQuestions();
    }

    private void createSoundPool(){
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            createNewSoundPool();
        } else {
            createOldSoundPool();
        }
    }

    @TargetApi(Build.VERSION_CODES.LOLLIPOP)
    private void createNewSoundPool(){
        AudioAttributes attributes = new AudioAttributes.Builder()
                .setUsage(AudioAttributes.USAGE_GAME)
                .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
                .build();

        soundPool = new SoundPool.Builder()
                .setAudioAttributes(attributes)
                .build();

        soundPool.autoResume();

        idAcierto = soundPool.load(getApplicationContext(), R.raw.correct, 0);
        idFallo = soundPool.load(getApplicationContext(), R.raw.error_beep, 0);

        soundPool.setOnLoadCompleteListener(new SoundPool.OnLoadCompleteListener() {
            public void onLoadComplete(SoundPool soundPool, int sampleId, int status) {
                loaded = true;
            }
        });
    }

    @SuppressWarnings("deprecation")
    private void createOldSoundPool(){
        soundPool = new SoundPool(5, AudioManager.STREAM_MUSIC,0);
        idAcierto = soundPool.load(getApplicationContext(), R.raw.correct, 0);
        idFallo = soundPool.load(getApplicationContext(), R.raw.error, 0);
    }

    /*
     * Método para reproducir el sonido de error o acierto
     */
    public void playSound(int idSound){

        lockButtons();
        if (loaded) {
            soundPool.play(idSound,  0.25f, 0.25f, 1, 0, 1f);
            if(idSound == idAcierto){
                numAciertos++;
                Toast.makeText(getApplicationContext(), "¡¡¡ENHORABUENA!!! Ha contestado correctamente la pregunta.", Toast.LENGTH_SHORT).show();
                reloadQuestions(SHORT_DELAY);
            }
            else{
                numFallos++;
                showOptions();
            }

            if((numAciertos + numFallos) == NUM_GAMES)
                finishGame();
        }
    }


    @Override
    protected void onDestroy() {
        super.onDestroy();
        pDataBase.insertResult(new Score(numAciertos, numFallos));
    }

    /*
         * Método para bloquear los botones de la interfaz una vez que ha seleccionado una respuesta
         */
    private void lockButtons() {
        for(int i = 0; i < NUM_BUTTONS; i++)
            listButtons.get(i).setClickable(false);
    }

    /*
     * Método para desbloquear los botones de la interfaz una vez que se ha cargado otra pantalla de juegos
     */
    private void unlockButtons() {
        for(int i = 0; i < NUM_BUTTONS; i++)
            listButtons.get(i).setClickable(true);
    }

    /*
     * Método para establecer las respuestas y la pregunta en los elementos de la interfaz
     */
    private void setQuestions() {

        Cursor cuestiones = this.pDataBase.getQuestions();

        listQuestions = Question.converToQuestions(cuestiones);

        // Selecciono una pregunta aleatoria del conjunto de preguntas
        if(listNumbers.size() > 0){
            do{
                numQuestion = (int) (Math.random() * (cuestiones.getCount()-1) + 0);

            }while(listNumbers.contains(numQuestion) == true);

        }
        else
            numQuestion = (int) (Math.random() * (cuestiones.getCount()-1) + 0);

        listNumbers.add(numQuestion);

        Question p = listQuestions.get(numQuestion);

        // Establezco la pregunta a realizar
        textViewQuestion.setText(p.getPregunta());

        // Establezco la imagen relacionada a la pregunta
        int resId = getResources().getIdentifier(p.getPath_image(), "drawable", this.getPackageName());
        imageViewQuestion.setImageDrawable(getResources().getDrawable(resId));

        // Establezco todas las posibles respuestas
        responseCorrect = (int) (Math.random() * (NUM_BUTTONS-1 + 0));
        String[] responsesIncorrec = p.getRespuestasErroneas();
        for(int i = 0, j = 0; i < NUM_BUTTONS; i++){
            if(i == responseCorrect)
                listButtons.get(i).setText(p.getRespuesta());
            else{
                listButtons.get(i).setText(responsesIncorrec[j]);
                j++;
            }
        }


        listButtons.get(0).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                playSound((responseCorrect == 0)? idAcierto: idFallo);
            }
        });

        listButtons.get(1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                playSound((responseCorrect == 1)? idAcierto: idFallo);
            }
        });

        listButtons.get(2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                playSound((responseCorrect == 2)? idAcierto: idFallo);
            }
        });

        listButtons.get(3).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                playSound((responseCorrect == 3)? idAcierto: idFallo);
            }
        });

        if(!p.getPath_sound().toString().equals("null")){
            lockButtons();
            playSoundQuestion(p.getPath_sound());
        }
    }

    /*
     * Método lanzado cuando el usuario se equivoca
     */
    public void showOptions(){
        AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(GameActivity.this);

        // set title
        alertDialogBuilder.setTitle("¡¡¡RESPUESTA INCORRECTA!!!");

        // set dialog message
        alertDialogBuilder
                .setMessage("¿Desea volver a la pantalla inicial o continuar?")
                .setCancelable(false)
                .setPositiveButton("Continuar",new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        // if this button is clicked, close
                        dialog.cancel();
                        Toast.makeText(getApplicationContext(), "La respuesta correcta es: " + listButtons.get(responseCorrect).getText().toString().toUpperCase(), Toast.LENGTH_SHORT).show();
                        setQuestions();
                    }
                })
                .setNegativeButton("Inicio",new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        // if this button is clicked, just close
                        // the dialog box and do nothing
                        GameActivity.this.finish();
                    }
                });

        // show it
        alertDialogBuilder.show();
    }

    /*
     * Método para refrescar la interfaz con una nueva pregunta y respuestas despues de un pequeño periodo de tiempo
     */
    private void reloadQuestions(int toastLength){
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                setQuestions();
                unlockButtons();
            }
        }, toastLength);
    }


    /*
     * Método para reproducir el sonido de la pregunta
     */
    private void playSoundQuestion(String pathSound){
        int resId = getResources().getIdentifier(pathSound, "raw", this.getPackageName());

        String uri = new String("R.raw.").concat(pathSound);
        Log.d("debug", uri);
        mediaPlayer = MediaPlayer.create(this, resId);
        mediaPlayer.start();

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                unlockButtons();
                mediaPlayer.stop();
            }
        }, mediaPlayer.getDuration());
    }

    /*
     * Método para finalizar el juego
     */
    private void finishGame(){
        AlertDialog.Builder builder = new AlertDialog.Builder(GameActivity.this);

        builder.setTitle("FIN DEL JUEGO")
                .setMessage("Gracias por participar. ¿Te atreves a volver a jugar?");

        builder.show();

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Log.d("debug", "aciertos: " + numAciertos);
                Log.d("debug", "fallos: " + numFallos);
                GameActivity.this.finish();
            }
        }, SHORT_DELAY);
    }
}
