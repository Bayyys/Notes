package com.bayyy.web;

import android.os.Bundle;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.web.utils.HttpUtil;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import okhttp3.Call;
import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class GetHttp extends AppCompatActivity {
  TextView res_text;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.get_http_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    res_text = findViewById(R.id.res_text);
    findViewById(R.id.get_data).setOnClickListener(v -> {
      sendHttpRequest();
    });
    findViewById(R.id.get_ok).setOnClickListener(v -> {
      sendOkHttp();
    });
  }

  private void updateUI(String data) {
    runOnUiThread(() -> {
      res_text.setText(data);
    });
  }

  private void sendOkHttp() {
    new Thread(new Runnable() {
      @Override
      public void run() {
        try {
          // 发送GET请求
          OkHttpClient client = new OkHttpClient();
          Request req = new Request.Builder().url("https://www.baidu.com").build();
          try (Response res = client.newCall(req).execute()) {
            String data = res.body() != null ? res.body().string() : null;
            updateUI(data);
          }
        } catch (Exception e) {
          e.printStackTrace();
        }

      }
    }).start();

    // 发送POST请求
    RequestBody body = new FormBody.Builder().add("username", "admin").add("password", "123456").build();
    Request req_post = new Request.Builder().url("https://www.baidu.com").post(body).build();

  }

  private void sendHttpRequest() {
    new Thread(new Runnable() {
      @Override
      public void run() {
        // send http request
        HttpURLConnection connection = null;
        BufferedReader reader = null;
        try {
          URL url = new URL("https://www.baidu.com");
          connection = (HttpURLConnection) url.openConnection();
          connection.setRequestMethod("GET");
          connection.setConnectTimeout(8000);
          connection.setReadTimeout(8000);
          InputStream in = connection.getInputStream();
          // read response
          reader = new BufferedReader(new InputStreamReader(in));
          StringBuilder response = new StringBuilder();
          String line;
          while ((line = reader.readLine()) != null) {
            response.append(line);
          }
          // show response
          runOnUiThread(() -> {
            res_text.setText(response.toString());
          });
        } catch (Exception e) {
          e.printStackTrace();
        } finally {
          if (reader != null) {
            try {
              reader.close();
            } catch (IOException e) {
              e.printStackTrace();
            }
          }
          if (connection != null) {
            connection.disconnect();
          }
        }
      }
    }).start();
  }

  private void sendRequest() {
    HttpUtil.sendOkHttpRequest("http://www.baidu.com", new okhttp3.Callback() {

      @Override
      public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
        String data = response.body() != null ? response.body().string() : null;
        updateUI(data);
      }

      @Override
      public void onFailure(@NonNull Call call, @NonNull IOException e) {
        e.printStackTrace();
      }
    });
  }
}