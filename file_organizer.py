import os         # import is a keyword used to bring a moduale 
import shutil

# Current folder
SOURCE_FOLDER = os.getcwd() # The folder where the script is located

# File categories
FILE_TYPES = { #FILE_TYPE is a dictionary that categorizes file extensions into different types of files
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".md"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Python_Files": [".py"],
    "Scripts": [".js", ".sh", ".bat"],
}

# Create folders
for folder_name in FILE_TYPES:
    folder_path = os.path.join(SOURCE_FOLDER, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Create Others folder
others_folder = os.path.join(SOURCE_FOLDER, "Others")
os.makedirs(others_folder, exist_ok=True)

# Organize files
for file_name in os.listdir(SOURCE_FOLDER):

    file_path = os.path.join(SOURCE_FOLDER, file_name)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get extension
    extension = os.path.splitext(file_name)[1].lower()

    moved = False

    # Check categories
    for folder_name, extensions in FILE_TYPES.items():

        if extension in extensions:# 

            destination = os.path.join(
                SOURCE_FOLDER,
                folder_name,
                file_name
            )

            # Avoid duplicate names
            if not os.path.exists(destination):
                shutil.move(file_path, destination)
                print(f"✅ {file_name} → {folder_name}")

            moved = True
            break

    # Move unknown files to Others

    if not moved:
        destination = os.path.join(
            SOURCE_FOLDER,
            "Others",
            file_name
        )

        if not os.path.exists(destination):
            shutil.move(file_path, destination)
            print(f"📁 {file_name} → Others")

print("\n🎉 File organization completed successfully!")