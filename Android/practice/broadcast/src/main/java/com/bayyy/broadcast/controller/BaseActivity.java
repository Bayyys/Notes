package com.bayyy.broadcast.controller;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.bayyy.broadcast.Login;

public class BaseActivity extends AppCompatActivity {
  private ForceReceiver receiver;

  @Override
  protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    ActivityController.addActivity(this);
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    ActivityController.removeActivity(this);
  }

  @Override
  protected void onResume() {
    super.onResume();
    IntentFilter intentFilter = new IntentFilter();
    intentFilter.addAction("com.bayyy.FORCE");
    receiver = new ForceReceiver();
    registerReceiver(receiver, intentFilter);
  }

  @Override
  protected void onPause() {
    super.onPause();
    if (receiver != null) {
      unregisterReceiver(receiver);
      receiver = null;
    }
  }

  class ForceReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
      AlertDialog.Builder builder = new AlertDialog.Builder(context);
      builder.setTitle("Warning");
      builder.setMessage("You are forced to be offline. Please try to login again.");
      builder.setCancelable(false);
      builder.setPositiveButton("OK", (dialog, which) -> {
        ActivityController.finishAll();
        Intent intent1 = new Intent(context, Login.class);
        context.startActivity(intent1);
      });
      builder.show();
    }
  }
}
