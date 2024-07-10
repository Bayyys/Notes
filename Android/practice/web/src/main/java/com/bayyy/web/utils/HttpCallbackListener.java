package com.bayyy.web.utils;

public interface HttpCallbackListener {
  void onFinish(String response);

  void onError(Exception e);
}
