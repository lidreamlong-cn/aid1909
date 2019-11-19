# 1. 打开文件，rb二进制方式打开读写方式都是字节串
#所有文件都可以用二进制方式读写
#二进制文件不可用文本方式开读
file = open("../day01/file1")
print(file)
# 2. 读取文件内容
text = file.read()
print(text)

# 3. 关闭文件
file.close()
