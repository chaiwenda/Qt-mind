# date:2018/8/25 21:00
# -*- coding: utf-8 -*-
#author;cwd
"""
function:读写文件
"""
class write_file:
    def __init__(self, msg, file_path):
        self.msg = msg
        self.path = file_path
    def writeMsg(self):
        with open(self.file_path, 'w') as f:
            f.write(self.msg)
            f.close()