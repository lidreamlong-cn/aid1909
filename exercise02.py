"""
with:操作完成后自动关闭文件对象
    作业：
        从终端一个文件名称，可以包含路径：
        将这个文件复制到家目录下
        注意：可能是文本文件，可能是二进制文件

"""
with open("readme2") as f:
    data=f.read()
    print(data)