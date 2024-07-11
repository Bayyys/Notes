package com.bayyy.services.basic;

public interface DownloadListener {
  void onProgress(int progress);

  void onSuccess();

  void onFailed();

  void onPaused();

  void onCanceled();
}
