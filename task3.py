import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist!")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files_moved = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            src_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename}")
            files_moved += 1

    print(f"\nTask Complete! Total {files_moved} .jpg files moved to '{destination_folder}'.")

if __name__ == "__main__":
    # Apana ehi path ku nijara folder anusare badalai paribe
    source = "./source_folder"
    destination = "./destination_folder"
    
    # Demonstration pain source folder baneiba
    if not os.path.exists(source):
        os.makedirs(source)
        with open(os.path.join(source, "test_image.jpg"), "w") as f:
            f.write("dummy image content")

    move_jpg_files(source, destination)