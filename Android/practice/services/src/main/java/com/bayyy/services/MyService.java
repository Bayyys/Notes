package com.bayyy.services;

import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;
import android.util.Log;

public class MyService extends Service {
  private static final String TAG = "MyLog";
  private DownloadBinder mBinder = new DownloadBinder();

  class DownloadBinder extends Binder {
    public void startDownload() {
      Log.d(TAG, "startDownload executed");
    }

    public int getProgress() {
      Log.d(TAG, "getProgress executed");
      return 0;
    }
  }


  public MyService() {
  }

  @Override
  public void onCreate() {
    super.onCreate();
    Log.d(TAG, "MyService onCreate");
  }

  @Override
  public int onStartCommand(Intent intent, int flags, int startId) {
    Log.d(TAG, "MyService onStartCommand");
    return super.onStartCommand(intent, flags, startId);
  }

  @Override
  public void onDestroy() {
    super.onDestroy();
    Log.d(TAG, "MyService onDestroy");
  }

  @Override
  public IBinder onBind(Intent intent) {
    return mBinder;
  }
}