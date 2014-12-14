from PIL import Image
import re
img = Image.open("oxygen.png")
rgb_img = img.convert('RGB')
li = []
answer = []
i= 0
while i < rgb_img.size[0]:
    r, g, b = rgb_img.getpixel((i,45))
    if r==g and g==b:
        li.append(r)
    i = i+7

result =  "".join(map(chr,li))
print "".join(map(chr,map(int,re.findall("\d+",result))))  
