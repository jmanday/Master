package com.jesusgarciamanday.practica5;

import android.content.Context;
import android.database.Cursor;

/**
 * Created by jesusgarciamanday on 7/2/17.
 */

public interface PresenterDataSource {

    public Cursor getQuestions();
    public Cursor getScores(int idGame);
    public Cursor getAllScores();
    public void deleteDB();
    public PresenterDataSource getPresenter(Context context);
    public void insertResult(Score score);
}
