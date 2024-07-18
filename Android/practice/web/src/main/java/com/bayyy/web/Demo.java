package com.bayyy.web;


import com.meituan.service.inf.kms.client.Kms;
import com.meituan.service.inf.kms.utils.KmsResultNullException;

public class Demo {
  public static void test(String[] args) {
    String appkey = "com.sankuai.mda.skr";
    String accessKey = getByName(appkey, "s3plus_service_access_key");
    String secretKey = getByName(appkey, "s3plus_service_secret_key");
    System.out.println("accessKey: " + accessKey);
    System.out.println("secretKey: " + secretKey);
  }

  private static String getByName(String appkey, String name) {
    String value = null;
    try {
      value = Kms.getByName(appkey, name);
    } catch (KmsResultNullException e) {
      throw new RuntimeException(e);
    }
    return value;
  }
}
