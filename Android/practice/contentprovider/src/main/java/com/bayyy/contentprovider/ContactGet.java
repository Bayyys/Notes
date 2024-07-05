package com.bayyy.contentprovider;

import android.Manifest;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.bayyy.contentprovider.controller.ContactAdapter;
import com.bayyy.contentprovider.pojo.MyContact;

import java.util.ArrayList;
import java.util.List;

public class ContactGet extends AppCompatActivity {
  private static final String TAG = "ContactGet";
  ContactAdapter adapter;
  List<MyContact> contactList = new ArrayList<>();
  ListView listView;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.contact_get_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    adapter = new ContactAdapter(this, R.layout.my_contact_layout);
    listView = findViewById(R.id.list_contacts);
    listView.setAdapter(adapter);
    findViewById(R.id.btn_get_contact).setOnClickListener(v -> {
      checkPermissionAndGetContacts();
    });
  }

  private void getContact() {
    try (Cursor c = getContentResolver().query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, null, null, null, null)) {
      contactList.clear();
      if (c != null) {
        while (c.moveToNext()) {
          // 获取联系人姓名
          String displayName = c.getString(c.getColumnIndexOrThrow(ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME));
          // 获取联系人手机号
          String number = c.getString(c.getColumnIndexOrThrow(ContactsContract.CommonDataKinds.Phone.NUMBER));
          contactList.add(new MyContact(displayName, number));
        }
        adapter.clear();
        adapter.addAll(contactList);
        if (contactList.size() > 0) {
          Toast.makeText(this, "Get contacts succeed!", Toast.LENGTH_SHORT).show();
          listView.setVisibility(android.view.View.VISIBLE);
          findViewById(R.id.tv_msg).setVisibility(android.view.View.GONE);
        } else {
          Toast.makeText(this, "No contacts!", Toast.LENGTH_SHORT).show();
          listView.setVisibility(android.view.View.GONE);
          findViewById(R.id.tv_msg).setVisibility(android.view.View.VISIBLE);
        }
      }
    } catch (Exception e) {
      e.printStackTrace();
    }

  }

  private void checkPermissionAndGetContacts() {
    if (ContextCompat.checkSelfPermission(this, Manifest.permission.READ_CONTACTS) != PackageManager.PERMISSION_GRANTED) {
      // 未授权，请求权限
      ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.READ_CONTACTS}, 1);
    } else {
      // 已授权，获取联系人
      getContact();
    }
  }

  @Override
  public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
    switch (requestCode) {
      case 1:
        if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
          getContact();
        } else {
          Toast.makeText(this, "You denied the permission", Toast.LENGTH_SHORT).show();
        }
        break;
      default:
        break;
    }
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
  }
}