package com.bayyy.storage;

import android.database.Cursor;
import android.graphics.ColorSpace;
import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.storage.pojo.Book;

import org.litepal.LitePal;
import org.litepal.LitePalDB;
import org.litepal.crud.LitePalSupport;
import org.litepal.tablemanager.Connector;

import java.util.List;

public class LitePalUse extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.lite_pal_use_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    findViewById(R.id.btn_create).setOnClickListener(v -> {
      Connector.getDatabase();
    });
    findViewById(R.id.btn_insert).setOnClickListener(v -> {
      Book book = new Book();
      book.setAuthor("Bayyy");
      book.setName("Android");
      book.setPages(454);
      book.setPrice(16.96);
      book.save();
    });
    findViewById(R.id.btn_update).setOnClickListener(v -> {
      Book book = new Book();
      book.setPrice(14.95);
      book.setToDefault("pages");
      book.updateAll("name = ?", "Android");
    });
    findViewById(R.id.btn_delete).setOnClickListener(v -> {
      LitePal.deleteAll(Book.class, "pages < ?", "500");
    });
    findViewById(R.id.btn_query).setOnClickListener(v -> {
      Book bookFirst = LitePal.findFirst(Book.class);  // 查询第一条数据
      Book bookLast = LitePal.findLast(Book.class);  // 查询第一条数据
      List<Book> books1 = LitePal.findAll(Book.class);
      List<Book> books2 = LitePal.select("name", "author").find(Book.class);
      List<Book> books3 = LitePal.where("pages > ?", "400").find(Book.class);
      List<Book> books4 = LitePal.order("pages desc").find(Book.class);
      List<Book> books5 = LitePal.limit(3).find(Book.class);
      List<Book> books6 = LitePal.limit(3).offset(1).find(Book.class);
      // 完整查询语句
      List<Book> books7 = LitePal.select("name", "author", "pages")
          .where("pages > ?", "400")
          .order("pages desc")
          .limit(3)
          .offset(1)
          .find(Book.class);
    });
    // 原生 SQL 查询
    Cursor cursor = LitePal.findBySQL("select * from Book where pages > ?", "400");
  }
}