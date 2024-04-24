import os
import numpy as np
from ultralytics import YOLO

model = YOLO("runs/detect/train5/weights/best.pt")  # build a new model from scratch
from ultralytics import YOLO

# Load a model
# model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model(['/Users/admin/Desktop/solar_panel/train/images/Drone_Solar_Sample2_mp4-59_jpg.rf.1c5a88973d1142781a704220d11b753e.jpg'])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename='result.jpg')  # save to disk