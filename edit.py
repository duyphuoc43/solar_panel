import os

# Đường dẫn đến thư mục chứa các file txt
folder_path = 'mix/test2/test/labels'

# Duyệt qua tất cả các file trong thư mục
for filename in os.listdir(folder_path):
    # Kiểm tra nếu file có đuôi là .txt
    if filename.endswith('.txt'):
        # Xây dựng đường dẫn đầy đủ tới file
        file_path = os.path.join(folder_path, filename)

        # Mở file ban đầu để đọc
        with open(file_path, 'r') as input_file:
            # Đọc nội dung của file
            lines = input_file.readlines()

        # Sửa đổi nội dung của file
        modified_lines = []
        for line in lines:
            modified_line = '0' + line[1:]  # Thay đổi ký tự đầu tiên thành số 0
            modified_lines.append(modified_line)

        # Ghi nội dung đã sửa vào file mới
        with open(file_path, 'w') as output_file:
            output_file.writelines(modified_lines)

print("Sửa đổi đã hoàn thành cho tất cả các file trong thư mục.")
