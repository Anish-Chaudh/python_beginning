import os
# os.rename("file/Dog_image/file.txt","file/Dog_image/6.txt")
files = os.listdir("file/Dog_image")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
    os.rename(f"file/Dog_image/{file}", f"file/Dog_image/{i}.png")
    i += 1