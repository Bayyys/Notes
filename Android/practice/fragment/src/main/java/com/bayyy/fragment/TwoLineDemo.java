package com.bayyy.fragment;

import android.nfc.Tag;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import com.bayyy.fragment.view.AnotherRightFragment;
import com.bayyy.fragment.view.LeftFragment;
import com.bayyy.fragment.view.RightFragment;

public class TwoLineDemo extends AppCompatActivity {

  private static final String TAG = "TwoLineDemo";

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.two_line_demo_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    FragmentManager fragmentManager = this.getSupportFragmentManager();
    LeftFragment fragment = (LeftFragment) fragmentManager.findFragmentById(R.id.left_fragment);
    Button btn_jump = fragment.getView().findViewById(R.id.btn_left_fragment);
//    Button btn_jump = findViewById(R.id.btn_left_fragment);
    btn_jump.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View v) {
        Log.d(TAG, "onClick: test");
        replaceFragment(new AnotherRightFragment());
      }
    });
    replaceFragment(new RightFragment());
  }

  private void replaceFragment(Fragment fragment) {
    Log.d(TAG, "onClick: replaceFragment");
    FragmentManager fragmentManager = getSupportFragmentManager();
    FragmentTransaction transaction = fragmentManager.beginTransaction();
    transaction.replace(R.id.right_layout, fragment);
    transaction.addToBackStack(null);
    transaction.commit();
  }
}