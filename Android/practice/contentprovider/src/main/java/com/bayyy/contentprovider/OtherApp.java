package com.bayyy.contentprovider;

import android.content.ContentValues;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Adapter;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.ArrayList;
import java.util.List;

public class OtherApp extends AppCompatActivity {
  List<String> books = new ArrayList<>();
  ListView listView;
  ArrayAdapter<String> adapter;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.other_app_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    listView = findViewById(R.id.list);
    adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, books);
    listView.setAdapter(adapter);
    // 增加数据
    findViewById(R.id.btn_add_book).setOnClickListener(v -> {
      Uri uri = Uri.parse("content://com.bayyy.dataset.provider/book");
      ContentValues values = new ContentValues();
      values.put("name", "A Clash of Kings");
      values.put("author", "George Martin");
      values.put("pages", 1040);
      values.put("price", 22.85);
      Uri newUri = getContentResolver().insert(uri, values);
      Toast.makeText(this, newUri.getLastPathSegment(), Toast.LENGTH_SHORT).show();
      queryAll();
    });
    // 删除数据
    findViewById(R.id.btn_delete_book).setOnClickListener(v -> {
      Uri uri = Uri.parse("content://com.bayyy.dataset.provider/book");
      getContentResolver().delete(uri, "name = ?", new String[]{"A Clash of Kings"});
      queryAll();
    });
    // 更新数据
    findViewById(R.id.btn_update_book).setOnClickListener(v -> {
      Uri uri = Uri.parse("content://com.bayyy.dataset.provider/book");
      ContentValues values = new ContentValues();
      values.put("price", 10.99);
      getContentResolver().update(uri, values, "name = ?", new String[]{"A Clash of Kings"});
      queryAll();
    });
    // 查询数据
    findViewById(R.id.btn_query_book).setOnClickListener(v -> {
      queryAll();
    });
  }

  private void queryAll() {
    Uri uri = Uri.parse("content://com.bayyy.dataset.provider/book");
    Cursor cursor = getContentResolver().query(uri, null, null, null, null);
    int no = 1;
    books.clear();
    if (cursor != null) {
      while (cursor.moveToNext()) {
        String name = cursor.getString(cursor.getColumnIndexOrThrow("name"));
        String author = cursor.getString(cursor.getColumnIndexOrThrow("author"));
        int pages = cursor.getInt(cursor.getColumnIndexOrThrow("pages"));
        double price = cursor.getDouble(cursor.getColumnIndexOrThrow("price"));
        books.add("No." + no + " Book name is " + name + ", author is " + author + ", pages is " + pages + ", price is " + price);
        no++;
      }
      cursor.close();
    }
    updateList();
  }

  private void updateList() {
    if (books.size() == 0) {
      findViewById(R.id.tv_msg).setVisibility(View.VISIBLE);
      listView.setVisibility(View.GONE);
    } else {
      findViewById(R.id.tv_msg).setVisibility(View.GONE);
      listView.setVisibility(View.VISIBLE);
      adapter.notifyDataSetChanged();
    }
  }
}