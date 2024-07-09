package com.bayyy.web;

import android.os.Bundle;
import android.util.Log;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.web.controller.MyParseSAXHandler;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import org.json.JSONArray;
import org.json.JSONObject;
import org.xml.sax.ContentHandler;
import org.xml.sax.XMLReader;
import org.xmlpull.v1.XmlPullParser;
import org.xmlpull.v1.XmlPullParserFactory;

import java.io.StringReader;
import java.util.List;

import javax.xml.parsers.SAXParserFactory;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class ParseUse extends AppCompatActivity {

  enum Parse_Type {
    PULL, SAX, JSON_OBJECT, GSON
  }

  private static final String TAG = "MyLog";

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
    findViewById(R.id.xml_pull).setOnClickListener(v -> getXMLData(Parse_Type.PULL));
    findViewById(R.id.xml_sax).setOnClickListener(v -> getXMLData(Parse_Type.SAX));
    findViewById(R.id.xml_json_object).setOnClickListener(v -> getXMLData(Parse_Type.JSON_OBJECT));
    findViewById(R.id.xml_gson).setOnClickListener(v -> getXMLData(Parse_Type.GSON));
  }

  private void getXMLData(Parse_Type type) {
    new Thread(() -> {
      try {
        OkHttpClient client = new OkHttpClient();
        Request req;
        switch (type) {
          case PULL:
          case SAX:
            req = new Request.Builder().url("http://10.0.2.2:5500/test.xml").build();
            break;
          case JSON_OBJECT:
          case GSON:
            req = new Request.Builder().url("http://10.0.2.2:5500/test.json").build();
            break;
          default:
            return;
        }
        Response res = client.newCall(req).execute();
        String data = res.body().string();
        switch (type) {
          case PULL:
            parseXMLWithPull(data);
            break;
          case SAX:
            parseXMLWithSAX(data);
            break;
          case JSON_OBJECT:
            parseJSONWithJSONObject(data);
            break;
          case GSON:
            parseJSONWithGSON(data);
          default:
            break;
        }
        parseXMLWithPull(data);
      } catch (Exception e) {
        e.printStackTrace();
      }
    }).start();
  }

  private void parseJSONWithGSON(String data) {
    Gson gson = new Gson();
    List<Person> people = gson.fromJson(data, new TypeToken<List<Person>>() {
    }.getType());
    for (Person p : people) {
      Log.d(TAG, "parseJSONWithGSON: id = " + p.getId());
      Log.d(TAG, "parseJSONWithGSON: name = " + p.getName());
      Log.d(TAG, "parseJSONWithGSON: age = " + p.getAge());
    }
  }

  private void parseJSONWithJSONObject(String data) {
    try {
      JSONArray jsonArray = new JSONArray(data);
      for (int i = 0; i < jsonArray.length(); i++) {
        JSONObject jsonObject = jsonArray.getJSONObject(i);
        String id = jsonObject.getString("id");
        String name = jsonObject.getString("name");
        String age = jsonObject.getString("age");
        Log.d(TAG, "parseJSONWithJSONObject: id = " + id);
        Log.d(TAG, "parseJSONWithJSONObject: name = " + name);
        Log.d(TAG, "parseJSONWithJSONObject: age = " + age);
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  private void parseXMLWithSAX(String data) {
    try {
      SAXParserFactory factory = SAXParserFactory.newInstance();
      XMLReader xmlReader = factory.newSAXParser().getXMLReader();
      ContentHandler handler = new MyParseSAXHandler();
      // 将ContentHandler的实例设置到XMLReader中
      xmlReader.setContentHandler(handler);
      // 开始执行解析
      xmlReader.parse(new org.xml.sax.InputSource(new StringReader(data)));
    } catch (Exception e) {
      e.printStackTrace();
    }
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
              Log.d(TAG, "parseXMLWithPull: id = " + id);
              Log.d(TAG, "parseXMLWithPull: name = " + name);
              Log.d(TAG, "parseXMLWithPull: age = " + age);
            }
            break;
          }
          default:
            break;
        }
        eventType = xmlPullParser.next();
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}