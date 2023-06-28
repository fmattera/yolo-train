from PIL import Image
import os

def resize_images(folder_path, target_size):
    # Get the list of files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over each file
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is an image
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                # Open the image file
                image = Image.open(file_path)

                # Resize the image
                resized_image = image.resize(target_size)

                # Save the resized image, overwriting the original file
                resized_image.save(file_path)
            except Exception as e:
                print(f"Error resizing {file_name}: {str(e)}")


folder_paths = [
r"C:\Users\Shadow\Documents\NeoLocus\11_04_23_backup\yolo-train\test\images",
r"C:\Users\Shadow\Documents\NeoLocus\11_04_23_backup\yolo-train\train\images",
r"C:\Users\Shadow\Documents\NeoLocus\11_04_23_backup\yolo-train\valid\images",


]


for folder_path in folder_paths:
    target_size = (1024, 1024)
    resize_images(folder_path, target_size)
