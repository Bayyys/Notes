package com.bayyy.ui;

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
    findViewById(R.id.btn_custom_widget).setOnClickListener(v -> {
      startActivity(new Intent(this, CustomWidget.class));
    });
    findViewById(R.id.btn_linear).setOnClickListener(v -> {
      startActivity(new Intent(this, Linear.class));
    });
    findViewById(R.id.btn_relative).setOnClickListener(v -> {
      startActivity(new Intent(this, Relative.class));
    });
    findViewById(R.id.btn_frame).setOnClickListener(v -> {
      startActivity(new Intent(this, Frame.class));
    });
    findViewById(R.id.btn_percent).setOnClickListener(v -> {
      startActivity(new Intent(this, Percent.class));
    });
    findViewById(R.id.btn_my).setOnClickListener(v -> {
      startActivity(new Intent(this, UseMyLayout.class));
    });
    findViewById(R.id.btn_listview).setOnClickListener(v -> {
      startActivity(new Intent(this, ListViewLayout.class));
    });
    findViewById(R.id.btn_my_listview).setOnClickListener(v -> {
      startActivity(new Intent(this, MyListView.class));
    });
    findViewById(R.id.btn_recyclerview).setOnClickListener(v -> {
      startActivity(new Intent(this, RecyclerViewLayout.class));
    });
  }
}