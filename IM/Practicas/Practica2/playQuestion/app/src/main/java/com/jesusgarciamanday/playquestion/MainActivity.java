package com.jesusgarciamanday.playquestion;

import android.Manifest;
import android.annotation.TargetApi;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.jesusgarciamanday.playquestion.listeners.OnPictureCapturedListener;
import com.jesusgarciamanday.playquestion.services.PictureService;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

/**
 * Created by jesusgarciamanday on 1/2/17.
 */

public class MainActivity extends AppCompatActivity implements OnPictureCapturedListener, ActivityCompat.OnRequestPermissionsResultCallback{

    public static final int MY_PERMISSIONS_REQUEST_ACCESS_CODE = 1;
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




    //**************** METODOS ******************

    private void setOptions() {

        buttonPlay.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new PictureService().startCapturing(MainActivity.this, MainActivity.this);

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


    @Override
    public void onCaptureDone(String pictureUrl, byte[] pictureData) {
        if (pictureData != null && pictureUrl != null) {
            System.out.println("Picture saved to " + pictureUrl);
        }
    }

    @Override
    public void onDoneCapturingAllPhotos(TreeMap<String, byte[]> picturesTaken) {
        if (picturesTaken != null && !picturesTaken.isEmpty()) {
            System.out.println("Done capturing all photos!");
            return;
        }
        System.out.println("No camera detected!");
    }


    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String permissions[], @NonNull int[] grantResults) {
        switch (requestCode) {
            case MY_PERMISSIONS_REQUEST_ACCESS_CODE: {
                if (!(grantResults.length > 0
                        && grantResults[0] == PackageManager.PERMISSION_GRANTED)) {
                    checkPermissions();
                }
            }
        }
    }

    // function to grant the permissions
    @TargetApi(Build.VERSION_CODES.M)
    private void checkPermissions() {
        final String[] requiredPermissions = {
                Manifest.permission.WRITE_EXTERNAL_STORAGE,
                Manifest.permission.CAMERA,
        };
        final List<String> neededPermissions = new ArrayList<>();
        for (final String p : requiredPermissions) {
            if (ContextCompat.checkSelfPermission(getApplicationContext(),
                    p) != PackageManager.PERMISSION_GRANTED) {
                neededPermissions.add(p);
            }
        }
        if (!neededPermissions.isEmpty()) {
            requestPermissions(neededPermissions.toArray(new String[]{}),
                    MY_PERMISSIONS_REQUEST_ACCESS_CODE);
        }
    }
}
