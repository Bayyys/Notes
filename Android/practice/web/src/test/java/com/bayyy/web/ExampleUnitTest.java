package com.bayyy.web;

import org.junit.Test;

import static org.junit.Assert.*;

import com.meituan.service.inf.kms.client.Kms;
import com.meituan.service.inf.kms.utils.KmsResultNullException;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
  @Test
  public void addition_isCorrect() {
    assertEquals(4, 2 + 2);
  }

  @Test
  public void kms_test() {
    String appkey = "com.sankuai.mda.skr";
    String secretKey = getByName(appkey, "s3plus_service_secret_key");
    String accessKey = getByName(appkey, "s3plus_service_access_key");
    System.out.println("accessKey: " + accessKey);
    System.out.println("secretKey: " + secretKey);
    assertEquals(4, 2 + 2);
  }

  private String getByName(String appkey, String name) {
    String value = null;
    try {
      value = Kms.getByName(appkey, name);
    } catch (KmsResultNullException e) {
      e.printStackTrace();
    }
    return value;
  }
}