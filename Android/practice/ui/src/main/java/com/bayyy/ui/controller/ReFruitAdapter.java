package com.bayyy.ui.controller;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bayyy.ui.R;
import com.bayyy.ui.pojo.Fruit;

import java.util.List;

public class ReFruitAdapter extends RecyclerView.Adapter {
  private List<Fruit> mFruitList;

  static class ViewHolder extends RecyclerView.ViewHolder {
    ImageView fruitImage;
    TextView fruitName;

    public ViewHolder(@NonNull View itemView) {
      super(itemView);
      fruitImage = itemView.findViewById(R.id.fruit_image);
      fruitName = itemView.findViewById(R.id.fruit_name);
    }

  }

  public ReFruitAdapter(List<Fruit> fruitList) {
    mFruitList = fruitList;
  }

  @NonNull
  @Override
  public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
    View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.fruit_item, parent, false);
    ViewHolder holder = new ViewHolder(view);
    return holder;
  }


  @Override
  public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) {
    Fruit fruit = mFruitList.get(position);
    ((ViewHolder) holder).fruitImage.setImageResource(fruit.getImageId());
    ((ViewHolder) holder).fruitName.setText(fruit.getName());

  }

  @Override
  public int getItemCount() {
    return mFruitList.size();
  }
}
