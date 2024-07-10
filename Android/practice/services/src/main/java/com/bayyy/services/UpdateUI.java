package com.bayyy.services;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class UpdateUI extends AppCompatActivity {
  public static final int UPDATE_TEXT = 1;
  private TextView tv_content;
  private Handler handler = new Handler(Looper.getMainLooper()) {
    public void handleMessage(android.os.Message msg) {
      switch (msg.what) {
        case UPDATE_TEXT:
          tv_content.setText("Now, update the content!");
          break;
        default:
          break;
      }
    }
  };

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.update_ui_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    tv_content = findViewById(R.id.tv_content);
    findViewById(R.id.btn_change_text).setOnClickListener(v -> {
      new Thread(() -> {
        Message message = new Message();
        message.what = UPDATE_TEXT;
        handler.sendMessage(message);
      }).start();
    });
  }
}