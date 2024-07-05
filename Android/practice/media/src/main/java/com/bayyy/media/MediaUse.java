package com.bayyy.media;

import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.io.File;
import java.io.IOException;

public class MediaUse extends AppCompatActivity {
  private static final String TAG = "MyLog";
  private MediaPlayer media = new MediaPlayer();

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.media_use_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.READ_EXTERNAL_STORAGE) == android.content.pm.PackageManager.PERMISSION_GRANTED) {
      initMedia();
    } else {
      requestPermissions(new String[]{android.Manifest.permission.READ_EXTERNAL_STORAGE}, 0);
    }
    findViewById(R.id.btn_play).setOnClickListener(v -> media.start());
    findViewById(R.id.btn_pause).setOnClickListener(v -> media.pause());
    findViewById(R.id.btn_stop).setOnClickListener(v -> media.reset());
  }


  @Override
  protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode == 1 && resultCode == RESULT_OK) {
      Log.d(TAG, "onActivityResult: " + data.getData());
    }
  }

  private void initMedia() {
    try {
      File file = new File(Environment.getExternalStorageDirectory(), "music.mp3");
      media.setDataSource(file.getPath());
      media.prepare();
    } catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  @Override
  public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    switch (requestCode) {
      case 1:
        if (grantResults.length > 0 && grantResults[0] == android.content.pm.PackageManager.PERMISSION_GRANTED) {
          initMedia();
        } else {
          Toast.makeText(this, "Permission denied", Toast.LENGTH_SHORT).show();
          finish();
        }
        break;
      default:
        break;
    }
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    media.stop();
    media.release();
  }
}