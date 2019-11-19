file = open("day02/dict.txt")
#无限循环，让用户选择退出
# while True:
#     text = file.readline()
#
#     # 判断是否读取到内容
#     if not text:
#         break
#
#     print(text)


#返回值： 返回读取到的内容列表
text = file.readlines(30)
for item in text:
    print(item)

print(text)
file.close()
