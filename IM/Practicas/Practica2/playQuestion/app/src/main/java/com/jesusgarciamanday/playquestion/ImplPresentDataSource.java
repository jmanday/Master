package com.jesusgarciamanday.playquestion;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by jesusgarciamanday on 1/2/17.
 */

/*
 * Clase creada para leer la base de datos sqlite
 */
public class ImplPresentDataSource extends SQLiteOpenHelper implements PresenterDataSource {

    private static final String sqlCreate1 = "CREATE TABLE Preguntas (" +
            "id INTEGER AUTO INCREMENT PRIMARY KEY, " +
            "pregunta VARCHAR(256) NOT NULL," +
            "respuesta VARCHAR(50) NOT NULL," +
            "respuesta_incorrecta_1 VARCHAR(50) NOT NULL," +
            "respuesta_incorrecta_2 VARCHAR(50) NOT NULL," +
            "respuesta_incorrecta_3 VARCHAR(50) NOT NULL," +
            "path_image VARCHAR(50) NOT NULL, " +
            "path_sound VARCHAR(50))";

    private static final String sqlCreate2 = "CREATE TABLE Puntuaciones (" +
            "idGame INTEGER AUTO INCREMENT PRIMARY KEY, " +
            "success INTEGER NOT NULL, " +
            "failure INTEGER NOT NULL)";

    private static final String NOMBRE_BD = "juego-questions.db";
    private static final int VERSION_ACTUAL_BD = 1;
    private static ImplPresentDataSource instance = null;
    private Context ctx;
    private SQLiteDatabase db;
    private ArrayList<Question> questions = new ArrayList<>();

    public static ImplPresentDataSource getInstance(Context context){
        if(instance == null)
            instance = new ImplPresentDataSource(context);

        return instance;
    }

    private ImplPresentDataSource(Context context) {
        super(context, NOMBRE_BD, null, VERSION_ACTUAL_BD);
        this.ctx = context;
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        //Se crea la tabla
        this.db = db;
        this.db.execSQL(sqlCreate1);
        this.db.execSQL(sqlCreate2);
        Log.d("debug", "Creando la base de datos");

        insertData(this.db);
        Log.d("debug", "Insertando los registros en la base de datos");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        //Se elimina la versión anterior de la tabla
        db.execSQL("DROP TABLE IF EXISTS Preguntas");
        db.execSQL("DROP TABLE IF EXISTS Puntuaciones");

        //Se crea las nuevas versiones de las tablas
        db.execSQL(sqlCreate1);
        db.execSQL(sqlCreate2);

        insertData(this.db);
        Log.d("debug", "Actualizando la base de datos de la versión " + oldVersion + " a la versión " + newVersion);
    }

    private void insertData(SQLiteDatabase db){

        StringBuilder sb = new StringBuilder();
        Question p;

        // Leemos el fichero donde se encuentran los registros
        Scanner sc = new Scanner(this.ctx.getResources().openRawResource(R.raw.database));
        while(sc.hasNext()){
            sb.append(sc.nextLine());
            sb.append('\n');
            if(sb.indexOf(";") == -1){
                p = new Question(sb);
                questions.add(p);
                sb.delete(0, sb.capacity());
            }
        }

        // Insertamos los registros en la base de datos
        for(int i = 0; i < questions.size(); i++){
            db.execSQL("INSERT INTO Preguntas(pregunta, respuesta, respuesta_incorrecta_1, "+
                    "respuesta_incorrecta_2, respuesta_incorrecta_3, path_image, path_sound) " +
                    "VALUES (" + questions.get(i).getPregunta() + "," + questions.get(i).getRespuesta() +
                    "," + questions.get(i).getRespuesta_incorrecta_1() + "," + questions.get(i).getRespuesta_incorrecta_2() +
                    "," + questions.get(i).getRespuesta_incorrecta_3() + "," + questions.get(i).getPath_image() +
                    "," + questions.get(i).getPath_sound() + ")");
        }
    }

    @Override
    public Cursor getQuestions(){
        return this.getWritableDatabase().rawQuery("SELECT * FROM Preguntas", null);
    }

    @Override
    public Cursor getAllScores(){
        return this.getWritableDatabase().rawQuery("SELECT * FROM Puntuaciones", null);
    }

    @Override
    public Cursor getScores(int idGame){
        String[] args = new String[] {String.valueOf(idGame)};
        return this.getWritableDatabase().rawQuery("SELECT * FROM Puntuaciones where idGame=?", args);
    }

    @Override
    public void deleteDB(){
        ctx.deleteDatabase(NOMBRE_BD);
        Log.d("debug", "Eliminando la base de datos");
    }

    @Override
    public PresenterDataSource getPresenter(Context context) {
        if(instance == null)
            instance = new ImplPresentDataSource(context);

        return instance;
    }

    @Override
    public void insertResult(Score score) {
        this.getWritableDatabase().execSQL("INSERT INTO Puntuaciones(success, failure) " +
                "VALUES (" + score.getNumSuccess() + "," +
                score.getNumFailure() + ")");
    }
}
