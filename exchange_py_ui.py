import os
import os.path

# -*- coding: utf-8 -*-

dir = "./UI"


class changeUI():
    def __init__(self, path):
        self.path = path
        self.lists = []

    def listUIFile(self):
        files = os.listdir(self.path)
        for filename in files:
            self.lists.append(filename)
        return self.lists

    def refname(self, filename):
        return os.path.splitext(filename)[0] + ".py"

    def change(self):
        self.listUIFile()
        for uifile in self.lists:
            pyfile = self.refname(uifile)
            uifile = os.path.join(self.path, uifile)
            pyfile = os.path.join(self.path, pyfile)
            if os.path.exists(pyfile):
                continue
            cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile, uifile=uifile)
            os.system(cmd)


# main（）
if __name__ == "__main__":
    changefile = changeUI(dir)
    changefile.change()
