package com.bayyy.services.basic;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.os.Binder;
import android.os.IBinder;
import android.widget.Toast;

import com.bayyy.services.R;

public class DownloadService extends Service {
  private DownloadTask downloadTask;
  private String downloadUrl;
  private DownloadListener listener = new DownloadListener() {
    @Override
    public void onProgress(int progress) {
      getNotificationManager().notify(1, getNotification("Downloading...", progress));

    }

    @Override
    public void onSuccess() {
      downloadTask = null;
      stopForeground(true);
      getNotificationManager().notify(1, getNotification("Download Success", -1));
      Toast.makeText(DownloadService.this, "Download Success", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onFailed() {
      downloadTask = null;
      stopForeground(true);
      getNotificationManager().notify(1, getNotification("Download Failed", -1));
      Toast.makeText(DownloadService.this, "Download Failed", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onPaused() {
      downloadTask = null;
      Toast.makeText(DownloadService.this, "Paused", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onCanceled() {
      downloadTask = null;
      stopForeground(true);
      Toast.makeText(DownloadService.this, "Canceled", Toast.LENGTH_SHORT).show();
    }
  };

  private DownloadBinder mBinder = new DownloadBinder();

  class DownloadBinder extends Binder {
    public void startDownload(String url) {
      if (downloadTask == null) {
        downloadUrl = url;
        downloadTask = new DownloadTask(listener);
        downloadTask.execute(downloadUrl);
        startForeground(1, getNotification("Downloading...", 0));
        Toast.makeText(DownloadService.this, "Downloading...", Toast.LENGTH_SHORT).show();
      }
    }

    public void pauseDownload() {
      if (downloadTask != null) {
        downloadTask.pauseDownload();
      }
    }

    public void cancelDownload() {
      if (downloadTask != null) {
        downloadTask.cancelDownload();
      } else {
        if (downloadUrl != null) {
          String fileName = downloadUrl.substring(downloadUrl.lastIndexOf("/"));
          String directory = getExternalFilesDir(null).getPath();
          java.io.File file = new java.io.File(directory + fileName);
          if (file.exists()) {
            file.delete();
          }
          getNotificationManager().cancel(1);
          stopForeground(true);
          Toast.makeText(DownloadService.this, "Canceled", Toast.LENGTH_SHORT).show();
        }
      }
    }
  }

  private Notification getNotification(String title, int progress) {
    Intent intent = new Intent(this, DownloadUse.class);
    PendingIntent pi = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE);
    Notification.Builder builder = new Notification.Builder(this);
    builder.setContentTitle(title);
    builder.setSmallIcon(R.mipmap.ic_launcher);
    builder.setLargeIcon(BitmapFactory.decodeResource(getResources(), R.mipmap.ic_launcher));
    builder.setContentIntent(pi);
    if (progress > 0) {
      builder.setContentText(progress + "%");
      builder.setProgress(100, progress, false);
    }
    return builder.build();
  }

  private NotificationManager getNotificationManager() {
    return (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
  }

  public DownloadService() {
  }

  @Override
  public IBinder onBind(Intent intent) {
    return mBinder;
  }
}