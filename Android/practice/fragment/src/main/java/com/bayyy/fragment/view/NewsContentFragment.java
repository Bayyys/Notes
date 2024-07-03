package com.bayyy.fragment.view;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.bayyy.fragment.R;

public class NewsContentFragment extends Fragment {
  private View view;

  @Nullable
  @Override
  public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
    view = inflater.inflate(R.layout.news_content_frag, container, false);
    return view;
  }

  public void refresh(String newsTitle, String newsContent) {
    View visibilityLayout = view.findViewById(R.id.visibility_layout);
    visibilityLayout.setVisibility(View.VISIBLE);
    TextView newsTitleView = (TextView) view.findViewById(R.id.news_title);
    TextView newsContentView = (TextView) view.findViewById(R.id.news_content);
    newsTitleView.setText(newsTitle);
    newsContentView.setText(newsContent);
  }
}
