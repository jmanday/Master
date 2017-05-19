package com.jesusgarciamanday.practica5;

import android.database.Cursor;

import java.util.ArrayList;

/**
 * Created by jesusgarciamanday on 1/2/17.
 */

public class Question {

    private String pregunta;
    private String respuesta;
    private String respuesta_incorrecta_1;
    private String respuesta_incorrecta_2;
    private String respuesta_incorrecta_3;
    private String path_image;
    private String path_sound;

    public static enum Fields {
        ID(0),
        PREGUNTA(1),
        RESPUESTA(2),
        RESPUESTA_INCORRECTA_1(3),
        RESPUESTA_INCORRECTA_2(4),
        RESPUESTA_INCORRECTA_3(5),
        PATH_IMAGE(6),
        PATH_SOUND(7);

        private final int field;

        private Fields(int f) {
            this.field = f;
        }

        public int getValue(){
            return field;
        }
    }

    public Question(String pregunta, String respuesta, String respuesta_incorrecta_1, String respuesta_incorrecta_2, String respuesta_incorrecta_3, String path_image, String path_sound){
        this.pregunta = pregunta;
        this.respuesta = respuesta;
        this.respuesta_incorrecta_1 = respuesta_incorrecta_1;
        this.respuesta_incorrecta_2 = respuesta_incorrecta_2;
        this.respuesta_incorrecta_3 = respuesta_incorrecta_3;
        this.path_image = path_image;
        this.path_sound = path_sound;
    }


    public Question(StringBuilder sb){
        String[] parts = sb.toString().split(",");

        this.pregunta = parts[0];
        this.respuesta = parts[1];
        this.respuesta_incorrecta_1 = parts[2];
        this.respuesta_incorrecta_2 = parts[3];
        this.respuesta_incorrecta_3 = parts[4];
        this.path_image = parts[5];
        this.path_sound = parts[6];
    }

    public static ArrayList<Question> converToQuestions(Cursor c){

        Question p;
        ArrayList<Question> listQuestions = new ArrayList<>();

        if(c != null){
            while(c.moveToNext()){
                p = new Question(c.getString(Question.Fields.PREGUNTA.getValue()), c.getString(Fields.RESPUESTA.getValue()),
                        c.getString(Fields.RESPUESTA_INCORRECTA_1.getValue()), c.getString(Fields.RESPUESTA_INCORRECTA_2.getValue()),
                        c.getString(Fields.RESPUESTA_INCORRECTA_3.getValue()), c.getString(Fields.PATH_IMAGE.getValue()),
                        c.getString(Fields.PATH_SOUND.getValue()));

                listQuestions.add(p);
            }
        }

        return listQuestions;
    }

    public String getPregunta(){
        return pregunta;
    }

    public String getRespuesta(){
        return respuesta;
    }

    public String[] getRespuestasErroneas() {
        return new String[]{respuesta_incorrecta_1, respuesta_incorrecta_2, respuesta_incorrecta_3};
    }

    public String getRespuesta_incorrecta_1() {
        return respuesta_incorrecta_1;
    }

    public String getRespuesta_incorrecta_2() {
        return respuesta_incorrecta_2;
    }

    public String getRespuesta_incorrecta_3() {
        return respuesta_incorrecta_3;
    }

    public String getPath_image() {
        return path_image;
    }

    public String getPath_sound() {
        return path_sound;
    }
}
