import cv2
import os
import datetime
# 路径
basepath = os.path.dirname(os.path.abspath(__file__))
# 在官网下载人脸识别文件（readme.MD中的第二步） 创建人脸识别器，使用default.xml
face_cascade = cv2.CascadeClassifier(basepath + r'\\opencv\\haarcascade_frontalface_default.xml')

# 打开摄像头
cap = cv2.VideoCapture(0)
#读取摄像头的图像帧
ret, frame = cap.read()

# 将图像帧转换为灰度图像
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 在灰度图像中检测人脸
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 标记检测到的人脸
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 显示带有人脸标记的图像
camera = cv2.imshow('new_picture', frame)
# 将图片存入camera文件夹下
now = datetime.datetime.now()
time_str = now.strftime("%Y_%m_%d_%H_%M_%S")
cv2.imwrite(basepath + f'\\camera\\image_{time_str}.jpg', frame)

# 释放摄像头，关闭窗口
cap.release()
cv2.destroyAllWindows()