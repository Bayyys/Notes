package com.bayyy.ui.controller;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bayyy.ui.R;
import com.bayyy.ui.pojo.Fruit;

import java.util.List;

public class ReFruitAdapter extends RecyclerView.Adapter {
  private List<Fruit> mFruitList;

  static class ViewHolder extends RecyclerView.ViewHolder {
    View fruitView;
    ImageView fruitImage;
    TextView fruitName;

    public ViewHolder(@NonNull View itemView) {
      super(itemView);
      fruitView = itemView;
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
    final ViewHolder holder = new ViewHolder(view);
    holder.fruitView.setOnClickListener(v ->
        {
          int position = holder.getAdapterPosition();
          Fruit fruit = mFruitList.get(position);
          Toast.makeText(v.getContext(), "You clicked view " + fruit.getName(), Toast.LENGTH_SHORT).show();
        }
    );
    holder.fruitImage.setOnClickListener(v -> {
      int position = holder.getAdapterPosition();
      Fruit fruit = mFruitList.get(position);
      Toast.makeText(v.getContext(), "You clicked image " + fruit.getName(), Toast.LENGTH_SHORT).show();
    });
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
