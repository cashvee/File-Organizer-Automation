import os
import shutil

# Set source and destination folders
source_folder = os.path.expanduser("~/Downloads")  # Downloads folder
destination_folder = os.path.expanduser("~/Desktop/Photos")  # Destination on Desktop

# List of image file extensions
image_extensions = [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"]

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Move image files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    
    if os.path.isfile(file_path) and file.lower().endswith(tuple(image_extensions)):
        shutil.move(file_path, os.path.join(destination_folder, file))
        print(f"Moved {file} to {destination_folder}")

print("✅ Image files moved successfully!")
