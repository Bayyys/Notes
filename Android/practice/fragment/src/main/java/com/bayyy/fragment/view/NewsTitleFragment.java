package com.bayyy.fragment.view;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.bayyy.fragment.NewsContentActivity;
import com.bayyy.fragment.R;
import com.bayyy.fragment.pojo.News;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class NewsTitleFragment extends Fragment {
  private boolean isTwoPane;  // 是否是双页模式

  @Nullable
  @Override
  public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
    View view = inflater.inflate(R.layout.news_title_frag, container, false);
    RecyclerView newsTitleRecyclerView = view.findViewById(R.id.news_title_recycler_view);
    LinearLayoutManager layoutManager = new LinearLayoutManager(getActivity());
    newsTitleRecyclerView.setLayoutManager(layoutManager);
    NewsAdapter adapter = new NewsAdapter(getNews());
    newsTitleRecyclerView.setAdapter(adapter);
    return view;
  }

  private List<News> getNews() {
    List<News> newsList = new ArrayList<>();
    for (int i = 0; i < 50; i++) {
      News news = new News();
      news.setTitle("This is news title " + i);
      news.setContent(getRandomLengthContent("This is news content " + i + ". "));
      newsList.add(news);
    }
    return newsList;
  }

  private String getRandomLengthContent(String content) {
    Random random = new Random();
    int length = random.nextInt(20) + 1;
    StringBuilder builder = new StringBuilder();
    for (int i = 0; i < length; i++) {
      builder.append(content);
    }
    return builder.toString();
  }

  @Override
  public void onActivityCreated(@Nullable Bundle savedInstanceState) {
    super.onActivityCreated(savedInstanceState);
    if (getActivity().findViewById(R.id.news_content_fragment) != null) {
      isTwoPane = true;  // 可以找到news_content_layout布局时，为双页模式
    } else {
      isTwoPane = false;  // 找不到news_content_layout布局时，为单页模式
    }
  }

  class NewsAdapter extends RecyclerView.Adapter<NewsAdapter.ViewHolder> {

    private List<News> mNewsList;

    public class ViewHolder extends RecyclerView.ViewHolder {

      TextView newsTitleText;

      public ViewHolder(@NonNull View itemView) {
        super(itemView);
        newsTitleText = itemView.findViewById(R.id.news_title);
      }
    }

    public NewsAdapter(List<News> mNewsList) {
      this.mNewsList = mNewsList;
    }

    @NonNull
    @Override
    public NewsAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
      View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.news_item, parent, false);
      final ViewHolder holder = new ViewHolder(view);
      view.setOnClickListener(v -> {
        News news = mNewsList.get(holder.getAdapterPosition());
        if (isTwoPane) {  // 双页模式
          NewsContentFragment newsContentFragment = (NewsContentFragment) getFragmentManager().findFragmentById(R.id.news_content_fragment);
          newsContentFragment.refresh(news.getTitle(), news.getContent());
        } else {
          NewsContentActivity.actionStart(getActivity(), news.getTitle(), news.getContent());
        }
      });
      return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull NewsAdapter.ViewHolder holder, int position) {
      News news = mNewsList.get(position);
      holder.newsTitleText.setText(news.getTitle());

    }

    @Override
    public int getItemCount() {
      return mNewsList.size();
    }

  }
}
