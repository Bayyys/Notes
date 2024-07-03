package com.bayyy.ui.controller;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bayyy.ui.R;
import com.bayyy.ui.pojo.Msg;

import java.util.List;

public class MsgAdapter extends RecyclerView.Adapter<MsgAdapter.ViewHolder> {
  private List<Msg> mMsgList;

  public class ViewHolder extends RecyclerView.ViewHolder {
    LinearLayout leftLayout;
    LinearLayout rightLayout;

    TextView leftMsg;
    TextView rightMsg;

    public ViewHolder(@NonNull View itemView) {
      super(itemView);
      leftLayout = (LinearLayout) itemView.findViewById(R.id.left_layout);
      rightLayout = (LinearLayout) itemView.findViewById(R.id.right_layout);
      leftMsg = (TextView) itemView.findViewById(R.id.left_msg);
      rightMsg = (TextView) itemView.findViewById(R.id.right_msg);
    }
  }

  public MsgAdapter(List<Msg> mMsgList) {
    this.mMsgList = mMsgList;
  }

  @NonNull
  @Override
  public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
    View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.msg_item, parent, false);
    return new ViewHolder(view);
  }

  @Override
  public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
    Msg msg = mMsgList.get(position);
    if (msg.getType() == Msg.TYPE_RECEIVED) {
      holder.leftLayout.setVisibility(View.VISIBLE);
      holder.rightLayout.setVisibility(View.GONE);
      holder.leftMsg.setText(msg.getContent());
    } else if (msg.getType() == Msg.TYPE_SENT) {
      holder.rightLayout.setVisibility(View.VISIBLE);
      holder.leftLayout.setVisibility(View.GONE);
      holder.rightMsg.setText(msg.getContent());
    }
  }

  @Override
  public int getItemCount() {
    return mMsgList.size();
  }

}
