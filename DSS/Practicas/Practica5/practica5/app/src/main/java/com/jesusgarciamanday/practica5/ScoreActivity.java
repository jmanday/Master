package com.jesusgarciamanday.practica5;

import android.database.Cursor;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.ListView;

import java.util.ArrayList;

/**
 * Created by jesusgarciamanday on 1/2/17.
 */

public class ScoreActivity extends AppCompatActivity {

    private PresenterDataSource pDataBase;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_scores);

        listView = (ListView) findViewById(R.id.listScores);

        // obtengo la instancia de la base de datos
        this.pDataBase = ImplPresentDataSource.getInstance(this);

        Cursor cuestiones = this.pDataBase.getAllScores();

        ArrayList<Score> arrayListScores = Score.converToScores(cuestiones);
        ScoreAdapter adapter = new ScoreAdapter(this, arrayListScores);
        listView.setAdapter(adapter);


        Log.d("debug", "tamaño: " + arrayListScores.size());
    }
}
