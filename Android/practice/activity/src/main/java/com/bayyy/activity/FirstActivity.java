package com.bayyy.activity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContract;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.bayyy.start.R;

import java.net.URL;

public class FirstActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.first_layout);
        // btn_1: 弹出 Toast (You clicked Button 1)
        Button btn_1 = (Button) findViewById(R.id.btn_1);
        btn_1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(FirstActivity.this, "You clicked Button 1", Toast.LENGTH_SHORT).show();
            }
        });
        // btn_2: 退出程序
        Button btn_2 = (Button) findViewById(R.id.btn_2);
        btn_2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
        // btn_3: 跳转到 SecondActivity
        findViewById(R.id.btn_3).setOnClickListener(View -> {
            // 显式方法跳转到 SecondActivity
//                    Intent intent = new Intent(FirstActivity.this, SecondActivity.class);
            // 隐式方法跳转到 SecondActivity
            Intent intent = new Intent("com.bayyy.activity.SECOND_ACTIVITY");
            intent.addCategory("com.bayyy.activity.MY_CATEGORY");
            startActivity(intent);
        });
        // btn_4: 跳转到百度
        findViewById(R.id.btn_4).setOnClickListener(View -> {
            Intent intent = new Intent(Intent.ACTION_VIEW);
            intent.setData(Uri.parse("http://www.baidu.com"));
            startActivity(intent);
        });
        // btn_5: 发送数据到 ThirdActivity
        findViewById(R.id.btn_5).setOnClickListener(View -> {
            Intent intent = new Intent(FirstActivity.this, ThirdActivity.class);
            intent.putExtra("extra_data", "Hello ThirdActivity");
            startActivity(intent);
        });
        // btn_6: 发送并接受返回数据
        findViewById(R.id.btn_6).setOnClickListener(View -> {
            Intent intent = new Intent(FirstActivity.this, ThirdActivity.class);
            startActivityForResult(intent, 1);
        });
        // btn_7: 使用 registerForActivityResult 进行消息发送+接收
        ActivityResultLauncher<Intent> launcher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(),
                new ActivityResultCallback<ActivityResult>() {
                    @Override
                    public void onActivityResult(ActivityResult result) {
                        if (result.getResultCode() == FirstActivity.RESULT_OK) {
                            Log.d("data_return", result.getData().getStringExtra("data_return"));
                        }
                    }
                });
        findViewById(R.id.btn_7).setOnClickListener(
                View -> {
                    Intent i = new Intent(FirstActivity.this, ThirdActivity.class);
                    launcher.launch(i);
                });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main, menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        if (item.getItemId() == R.id.add_item) {
            Toast.makeText(this, "You clicked Add", Toast.LENGTH_SHORT).show();
        } else if (item.getItemId() == R.id.remove_item) {
            Toast.makeText(this, "You clicked Remove", Toast.LENGTH_SHORT).show();
        } else {
            return false;
        }
        return true;
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 1 && resultCode == RESULT_OK) {
            assert data != null;
            String returnedData = data.getStringExtra("data_return");
            Toast.makeText(this, returnedData, Toast.LENGTH_SHORT).show();
        }
    }
}