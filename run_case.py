import unittest
from demoa import TestDemoAdd

 #生成一个套件对象
 # suite 使用 unittest 调用 testloadr 然后调用discover "."为当前路径 匹配模式
# 1 suite = unittest.TestLoader().discover(star_dir= '.',pattern = 'demo*.py')

#2  一个个加与textloader一样
suite = unittest.TestSuite()
suite.addTest(TestDemoAdd('test_add01'))
suite.addTest(TestDemoAdd('test_add02'))
suite.addTest(TestDemoAdd('test_add03'))

#按照这种环境添加
runner = unittest.TextTestRunner()
#利用runner运行suite套件
runner.run(suite)