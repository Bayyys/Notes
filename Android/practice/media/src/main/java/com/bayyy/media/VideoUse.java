package com.bayyy.media;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;
import android.widget.VideoView;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.media.util.MyValue;

import java.util.Objects;

public class VideoUse extends AppCompatActivity {
  private static final int CHOOSE_VIDEO = 1;
  VideoView videoView;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.video_use_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    videoView = findViewById(R.id.video);
    requestPer();
    findViewById(R.id.play).setOnClickListener(v -> videoView.start());
    findViewById(R.id.pause).setOnClickListener(v -> videoView.pause());
    findViewById(R.id.replay).setOnClickListener(v -> videoView.resume());
  }

  private void requestPer() {
    if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.READ_EXTERNAL_STORAGE) == android.content.pm.PackageManager.PERMISSION_GRANTED) {
      openVide();
    } else {
      requestPermissions(new String[]{android.Manifest.permission.READ_EXTERNAL_STORAGE}, 0);
    }
  }

  private void openVide() {
    Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
    intent.setType("video/*");
    startActivityForResult(intent, CHOOSE_VIDEO);
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    switch (requestCode) {
      case CHOOSE_VIDEO:
        if (resultCode == RESULT_OK) {
          Log.d(MyValue.TAG, "onActivityResult: " + Objects.requireNonNull(data).getData());
          videoView.setVideoURI(data.getData());
        }
        break;
      default:
        break;
    }
  }

  @Override
  public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    switch (requestCode) {
      case 0:
        if (grantResults[0] == android.content.pm.PackageManager.PERMISSION_GRANTED) {
          openVide();
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
    // 销毁
    if (videoView != null) {
      videoView.suspend();
    }
  }
}