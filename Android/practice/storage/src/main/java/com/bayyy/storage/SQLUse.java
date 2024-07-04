package com.bayyy.storage;

import android.content.ContentValues;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.storage.db.MyDatabaseHelper;

public class SQLUse extends AppCompatActivity {

  public static MyDatabaseHelper dbHelper;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.sql_use_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    dbHelper = new MyDatabaseHelper(this, "BookStore.db", null, 2);
    // Create database
    findViewById(R.id.btn_create_db).setOnClickListener(v -> {
      startActivity(new Intent(this, MyDatabaseHelper.class));
    });
    // Insert data
    findViewById(R.id.btn_insert).setOnClickListener(v -> {
      SQLiteDatabase db = dbHelper.getWritableDatabase();
      ContentValues values = new ContentValues();
      // 装载第一组数据
      values.put("name", "The Da Vinci Code");
      values.put("author", "Dan Brown");
      values.put("pages", 454);
      values.put("price", 16.96);
      db.insert("Book", null, values);
      values.clear(); // 清空ContentValues对象
      // 装载第二组数据
      values.put("name", "The Lost Symbol");
      values.put("author", "Dan Brown");
      values.put("pages", 510);
      values.put("price", 19.95);
      db.insert("Book", null, values);
      // SQL 语法
//      db.execSQL("insert into Book (name, author, pages, price) values(?, ?, ?, ?)",
//          new String[]{"The Da Vinci Code", "Dan Brown", "454", "16.96"});
    });
    // Update data
    findViewById(R.id.btn_update).setOnClickListener(v -> {
      SQLiteDatabase db = dbHelper.getWritableDatabase();
      ContentValues values = new ContentValues();
      values.put("price", 10.99);
      db.update("Book", values, "name = ?", new String[]{"The Da Vinci Code"});
//      db.execSQL("update Book set price = ? where pages > ?", new String[]{"10.99", "500"});
    });
    // Delete data
    findViewById(R.id.btn_delete).setOnClickListener(v -> {
      SQLiteDatabase db = dbHelper.getWritableDatabase();
      db.delete("Book", "pages > ?", new String[]{"500"});
//      db.execSQL("delete from Book where pages < ?", new String[]{"500"});
    });
    // Select data
    findViewById(R.id.btn_query).setOnClickListener(v -> {
      SQLiteDatabase db = dbHelper.getWritableDatabase();
      Cursor cursor = db.query("Book", null, null, null, null, null, null);
      if (cursor.moveToFirst()) {
        do {
          // 遍历Cursor对象，取出数据并打印
          String name = cursor.getString(cursor.getColumnIndex("name"));
          String author = cursor.getString(cursor.getColumnIndex("author"));
          int pages = cursor.getInt(cursor.getColumnIndex("pages"));
          double price = cursor.getDouble(cursor.getColumnIndex("price"));
          System.out.println("Book name is " + name);
          System.out.println("Book author is " + author);
          System.out.println("Book pages is " + pages);
          System.out.println("Book price is " + price);
        } while (cursor.moveToNext());
      }
      cursor.close();
//      Cursor cursor = db.rawQuery("select * from Book where pages > ?", new String[]{"400"});
    });

  }
}