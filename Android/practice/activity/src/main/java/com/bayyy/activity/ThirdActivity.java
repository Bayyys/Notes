package com.bayyy.activity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.start.R;

public class ThirdActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.third_layout);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        Intent intent = getIntent();
        String data = intent.getStringExtra("extra_data");
        findViewById(R.id.btn_2).setOnClickListener(
                View -> {
                    Toast.makeText(ThirdActivity.this, data, Toast.LENGTH_SHORT).show();
                }
        );
        findViewById(R.id.btn_3).setOnClickListener(
                View -> {
                    Intent intent1 = new Intent();
                    intent1.putExtra("data_return", "Hello FirstActivity");
                    setResult(RESULT_OK, intent1);
                    finish();
                }
        );
    }


    @Override
    public void onBackPressed() {
        Intent intent = new Intent();
        intent.putExtra("data_return", "Hello FirstActivity, via Back Pressed.");
        setResult(RESULT_OK, intent);
        super.onBackPressed();
    }
}