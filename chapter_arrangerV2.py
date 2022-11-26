import re,os, os.path
import shutil

def main():
    # Name of the folder
    
    folder_path = ("Chapter")
    #folder_path = input("Manga folder name: ")
    
    images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    i = 1
    num = 0
    new_images = []
    for img in images:
        new_images.append((img.split(".")[0]))
    new_images = sorted(new_images, key=lambda s: int(re.search(r'\d+', s).group()))
    
    for image in new_images:
        image_name_only = image.split(" ")[0]
        #image_name_only = str(image_name_only).split("_")[1:]
        #folder_name = "chapter " + str(image_name_only[0])
        prom = (re.search(r'_', image))
        if prom == None:
            i = i + 1
        folder_name = "chapter " + str(i-1)
        new_path = os.path.join(folder_path, folder_name)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        image_jpg = str(image) + ".jpg"
        print(image_jpg)
        old_img_path = os.path.join(folder_path, image_jpg)
        print(old_img_path)
        new_img_path = os.path.join(new_path, image_jpg)
        print(new_img_path)
        shutil.move(old_img_path, new_img_path)
        print("i: ",i,"n: ",num)
        num = num + 1
        
    return True

while True:
    checker = main()
    if checker:
        break