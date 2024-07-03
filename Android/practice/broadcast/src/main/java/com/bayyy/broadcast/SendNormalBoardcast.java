package com.bayyy.broadcast;

import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;

public class SendNormalBoardcast extends AppCompatActivity {
  public static final String TAG = "SendNormalBoardcast";
  private LocalBroadcastManager localBroadcastManager;
  private LocalReceiver localReceiver;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.send_normal_boardcast_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    localBroadcastManager = LocalBroadcastManager.getInstance(this);
    findViewById(R.id.btn_send).setOnClickListener(v -> {
      Log.d(TAG, "onCreate: send broadcast");
      Intent intent = new Intent("com.bayyy.MY_NORMAL");
      // Android 8.0 之后，静态注册的广播接收器无法接收隐式广播，需要指定包名
      intent.setPackage(getPackageName());  // 指定包名, 使得广播只能被本应用接收
      intent.setComponent(new ComponentName("com.bayyy.broadcastreceiver", "com.bayyy.broadcastreceiver.OtherAppReceiver"));  // 指定接收器, 完整应用名+接收器名, 适用于跨应用广播
      sendOrderedBroadcast(intent, "com.bayyy.MY_PER");
    });

    findViewById(R.id.btn_send_local).setOnClickListener(v -> {
      Log.d(TAG, "onCreate: send local broadcast");
      Intent intent = new Intent("com.bayyy.MY_LOCAL");
      localBroadcastManager.sendBroadcast(intent);
    });
    localReceiver = new LocalReceiver();
    localBroadcastManager.registerReceiver(localReceiver, new IntentFilter("com.bayyy.MY_LOCAL"));
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    localBroadcastManager.unregisterReceiver(localReceiver);
  }

  class LocalReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
      Toast.makeText(context, "LocalReceiver", Toast.LENGTH_SHORT).show();
    }
  }
}