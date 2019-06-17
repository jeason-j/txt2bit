# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:26:19 2019
Function: text文件转成bin类型文件
@author: Admin
"""
import time
import struct

# 读取text文件和长度
file_txt = open('txt2bin_test.txt', 'r')
txt_read = file_txt.read()
file_txt_size = len(txt_read)
print(file_txt_size)

count = 0
# 写入bin文件
with open('hexbin_test.bin', 'wb') as fp:
    # 判断文件长度
    while count < file_txt_size:
        # 截取 8bit 数据 [count:count+8]
        txt_read_string = txt_read[count:count+8]
        # print(txt_read_string) # 00000001
        # 二进制类型 字符串 00000001 ，转十进制类型 int数据 1
        txt_read_int = int(txt_read_string, 2)
        # print(txt_read_int) # 1
        # 十进制类型 int数据 1 ，转16进制类型b'\x01'
        txt_read_bin = struct.pack('B' ,txt_read_int)
        # print(txt_read_bin) # b'\x01'
        # 写入bin文件
        fp.write(txt_read_bin)
        # 文件累加长度
        count += 8
        # 测试用延时 1s
        # time.sleep( 1 )    
print('执行完毕')

