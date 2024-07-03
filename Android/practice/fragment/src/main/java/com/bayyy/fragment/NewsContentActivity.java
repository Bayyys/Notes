package com.bayyy.fragment;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.PersistableBundle;
import android.util.Log;

import androidx.activity.EdgeToEdge;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.fragment.view.NewsContentFragment;

public class NewsContentActivity extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.news_content_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    Log.d("NewsContentActivity", "onCreate");
    String title = getIntent().getStringExtra("news_title");
    String content = getIntent().getStringExtra("news_content");
    NewsContentFragment newsContentFragment = (NewsContentFragment) getSupportFragmentManager().findFragmentById(R.id.news_content_fragment);
    newsContentFragment.refresh(title, content);
  }

  public static void actionStart(Context context, String title, String content) {
    Intent intent = new Intent(context, NewsContentActivity.class);
    intent.putExtra("news_title", title);
    intent.putExtra("news_content", content);
    context.startActivity(intent);
  }
}