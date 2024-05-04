import cv2
import os

folder_name = "/Users/admin/Desktop/solar/solar_panel/gray/vietHuong"
folder_save = "/Users/admin/Desktop/solar/solar_panel/gray/vietHuong_gray"

for filename in os.listdir(folder_name):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        file_path = os.path.join(folder_name, filename)
        image = cv2.imread(file_path)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray_file_path = os.path.join(folder_save, filename)

        cv2.imwrite(gray_file_path, gray_image)
