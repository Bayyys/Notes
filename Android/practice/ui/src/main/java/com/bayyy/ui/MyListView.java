package com.bayyy.ui;

import android.os.Bundle;
import android.widget.ListView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.ui.controller.FruitAdapter;
import com.bayyy.ui.pojo.Fruit;

import java.util.ArrayList;
import java.util.List;

public class MyListView extends AppCompatActivity {
  private List<Fruit> fruitList = new ArrayList<>();

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.my_list_view_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    initFruits();
    FruitAdapter fruitAdapter = new FruitAdapter(this, R.layout.fruit_item, fruitList);
    ListView listView = (ListView) findViewById(R.id.list_view);
    listView.setAdapter(fruitAdapter);
    listView.setOnItemClickListener((parent, view, position, id) -> {
      Fruit fruit = fruitList.get(position);
      Toast.makeText(MyListView.this, fruit.getName(), Toast.LENGTH_SHORT).show();
    });
  }

  private void initFruits() {
    for (int i = 0; i < 10; i++) {
      Fruit apple = new Fruit("Apple", R.drawable.apple);
      fruitList.add(apple);
      Fruit banana = new Fruit("Banana", R.drawable.banana);
      fruitList.add(banana);
      Fruit watermelon = new Fruit("Watermelon", R.drawable.watermelon);
      fruitList.add(watermelon);
    }
  }
}