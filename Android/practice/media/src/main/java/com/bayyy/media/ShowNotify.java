package com.bayyy.media;

import android.Manifest;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.util.Log;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.app.NotificationCompat;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class ShowNotify extends AppCompatActivity {

  private static final String TAG = "Log";

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.notify_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    findViewById(R.id.btn_show).setOnClickListener(v -> {
      // 获取通知管理器
      NotificationManager manager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
      // Android 8.0及以上需要建立消息通道, 否则会报错: No channel found for notification
      if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
        Log.d(TAG, "onCreate: Crete Channel");
        String channelId = "1";
        CharSequence channelName = "channel1";
        String channelDescription = "This is channel 1";
        int channelImportance = android.app.NotificationManager.IMPORTANCE_HIGH;
        NotificationChannel channel = new NotificationChannel(channelId, channelName, channelImportance);
        channel.setDescription(channelDescription);
        Log.d(TAG, "onCreate: Create Channel" + channel);
        manager.createNotificationChannel(channel);
      }
      PendingIntent pi = PendingIntent.getActivity(this, 0, new Intent(this, JumpPage.class), PendingIntent.FLAG_IMMUTABLE);
      // 创建通知
      Notification notify = new NotificationCompat.Builder(this, "1")
          .setContentTitle("Title")
          .setContentText("This is the content")
          .setWhen(System.currentTimeMillis())
          .setSmallIcon(R.mipmap.ic_launcher)
          .setContentIntent(pi)
//          .setLargeIcon(BitmapFactory.decodeResource(getResources(), R.mipmap.ic_launcher))
          .build();
      manager.notify(1, notify);
    });
  }
}