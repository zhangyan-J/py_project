from PIL import Image
import os


im = Image.open(r"D:\project\py_project\request_test\image_generate\img\身份证正面.jpg")
w,h = im.size
image_row = 2
image_column = 2

names =  os.listdir(r"D:\project\py_project\request_test\image_generate\img")
# 新的画布

new_img = Image.new('RGB',(image_column*w,image_row*h))
for y in range(image_row): #y = 0,1,2,3
    print(y)
    for x in range(image_column):
        o_img = Image.open(r'D:\project\py_project\request_test\image_generate\img/' + names[image_column*y + x])
        new_img.paste(o_img,(x*w,y*h))
new_img.save('new_img1111111111.jpg')