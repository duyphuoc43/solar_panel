from ultralytics import YOLO

import cv2
model = YOLO("yolov8n.pt")
while (1):
    link = 0
    results = model.predict(source=link,show=True)
    print(results)