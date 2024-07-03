package com.bayyy.broadcast;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class BaseUse extends AppCompatActivity {
  private IntentFilter intentFilter;
  private NetworkChangeReceiver networkChangeReceiver;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    intentFilter = new IntentFilter();
    // 网络状态发生变化时会发送一条值为 android.net.conn.CONNECTIVITY_CHANGE 的广播
    // 此处作过滤器，只接收值为 android.net.conn.CONNECTIVITY_CHANGE 的广播
    intentFilter.addAction("android.net.conn.CONNECTIVITY_CHANGE");
    networkChangeReceiver = new NetworkChangeReceiver();
    // 注册广播接收器
    // 此时 NetworkChangeReceiver 会接受到值为 android.net.conn.CONNECTIVITY_CHANGE 的广播
    // Notice: 动态注册的广播接收器一定要取消注册，否则会导致内存泄漏
    registerReceiver(networkChangeReceiver, intentFilter);
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    // 取消注册广播接收器
    unregisterReceiver(networkChangeReceiver);
  }

  class NetworkChangeReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
      // 1. 简单提示网络状态发生变化
      // Toast.makeText(context, "Network is changed", Toast.LENGTH_SHORT).show());

      // 2. 获取网络连接管理器, 通过网络连接管理器获取网络连接信息
      ConnectivityManager connectivityManager = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
      // 访问系统等操作, 必须在 AndroidManifest.xml 中声明权限
      NetworkInfo activeNetworkInfo = connectivityManager.getActiveNetworkInfo();
      if (activeNetworkInfo != null && activeNetworkInfo.isAvailable()) {
        Toast.makeText(context, "Network is available", Toast.LENGTH_SHORT).show();
      } else {
        Toast.makeText(context, "Network is unavailable", Toast.LENGTH_SHORT).show();
      }
    }
  }
}