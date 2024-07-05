package com.bayyy.web;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import org.xmlpull.v1.XmlPullParser;
import org.xmlpull.v1.XmlPullParserFactory;

import java.io.StringReader;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class ParseUse extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.parse_use_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    findViewById(R.id.xml_pull).setOnClickListener(v -> getXMLData());
  }

  private void getXMLData() {
    new Thread(() -> {
      try {
        OkHttpClient client = new OkHttpClient();
        Request req = new Request.Builder().url("http://127.0.0.1:5500/test.xml").build();
        Response res = client.newCall(req).execute();
        String data = res.body().string();
        parseXMLWithPull(data);
      } catch (Exception e) {
        e.printStackTrace();
      }
    }).start();
  }

  private void parseXMLWithPull(String xmlData) {
    try {
      XmlPullParserFactory factory = XmlPullParserFactory.newInstance();
      XmlPullParser xmlPullParser = factory.newPullParser();
      xmlPullParser.setInput(new StringReader(xmlData));
      int eventType = xmlPullParser.getEventType();
      String id = "";
      String name = "";
      String age = "";
      while (eventType != XmlPullParser.END_DOCUMENT) {
        String nodeName = xmlPullParser.getName();
        switch (eventType) {
          // 开始解析某个节点
          case XmlPullParser.START_TAG: {
            if ("id".equals(nodeName)) {
              id = xmlPullParser.nextText();
            } else if ("name".equals(nodeName)) {
              name = xmlPullParser.nextText();
            } else if ("age".equals(nodeName)) {
              age = xmlPullParser.nextText();
            }
            break;
          }
          // 完成解析某个节点
          case XmlPullParser.END_TAG: {
            if ("person".equals(nodeName)) {
              System.out.println("id is " + id);
              System.out.println("name is " + name);
              System.out.println("age is " + age);
            }
            break;
          }
          default:
            break;
        }
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}