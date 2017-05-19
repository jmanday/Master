package com.jesusgarciamanday.playquestion;

import android.database.Cursor;

import java.util.ArrayList;

/**
 * Created by jesusgarciamanday on 7/2/17.
 */

public class Score {

    private static int count = 0;
    private int idGame;
    private int numSuccess;
    private int numFailure;

    public Score(String idGame, String success, String failure) {
        this.idGame = Integer.parseInt(idGame);
        this.numSuccess = Integer.parseInt(success);
        this.numFailure = Integer.parseInt(failure);
    }

    public static enum Fields {
        ID_GAME(0),
        SUCCESS(1),
        FAILURE(2);

        private final int field;

        private Fields(int f) {
            this.field = f;
        }

        public int getValue(){
            return field;
        }
    }

    public Score(int numSuccess, int numFailure){
        this.idGame = count++;
        this.numSuccess = numSuccess;
        this.numFailure = numFailure;
    }

    public int getIdGame(){
        return this.idGame;
    }

    public int getNumSuccess(){
        return this.numSuccess;
    }

    public int getNumFailure(){
        return this.numFailure;
    }

    public void setNumSuccess(int numSuccess){
        this.numSuccess = numSuccess;
    }

    public void setNumFailure(int numFailure){
        this.numFailure = numFailure;
    }

    public static ArrayList<Score> converToScores(Cursor c){

        Score s;
        ArrayList<Score> listScores = new ArrayList<>();

        if(c != null){
            while(c.moveToNext()){
                s = new Score(Integer.parseInt(c.getString(Fields.SUCCESS.getValue())),
                       Integer.parseInt(c.getString(Fields.FAILURE.getValue())));

                listScores.add(s);
            }
        }

        return listScores;
    }
}
