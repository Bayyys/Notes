package com.bayyy.ui;

import android.app.AlertDialog;
import android.app.ProgressDialog;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class CustomWidget extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.custom_widget_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    // Button
    findViewById(R.id.btn_demo).setOnClickListener(v -> {
      String inputTxt = ((EditText) findViewById(R.id.et_text)).getText().toString();
      Toast.makeText(this, inputTxt, Toast.LENGTH_SHORT).show();
    });
    // ImageView
    ((ImageView) findViewById(R.id.img_view)).setImageResource(R.drawable.img);
    // ProgressBar
    ProgressBar progressBar = findViewById(R.id.progress_bar);
    findViewById(R.id.p_visiable).setOnClickListener(v -> progressBar.setVisibility(progressBar.getVisibility() == ProgressBar.VISIBLE ? ProgressBar.INVISIBLE : ProgressBar.VISIBLE));
    findViewById(R.id.p_style).setOnClickListener(v -> progressBar.setScrollBarStyle(progressBar.getScrollBarStyle() == ProgressBar.SCROLLBARS_INSIDE_OVERLAY ? ProgressBar.SCROLLBARS_INSIDE_INSET : ProgressBar.SCROLLBARS_INSIDE_OVERLAY));
    findViewById(R.id.p_add).setOnClickListener(v -> progressBar.setProgress(progressBar.getProgress() + 10));
    findViewById(R.id.p_add).setOnClickListener(v -> progressBar.setProgress(progressBar.getProgress() - 10));
    // AlertDialog
    findViewById(R.id.btn_alert).setOnClickListener(
        v -> {
          new AlertDialog.Builder(this)
              .setTitle("Alert Dialog")
              .setMessage("This is an alert dialog")
              .setPositiveButton("OK", (dialog, which) -> {
                Toast.makeText(this, "OK", Toast.LENGTH_SHORT).show();
              })
              .setNegativeButton("Cancel", (dialog, which) -> {
                Toast.makeText(this, "Cancel", Toast.LENGTH_SHORT).show();
              })
              .show();
        }
    );
    // ProgressDialog
    findViewById(R.id.btn_progress_dialog).setOnClickListener(
        v -> {
          ProgressDialog progressDialog = new ProgressDialog(this);
          progressDialog.setTitle("Progress Dialog");
          progressDialog.setMessage("This is a progress dialog");
          progressDialog.setCancelable(true);
          progressDialog.show();
        }
    );

  }

}