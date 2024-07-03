package com.bayyy.broadcast;

import android.content.Intent;
import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.broadcast.controller.BaseActivity;

public class LoginSuccess extends BaseActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.login_success_layout);
    findViewById(R.id.force_offline).setOnClickListener(v ->
    {
      Intent intent = new Intent("com.bayyy.FORCE");
      sendBroadcast(intent);
    });
  }
}