package com.bayyy.ui;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.recyclerview.widget.StaggeredGridLayoutManager;

import com.bayyy.ui.controller.ReFruitAdapter;
import com.bayyy.ui.pojo.Fruit;

import java.util.ArrayList;
import java.util.List;

public class RecyclerViewLayout extends AppCompatActivity {
  private List<Fruit> fruitList = new ArrayList<>();

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.recycler_view_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    initFruits();
    RecyclerView recyclerView = (RecyclerView) findViewById(R.id.recycler_view);
//    LinearLayoutManager manager = new LinearLayoutManager(this);
    StaggeredGridLayoutManager manager = new StaggeredGridLayoutManager(3, StaggeredGridLayoutManager.VERTICAL);
    recyclerView.setLayoutManager(manager);
    ReFruitAdapter fruitAdapter = new ReFruitAdapter(fruitList);
    recyclerView.setAdapter(fruitAdapter);

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