"""
with:操作完成后自动关闭文件对象
    作业：
        从终端一个文件名称，可以包含路径：
        将这个文件复制到家目录下
        注意：可能是文本文件，可能是二进制文件

"""
import os

file_name = input("请输入一个文件名：")
file2=file_name.split("/")[-1]
new_file="/home/tarena/"+file2
try:
    fr = open(new_file, "rb")
except Exception as e:
    print(e)
else:
    fw = open("/home/tarena/file100", "wb")
    while True:
        data=fr.readline()
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

# if not os.path.exists(file_name):
#     print("不存在")


