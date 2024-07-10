package com.bayyy.services;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.Build;
import android.os.IBinder;
import android.util.Log;

import androidx.core.app.NotificationCompat;

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
    // 获取通知管理器
    NotificationManager manager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
    String channelId = "1";
// Android 8.0及以上需要建立消息通道, 否则会报错: No channel found for notification
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
      Log.d(TAG, "onCreate: Crete Channel");
      channelId = "1";
      CharSequence channelName = "channel1";
      String channelDescription = "This is channel 1";
      int channelImportance = NotificationManager.IMPORTANCE_HIGH;
      NotificationChannel channel = new NotificationChannel(channelId, channelName, channelImportance);
      channel.setDescription(channelDescription);
      Log.d(TAG, "onCreate: Create Channel" + channel);
      manager.createNotificationChannel(channel);
    }
// 创建通知
    Notification notify = new NotificationCompat.Builder(this, channelId)  // 此处需要给定通知通道号
        .setContentTitle("Title")
        .setContentText("This is the content")
        .setWhen(System.currentTimeMillis())
        .setSmallIcon(R.mipmap.ic_launcher)
        .build();
    manager.notify(1, notify);
//    Log.d(TAG, "MyService onCreate"); Intent intent = new Intent(this, StartService.class);
//    PendingIntent pi = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE);
//    Notification notification = new NotificationCompat.Builder(this)
//        .setContentTitle("This is content title")
//        .setContentText("This is content text")
//        .setWhen(System.currentTimeMillis())
//        .setSmallIcon(R.mipmap.ic_launcher)
//        .setContentIntent(pi)
//        .build();
//    startForeground(1, notification);
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