package com.bayyy.ui.controller;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.bayyy.ui.R;
import com.bayyy.ui.pojo.Fruit;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.util.List;

public class FruitAdapter extends ArrayAdapter<Fruit> {

  private int resourceId;

  public FruitAdapter(@NonNull Context context, int resource, @NonNull List<Fruit> objects) {
    super(context, resource, objects);
    resourceId = resource;
  }

  @NonNull
  @Override
  public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
    Fruit fruit = getItem(position);
    View view;
    ViewHolder viewHolder;
    if (convertView == null) {
      view = LayoutInflater.from(getContext()).inflate(resourceId, parent, false);
      viewHolder = new ViewHolder();
      viewHolder.fruitImage = (ImageView) view.findViewById(R.id.fruit_image);
      viewHolder.fruitName = (TextView) view.findViewById(R.id.fruit_name);
      view.setTag(viewHolder);
    } else {
      view = convertView;
      viewHolder = (ViewHolder) view.getTag();
    }
    viewHolder.fruitImage.setImageResource(fruit.getImageId());
    viewHolder.fruitName.setText(fruit.getName());
    return view;
  }

  class ViewHolder {
    ImageView fruitImage;
    TextView fruitName;
  }
}
