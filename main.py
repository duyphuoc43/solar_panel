import os
import numpy as np
from ultralytics import YOLO


# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
results = model.train(data="/Users/admin/Desktop/solar_panel/data.yaml", epochs=200 , batch = 16)  # train the model