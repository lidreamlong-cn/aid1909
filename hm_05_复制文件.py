file_read = open("dict.txt")
file_write = open("readme2", "w")

# 2. 读、写
text = file_read.read()
file_write.write(text)

# 3. 关闭
file_read.close()
file_write.close()
