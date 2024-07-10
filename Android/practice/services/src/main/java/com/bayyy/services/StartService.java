package com.bayyy.services;

import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class StartService extends AppCompatActivity {
  private MyService.DownloadBinder downloadBinder;
  private ServiceConnection connection = new ServiceConnection() {
    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
      downloadBinder = (MyService.DownloadBinder) service;
      downloadBinder.startDownload();
      downloadBinder.getProgress();
    }

    @Override
    public void onServiceDisconnected(ComponentName name) {
    }
  };

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.start_service_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    findViewById(R.id.btn_start).setOnClickListener(v -> {
      startService(new Intent(this, MyService.class));
    });
    findViewById(R.id.btn_stop).setOnClickListener(v -> {
      stopService(new Intent(this, MyService.class));
    });
    findViewById(R.id.btn_bind_service).setOnClickListener(v -> {
      // 绑定服务
      // 第一个参数是Intent对象，第二个参数是ServiceConnection对象, 第三个参数是一个标志位(这里传入BIND_AUTO_CREATE表示在Activity和Service建立关联后自动创建Service)
      bindService(new Intent(this, MyService.class), connection, BIND_AUTO_CREATE);
    });
    findViewById(R.id.btn_unbind_service).setOnClickListener(v -> {
      // 解绑服务
      unbindService(connection);
    });
  }
}