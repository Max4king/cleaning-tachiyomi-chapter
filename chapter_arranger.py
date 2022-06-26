import os, os.path
import shutil

def main():
    # Name of the folder
    folder_path = ("Wataten")
    
    images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for image in images:
        image_name_only = image.split(".")[0]
        image_name_only = str(image_name_only).split("_")[1:]
        folder_name = "chapter " + str(image_name_only[0])
        new_path = os.path.join(folder_path, folder_name)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        old_img_path = os.path.join(folder_path, image)            
        new_img_path = os.path.join(new_path, image)
        shutil.move(old_img_path, new_img_path)
    return True

while True:
    checker = main()
    if checker:
        break
