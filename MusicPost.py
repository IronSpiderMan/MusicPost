from PIL import Image, ImageDraw

left = 273
top = 573
radius = 533
circle_size = (radius, radius)

def generate_circle_image(img_path):
    # 创建一个透明的正方形
    im = Image.new('RGBA', circle_size, (255, 255, 255, 0))
    # 获取绘画者
    drawer = ImageDraw.Draw(im)
    # 在透明的正方形上画一个黄色的圆
    drawer.ellipse((0, 0, circle_size[0], circle_size[1]), fill=(255, 255, 0), width=0)

    # 打开要转换成圆形的图片，我们事先把图片裁剪好
    pic = Image.open(img_path).convert('RGBA')
    re_pic = pic.resize(circle_size, Image.ANTIALIAS)

    # 遍历图片的每个像素
    for i in range(circle_size[0]):
        for j in range(circle_size[1]):
            r, g, b, a = im.getpixel((i, j))
            if (r, g, b) != (255, 255, 0):
                re_pic.putpixel((i, j), (255, 255, 255, 0))

    return re_pic

def generate_music_post(circle_im, bg_im):
    bg_copy = bg_im.copy()
    bg_copy.paste(circle_im, (left, top))
    for i in range(left, left+radius):
        for j in range(top, top+radius):
            color = bg_copy.getpixel((i, j))
            if color[3] == 0:
                bg_copy.putpixel((i, j), bg_im.getpixel((i, j)))

    return bg_copy

pic = generate_circle_image('girl.jpeg')
bg_im = Image.open('music.jpg').convert('RGBA')
music_post = generate_music_post(pic, bg_im)
music_post.show()