package com.jesusgarciamanday.practica5;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

/**
 * Created by jesusgarciamanday on 1/2/17.
 */

public class MainActivity extends AppCompatActivity {

    private Button buttonPlay;
    private Button buttonResults;
    private Button buttonOtherGames;
    private ImplPresentDataSource db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_main);

        buttonPlay = (Button) findViewById(R.id.buttonPlay);
        buttonResults = (Button) findViewById(R.id.buttonResults);
        buttonOtherGames = (Button) findViewById(R.id.buttonOtherGames);

        // obtengo la instancia de la base de datos
        this.db = ImplPresentDataSource.getInstance(this);
        //this.db.deleteDB();

        setOptions();
    }


    private void setOptions(){

        buttonPlay.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent launchPlay = new Intent(MainActivity.this, GameActivity.class);

                startActivity(launchPlay);
            }
        });


        buttonResults.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent launchResults = new Intent(MainActivity.this, ScoreActivity.class);

                startActivity(launchResults);
            }
        });


        buttonOtherGames.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent launchOtherGames = new Intent(MainActivity.this, OtherGamesActivity.class);

                startActivity(launchOtherGames);
            }
        });
    }
}
