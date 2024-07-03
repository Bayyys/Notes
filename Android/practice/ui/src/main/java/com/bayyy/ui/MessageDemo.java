package com.bayyy.ui;

import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.bayyy.ui.controller.MsgAdapter;
import com.bayyy.ui.pojo.Fruit;
import com.bayyy.ui.pojo.Msg;

import java.util.ArrayList;
import java.util.List;

public class MessageDemo extends AppCompatActivity {
  private List<Msg> msgList = new ArrayList<>();

  private EditText inputText;

  private Button send;

  private RecyclerView msgRecyclerView;

  private MsgAdapter adapter;


  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.message_demo_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    initMsgs();
    // 输出 msgList
    inputText = (EditText) findViewById(R.id.input_text);
    send = (Button) findViewById(R.id.send);
    msgRecyclerView = (RecyclerView) findViewById(R.id.msg_recycler_view);
    msgRecyclerView.setLayoutManager(new LinearLayoutManager(this));
    adapter = new MsgAdapter(msgList);
    msgRecyclerView.setAdapter(adapter);
    send.setOnClickListener(v -> {
          String content = inputText.getText().toString();
          if (!"".equals(content)) {
            Msg msg = new Msg(content, Msg.TYPE_SENT);
            msgList.add(msg);
            adapter.notifyItemInserted(msgList.size() - 1);
            msgRecyclerView.scrollToPosition(msgList.size() - 1);
            inputText.setText("");
          }
        }
    );
  }

  private void initMsgs() {
    Msg msg1 = new Msg("Hello guy.", Msg.TYPE_RECEIVED);
    msgList.add(msg1);
    Msg msg2 = new Msg("Hello. Who is that?", Msg.TYPE_SENT);
    msgList.add(msg2);
    Msg msg3 = new Msg("This is Tom. Nice talking to you.", Msg.TYPE_RECEIVED);
    msgList.add(msg3);
  }
}