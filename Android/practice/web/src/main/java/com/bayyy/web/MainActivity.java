package com.bayyy.web;

import android.content.Intent;
import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.main_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    findViewById(R.id.web_demo).setOnClickListener(v -> startActivity(new Intent(this, WebViewDemo.class)));
    findViewById(R.id.btn_get_data).setOnClickListener(v -> startActivity(new Intent(this, GetHttp.class)));
    findViewById(R.id.btn_parse).setOnClickListener(v -> startActivity(new Intent(this, ParseUse.class)));
  }
}