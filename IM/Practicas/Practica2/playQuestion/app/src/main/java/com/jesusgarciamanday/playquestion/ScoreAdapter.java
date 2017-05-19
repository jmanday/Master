package com.jesusgarciamanday.playquestion;

import android.content.Context;
import android.support.annotation.NonNull;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by jesusgarciamanday on 7/2/17.
 */

public class ScoreAdapter extends ArrayAdapter<Score> {

    public ScoreAdapter(Context context, ArrayList<Score> scores) {
        super(context, 0, scores);
    }

    @NonNull
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        Score score = getItem(position);

        if(convertView == null)
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.layout_cell, parent, false);

        TextView txtLabel = (TextView) convertView.findViewById(R.id.textLabel);
        TextView txtNum = (TextView) convertView.findViewById(R.id.textNum);
        TextView txtLabel2 = (TextView) convertView.findViewById(R.id.textLabel2);
        TextView txtNum2 = (TextView) convertView.findViewById(R.id.textNum2);

        txtLabel.setText("Número de aciertos: ");
        txtNum.setText(String.valueOf(score.getNumSuccess()));
        txtLabel2.setText("Número de errores: ");
        txtNum2.setText(String.valueOf(score.getNumFailure()));

        return convertView;
    }
}
