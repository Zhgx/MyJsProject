#coding=UTF-8
import unittest
import timelist as TL


class PTest(unittest.TestCase):
#打开读取文件
    def setUp(self): 
        self.timelist=TL.timeList() 
        with open('timedata.txt','r')as self.f:
            lines=self.f.readlines()
            self.last_line=lines[-1]   
    # 关闭文件  
    def tearDown(self):
        self.f.close()
    #测试用例
    def test_write(self):
        # print(self.last_line)
        self.assertEqual("2020.05.26\n",self.last_line)
    
if __name__ == '__main__':
    #构建测试集合
    suite=unittest.TestSuite()
    #将测试用例加到测试集
    suite.addTest(PTest('test_write'))
    #运行整个测试集
    unittest.TextTestRunner(verbosity=2).run(suite)


