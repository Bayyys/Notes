package com.bayyy.ui;

import android.content.Context;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.widget.LinearLayout;
import android.widget.Toast;

import androidx.annotation.Nullable;

public class MyLayout extends LinearLayout {

  public MyLayout(Context context, @Nullable AttributeSet attrs) {
    super(context, attrs);
    LayoutInflater.from(context).inflate(R.layout.my_layout, this);
    findViewById(R.id.btn_back).setOnClickListener(v -> Toast.makeText(context, "Back", Toast.LENGTH_SHORT).show());
    findViewById(R.id.btn_exit).setOnClickListener(v -> Toast.makeText(context, "Exit", Toast.LENGTH_SHORT).show());
  }
}
