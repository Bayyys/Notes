package com.bayyy.storage;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class SharedData extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.shared_data_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    findViewById(R.id.btn_con).setOnClickListener(v -> {
      // Context 类中的 getSharedPreferences() 方法用于获取 SharedPreferences 对象
      // 可以指定包名
      SharedPreferences.Editor editor = getSharedPreferences("context_data", MODE_PRIVATE).edit();
      editor.putString("method", "Context");
      editor.putString("name", "Bay");
      editor.putInt("age", 18);
      editor.putBoolean("sex", true);
      editor.apply();
    });

    findViewById(R.id.btn_con_load).setOnClickListener(v -> {
      SharedPreferences preferences = getSharedPreferences("context_data", MODE_PRIVATE);
      String method = preferences.getString("method", "null");
      String name = preferences.getString("name", "null");
      int age = preferences.getInt("age", 0);
      boolean sex = preferences.getBoolean("sex", true);
      Toast.makeText(this, "Context\nMethod: " + method + "\nName: " + name + "\nAge: " + age + "\nSex: " + sex, Toast.LENGTH_SHORT).show();
    });

    findViewById(R.id.btn_act).setOnClickListener(v -> {
      // Activity 类中的 getPreferences() 方法用于获取 SharedPreferences 对象
      // 自动将 Activity 的类名作为 SharedPreferences 的文件名: SharedData.xml
      SharedPreferences.Editor editor = this.getPreferences(MODE_PRIVATE).edit();
      editor.putString("method", "Activity");
      editor.putString("name", "Bay");
      editor.putInt("age", 18);
      editor.putBoolean("sex", true);
      editor.apply();
    });


    findViewById(R.id.btn_act_load).setOnClickListener(v -> {
      SharedPreferences preferences = this.getPreferences(MODE_PRIVATE);
      String method = preferences.getString("method", "null");
      String name = preferences.getString("name", "null");
      int age = preferences.getInt("age", 0);
      boolean sex = preferences.getBoolean("sex", true);
      Toast.makeText(this, "Activity\nMethod: " + method + "\nName: " + name + "\nAge: " + age + "\nSex: " + sex, Toast.LENGTH_SHORT).show();
    });

    findViewById(R.id.btn_pre).setOnClickListener(v -> {
      // PreferenceManager 类中的 getDefaultSharedPreferences() 方法用于获取 SharedPreferences 对象
      // 自动将包名作为 SharedPreferences 的文件名: com.bayyy.storage_preferences.xml
      SharedPreferences.Editor editor = PreferenceManager.getDefaultSharedPreferences(this).edit();
      editor.putString("method", "PreferenceManager");
      editor.putString("name", "Bay");
      editor.putInt("age", 18);
      editor.putBoolean("sex", true);
      editor.apply();
    });

    findViewById(R.id.btn_pre_load).setOnClickListener(v -> {
      SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(this);
      String method = preferences.getString("method", "null");
      String name = preferences.getString("name", "null");
      int age = preferences.getInt("age", 0);
      boolean sex = preferences.getBoolean("sex", true);
      Toast.makeText(this, "PreferenceManager\nMethod: " + method + "\nName: " + name + "\nAge: " + age + "\nSex: " + sex, Toast.LENGTH_SHORT).show();
    });
  }
}