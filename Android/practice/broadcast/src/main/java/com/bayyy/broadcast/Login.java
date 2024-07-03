package com.bayyy.broadcast;

import android.content.Intent;
import android.os.Bundle;
import android.os.PersistableBundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.broadcast.controller.BaseActivity;

public class Login extends BaseActivity {
  private EditText accountEdit;
  private EditText passwordEdit;
  private Button login;

  @Override
  public void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.login_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    accountEdit = (EditText) findViewById(R.id.account);
    passwordEdit = (EditText) findViewById(R.id.password);
    login = (Button) findViewById(R.id.login);
    login.setOnClickListener(v -> {
      String account = accountEdit.getText().toString();
      String password = passwordEdit.getText().toString();
      if (account.equals("admin") && password.equals("123456")) {
        Intent intent = new Intent(Login.this, LoginSuccess.class);
        startActivity(intent);
        finish();
      } else {
        Toast.makeText(Login.this, "account or password is invalid", Toast.LENGTH_SHORT).show();
      }
    });
  }
}