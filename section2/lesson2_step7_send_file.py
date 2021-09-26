import os

current_dir = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(current_dir, "file.txt")

print(file_path)
print("-------------------------")

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print("-------------------------")

esp_path = os.path.join(current_dir, "../esp/author.txt")

print(esp_path)
