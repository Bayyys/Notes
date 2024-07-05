package com.bayyy.contentprovider.controller;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.bayyy.contentprovider.R;
import com.bayyy.contentprovider.pojo.MyContact;

public class ContactAdapter extends ArrayAdapter<MyContact> {
  private int resourceId;

  public ContactAdapter(@NonNull Context context, int resource) {
    super(context, resource);
    resourceId = resource;
  }

  @NonNull
  @Override
  public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
    MyContact contact = getItem(position);
    View v;
    ViewHolder holder;
    if (convertView == null) {
      v = LayoutInflater.from(getContext()).inflate(resourceId, parent, false);
      holder = new ViewHolder();
      holder.name = v.findViewById(R.id.tv_name);
      holder.phone = v.findViewById(R.id.tv_number);
      v.setTag(holder);
    } else {
      v = convertView;
      holder = (ViewHolder) v.getTag();
    }
    holder.name.setText(contact.getName());
    holder.phone.setText(contact.getPhone());
    return v;
  }

  class ViewHolder {
    TextView name;
    TextView phone;
  }
}
