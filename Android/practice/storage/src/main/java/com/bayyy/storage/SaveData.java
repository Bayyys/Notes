package com.bayyy.storage;

import android.os.Bundle;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class SaveData extends AppCompatActivity {
  private EditText edit;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.save_data_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    edit = (EditText) findViewById(R.id.et_data);
    load();
    findViewById(R.id.btn_save).setOnClickListener(v -> {
      save();
    });
    findViewById(R.id.btn_load).setOnClickListener(v -> {
      load();
    });
  }

  private void load() {
    FileInputStream in = null;
    BufferedReader read = null;
    StringBuilder content = new StringBuilder();  // 新建一个StringBuilder对象(content)用于存放读取的数据
    try {
      in = openFileInput("data"); // 通过openFileInput()方法获取FileInputStream对象
      read = new BufferedReader(new InputStreamReader(in)); // 通过 FileInputStream 对象构建 BufferedReader 对象
      String line = "";
      while ((line = read.readLine()) != null) {  // 逐行读取文件内容
        content.append(line);
      }
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      if (read != null) {
        try {
          read.close();
        } catch (Exception e) {
          e.printStackTrace();
        }
      }
    }
    edit.setText(content.toString());
    edit.setSelection(content.length());
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    save();
  }

  public void save() {
    String inputText = edit.getText().toString();
    FileOutputStream out = null;
    BufferedWriter writer = null;
    try {
      out = openFileOutput("data", MODE_PRIVATE);
      writer = new BufferedWriter(new OutputStreamWriter(out));
      writer.write(inputText);
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      try {
        if (writer != null) {
          writer.close();
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
  }
}