package com.jesusgarciamanday.playquestion.services;

/**
 * Created by jesusgarciamanday on 18/5/17.
 */

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;



public class ReceiverBoot extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {

        // LANZAR SERVICIO
        System.out.println("COMENZAANDOO");
        Intent serviceIntent = new Intent(context, ServiceBootDevice.class);
        context.startService(serviceIntent);

    }
}
