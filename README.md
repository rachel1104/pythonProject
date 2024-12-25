# pythonProject
## 开机启动摄像头、拍照并保存照片到电脑中，可检测打开使用电脑的人员，(以windows系统为例)
### 一. 安装所需包
    1. pip install opencv-python   这个命令会安装基础的OpenCV库，通常包括核心的图像处理功能
    2. pip install opencv-contrib-python  它包含了很多用于图像和视频处理的函数和算法。contrib模块则包含了一些额外的、实验性的或者尚未被完全整合进主库的特性和模块 
### 二.在官网下载人脸识别文件
    官网: https://opencv.org/
    ![img.png](img.png)
    代码第7行中用到 face_cascade = cv2.CascadeClassifier(basepath + r'\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
### 三.编写代码 openCamera.py
    执行代码camera文件夹中显示摄像头截图
### 四.配置电脑开机时自动执行命令
    1.win+R 打开运行对话框
    2.输入    shell:startup 点击确定按钮
    3.在打开的文件夹中新增文件如（aa.bat）
    4.在aa.bat中输入, python py文件路径如下，保存
        @echo off
        python E:\python_project\peopleread\opencamera.py

        或者每隔一段时间截图保存（以下为每600秒截图一次）
        @echo off
        :loop
        python E:\git\python\pythonProject\openCamera.py
        timeout /t 600 /nobreak
        goto loop


