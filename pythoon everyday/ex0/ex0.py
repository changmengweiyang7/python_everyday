from PIL import Image,ImageDraw

def add_num(filepath,num=1):
    img=Image.open(filepath)
    size=img.size
    fontsize=size[1]/4
    ImageDraw.Draw(img).text((3*fontsize,0),str(num),fill="red")
    img.save('anenggai.jpg')
    img.show()

add_num('E:/下载/t图标/aneng.jpg')