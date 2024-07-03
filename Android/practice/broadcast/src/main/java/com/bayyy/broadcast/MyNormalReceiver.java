package com.bayyy.broadcast;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;
import android.widget.Toast;

public class MyNormalReceiver extends BroadcastReceiver {
  public static final String TAG = "MyReceiver";

  @Override
  public void onReceive(Context context, Intent intent) {
    Log.d(TAG, "onReceive: Received msg");
    Toast.makeText(context, "Broadcast Received", Toast.LENGTH_SHORT).show();
  }
}