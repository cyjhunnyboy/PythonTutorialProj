"""
Mac: 无需安装
Linux：无需安装
windows: 勾选了pip和Add python.exe to path


安装三方库，需要知道模块的名字

Pillow: 非常强大的处理图像的工具库
命令：pip install Pillow
更新pip命令：pip install --upgrade pip

"""
# 引入了三方库
from PIL import Image


# 打开图片
img = Image.open("girl.jpg")
# 查看图片信息
print(img.format, img.size, img.mode)

# 设置图片的大小
img.thumbnail((150, 100))
img.save("temp.jpg", "JPEG")
