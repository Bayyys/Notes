# 介绍

本部分旨在为肩肱节律及肩峰撞击综合征传感器上位机提供参考

# 项目结构

```
|-- sensors.py
|-- data
|-- threads
|   |-- readThread.py
|   |-- saveThread.py
|   |-- updateThread.py
|   |-- updateCanvasThread.py
|-- ui
|   |-- canvas_ui
|   |   |-- canvas_ui.ui
|   |   |-- canvas_ui.py
|   |   |-- Canvas.py
|   |-- sensor_info_list_ui
|   |   |-- SensorInfoList_ui.ui
|   |   |-- SensorInfoList_ui.py
|   |   |-- SensorInfoList.py
|   |   |-- sensor_single_info_list_ui
|   |   |   |-- SensorSingleInfoList_ui.ui
|   |   |   |-- SensorSingleInfoList_ui.py
|   |-- sensor_info_ui
|   |   |-- SensorInfo_ui.ui
|   |   |-- SensorInfo_ui.py
|   |   |-- SensorInfo.py
|   |   |-- sensor_single_info_ui
|   |   |   |-- SensorSingleInfo.py
|   |-- sensor_print_ui
|   |   |-- SensorPrint.py
|   |-- setting_ui
|       |-- setting_ui.ui
|       |-- setting_ui.py
|-- utils
    |-- setting_ui.ui
    |-- setting_ui.py
```

# 项目依赖

```
PyQt5
...
```

# 项目运行

```
python3 main.py
```

# 项目进度

[Change Log](./CHANGELOG.md)