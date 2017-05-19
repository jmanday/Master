package com.jesusgarciamanday.practica5;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;

/**
 * Created by jesusgarciamanday on 1/2/17.
 */

public class OtherGamesActivity extends AppCompatActivity {

    private Button buttonGame1, buttonGame2, buttonGame3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_other_games);

        buttonGame1 = (Button) findViewById(R.id.buttonGame1);
        buttonGame2 = (Button) findViewById(R.id.buttonGame2);
        buttonGame3 = (Button) findViewById(R.id.buttonGame3);

        buttonGame1.setText("PAC-ON DELUXE");
        buttonGame2.setText("ZOMBIE CRISIS");
        buttonGame3.setText("SUPER STACK");

        setGames();
    }

    private void setGames(){
        buttonGame1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(OtherGamesActivity.this, webViewActivity.class);
                Bundle b = new Bundle();
                b.putString("url", "https://m.minijuegos.com/juego/pac-xon-deluxe/jugar");
                intent.putExtras(b);
                startActivity(intent);
            }
        });

        buttonGame2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(OtherGamesActivity.this, webViewActivity.class);
                Bundle b = new Bundle();
                b.putString("url", "https://m.minijuegos.com/juego/zombie-crisis/jugar");
                intent.putExtras(b);
                startActivity(intent);
            }
        });

        buttonGame3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(OtherGamesActivity.this, webViewActivity.class);
                Bundle b = new Bundle();
                b.putString("url", "https://m.minijuegos.com/juego/super-stack/jugar");
                intent.putExtras(b);
                startActivity(intent);
            }
        });
    }
}
