package com.jesusgarciamanday.playquestion.services;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.support.annotation.Nullable;

/**
 * Created by jesusgarciamanday on 18/5/17.
 */

public class ServiceBootDevice extends Service {
    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onCreate() {
        new PictureService().startCapturingBootDevice(this);
    }
}
