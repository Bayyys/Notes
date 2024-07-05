package com.bayyy.media;

import android.Manifest;
import android.annotation.TargetApi;
import android.content.ContentUris;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.DocumentsContract;
import android.provider.MediaStore;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.core.content.FileProvider;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class CameraUse extends AppCompatActivity {
  public static final int TAKE_PHOTO = 1;
  public static final int CHOOSE_PHOTO = 2;
  public static final int REQUEST_PERMISSION_WRITE_EXTERNAL_STORAGE = 1;
  private ImageView photo;
  private Button btn_take;
  private Button btn_load;
  private Uri imageUri;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    EdgeToEdge.enable(this);
    setContentView(R.layout.camera_use_layout);
    ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
      Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
      v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
      return insets;
    });
    btn_take = (Button) findViewById(R.id.btn_take);
    btn_load = (Button) findViewById(R.id.btn_load);
    photo = (ImageView) findViewById(R.id.img_show);
    btn_take.setOnClickListener(v -> {
      // 1.创建File对象，用于存储拍照后的图片
      // getExternalCacheDir()方法用于获取应用关联缓存目录 (/sdcard/Android/data/包名/cache/)
      File outputImage = new File(getExternalCacheDir(), "output_image.jpg");
      try {
        if (outputImage.exists()) {
          outputImage.delete();
        }
        outputImage.createNewFile();
      } catch (IOException e) {
        e.printStackTrace();
      }
      // 2.将File对象转换成Uri对象
      if (Build.VERSION.SDK_INT >= 24) {
        // 如果Android版本大于等于7.0, 则使用FileProvider获取Uri
        imageUri = FileProvider.getUriForFile(CameraUse.this, "com.bayyy.media.fileprovider", outputImage);
      } else {
        // 否则使用Uri.fromFile()方法获取Uri
        imageUri = Uri.fromFile(outputImage);
      }
      // 3.启动相机程序
      Intent intent = new Intent("android.media.action.IMAGE_CAPTURE");
      // 指定图片的输出地址
      intent.putExtra(MediaStore.EXTRA_OUTPUT, imageUri);
      startActivityForResult(intent, TAKE_PHOTO);
    });
    btn_load.setOnClickListener(v -> {
      // 需要动态申请权限: 读取外部存储器的权限
      if (ContextCompat.checkSelfPermission(CameraUse.this, android.Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
        ActivityCompat.requestPermissions(CameraUse.this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, REQUEST_PERMISSION_WRITE_EXTERNAL_STORAGE);
      } else {
        openAlbum();
      }
    });
  }

  /**
   * 打开相册, 选择图片
   */
  private void openAlbum() {
    Intent intent = new Intent("android.intent.action.GET_CONTENT");
    intent.setType("image/*");
    startActivityForResult(intent, CHOOSE_PHOTO);
  }

  @Override
  public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    switch (requestCode) {
      case REQUEST_PERMISSION_WRITE_EXTERNAL_STORAGE:
        if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
          openAlbum();
        } else {
          // 拒绝权限请求
          Toast.makeText(this, "You denied the permission: Request to visit your album", Toast.LENGTH_SHORT).show();
        }
        break;
      default:
        break;
    }
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    switch (requestCode) {
      case TAKE_PHOTO:
        if (resultCode == RESULT_OK) {
          try {
            Bitmap bitmap = BitmapFactory.decodeStream(getContentResolver().openInputStream(imageUri));
            photo.setImageBitmap(bitmap);
          } catch (FileNotFoundException e) {
            e.printStackTrace();
          }
          // 将拍摄的照片显示出来
          photo.setImageURI(imageUri);
        }
        break;
      case CHOOSE_PHOTO:
        if (resultCode == RESULT_OK) {
          // 判断手机系统版本号
          if (Build.VERSION.SDK_INT >= 19) {
            // 4.4及以上系统使用这个方法处理图片
            photo.setImageURI(data.getData());
//            handleImageOnKitKat(data);
          } else {
            // 4.4以下系统使用这个方法处理图片
            photo.setImageURI(data.getData());
//            handleImageBeforeKitKat(data);
          }
        }
        break;
      default:
        break;
    }
  }

  @TargetApi(19)
  private void handleImageOnKitKat(Intent data) {
    // 1.获取图片的Uri
    String imagePath = null;
    Uri uri = data.getData();
    // 2.判断Uri的Authority是不是DocumentsContract
    if (DocumentsContract.isDocumentUri(this, uri)) {
      // 如果是Document类型的Uri, 则通过Document的Id处理
      String docId = DocumentsContract.getDocumentId(uri);
      if ("com.android.providers.media.documents".equals(uri.getAuthority())) {
        // 判断Uri的Authority是不是MediaProvider
        String id = docId.split(":")[1]; // 解析出数字格式的id
        String selection = MediaStore.Images.Media._ID + "=" + id;
        imagePath = getImagePath(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, selection);
      } else if ("com.android.providers.downloads.documents".equals(uri.getAuthority())) {
        // 判断Uri的Authority是不是DownloadsProvider
        Uri contentUri = ContentUris.withAppendedId(Uri.parse("content://downloads/public_downloads"), Long.valueOf(docId));
        imagePath = getImagePath(contentUri, null);
      }
    } else if ("content".equalsIgnoreCase(uri.getScheme())) {
      // 4.如果是Content类型的Uri, 则使用普通方式处理
      imagePath = getImagePath(uri, null);
    } else if ("file".equalsIgnoreCase(uri.getScheme())) {
      // 5.如果是File类型的Uri, 直接获取图片路径即可
      imagePath = uri.getPath();
    }
    displayImg(imagePath); // 根据图片路径显示图片
  }

  /**
   * 根据图片路径显示图片
   *
   * @param imagePath 图片路径
   */
  private void displayImg(String imagePath) {
    if (imagePath != null) {
      Bitmap bitmap = BitmapFactory.decodeFile(imagePath);
      photo.setImageBitmap(bitmap);
    } else {
      Toast.makeText(this, "Failed to get image", Toast.LENGTH_SHORT).show();
    }
  }

  /**
   * 根据Uri和selection来获取图片的真实路径
   *
   * @param uri       图片的Uri
   * @param selection 查询条件
   * @return 图片的真实路径
   */
  private String getImagePath(Uri uri, String selection) {
    String path = null;
    Cursor cursor = getContentResolver().query(uri, null, selection, null, null);
    if (cursor != null) {
      if (cursor.moveToFirst()) {
        path = cursor.getString(cursor.getColumnIndexOrThrow(MediaStore.Images.Media.DATA));
      }
      cursor.close();
    }
    return path;
  }

  /**
   * 4.4以下系统使用这个方法处理图片
   *
   * @param data Intent
   */
  private void handleImageBeforeKitKat(Intent data) {
    Uri uri = data.getData();
    String imagePath = getImagePath(uri, null);
    displayImg(imagePath);
  }
}