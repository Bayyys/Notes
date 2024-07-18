package com.example.lbs;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.baidu.location.BDLocation;
import com.baidu.location.BDLocationListener;
import com.baidu.location.LocationClient;
import com.baidu.location.LocationClientOption;
import com.baidu.mapapi.SDKInitializer;
import com.baidu.mapapi.map.MapView;

import java.util.ArrayList;
import java.util.List;

public class SimpleLocation extends AppCompatActivity {
  private static final String TAG = "MYLOG";
  public LocationClient mLocationClient;
  private TextView et_location;
  private MapView map;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    SDKInitializer.setAgreePrivacy(this, false);
    LocationClient.setAgreePrivacy(true);
    EdgeToEdge.enable(this);
    SDKInitializer.initialize(this);
    setContentView(R.layout.simple_location_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    try {
      mLocationClient = new LocationClient(getApplicationContext());
      mLocationClient.registerLocationListener(new MyLocationListener());
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
    et_location = findViewById(R.id.tv_position);
    map = findViewById(R.id.map);
    List<String> permissionList = new ArrayList<>();
    if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) != android.content.pm.PackageManager.PERMISSION_GRANTED) {
      permissionList.add(android.Manifest.permission.ACCESS_FINE_LOCATION);
    }
    if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.READ_PHONE_STATE) != android.content.pm.PackageManager.PERMISSION_GRANTED) {
      permissionList.add(android.Manifest.permission.READ_PHONE_STATE);
    }
    if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.WRITE_EXTERNAL_STORAGE) != android.content.pm.PackageManager.PERMISSION_GRANTED) {
      permissionList.add(android.Manifest.permission.WRITE_EXTERNAL_STORAGE);
    }
    if (!permissionList.isEmpty()) {
      String[] permissions = permissionList.toArray(new String[0]);
      requestPermissions(permissions, 1);
    } else {
      requestLocation();  // 请求位置信息
    }
  }

  private void requestLocation() {
    initLocation(5000); // 需要动态更新 (s)
    mLocationClient.start();
  }

  private void initLocation(Integer seconds) {
    LocationClientOption option = new LocationClientOption();
    option.setScanSpan(seconds);  // 设置更新位置信息的间隔
    option.setIsNeedAddress(true);
    mLocationClient.setLocOption(option);
  }

  @Override
  protected void onResume() {
    super.onResume();
    map.onResume();
  }

  @Override
  protected void onPause() {
    super.onPause();
    map.onPause();
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    mLocationClient.stop();
    map.onDestroy();
  }

  @Override
  public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    switch (requestCode) {
      case 1:
        if (grantResults.length > 0) {
          for (int result : grantResults) {
            if (result != android.content.pm.PackageManager.PERMISSION_GRANTED) {
              throw new RuntimeException("You must grant all permissions");
            }
          }
          requestLocation();
        } else {
          throw new RuntimeException("You must grant all permissions");
        }
      default:
        break;
    }
  }

  // 定位监听器: 获取到位置信息后的处理
  public class MyLocationListener implements BDLocationListener {

    @Override
    public void onReceiveLocation(BDLocation bdLocation) {
      Log.d(TAG, "onReceiveLocation: onReceiveLocation");
      StringBuilder currentPosition = new StringBuilder();
      currentPosition.append("纬度: ").append(bdLocation.getLatitude()).append("\n");
      currentPosition.append("经度: ").append(bdLocation.getLongitude()).append("\n");
      currentPosition.append("国家: ").append(bdLocation.getCountry()).append("\n");
      currentPosition.append("省: ").append(bdLocation.getProvince()).append("\n");
      currentPosition.append("市: ").append(bdLocation.getCity()).append("\n");
      currentPosition.append("区: ").append(bdLocation.getDistrict()).append("\n");
      currentPosition.append("街道: ").append(bdLocation.getStreet()).append("\n");
      currentPosition.append("定位方式: ");
      if (bdLocation.getLocType() == BDLocation.TypeGpsLocation) {
        currentPosition.append("GPS");
      } else if (bdLocation.getLocType() == BDLocation.TypeNetWorkLocation) {
        currentPosition.append("网络");
      }
      Log.d(TAG, "onReceiveLocation: cur" + currentPosition);
      et_location.setText(currentPosition);
    }
  }
}