
import unittest
#导入HTMLtestrunner 文件名与类一致

from HTMLTestRunner import HTMLTestRunner

#定义一个测试报告文件

report_file = "test_repoet.html"

 #生成一个套件对象
 # suite 使用 unittest 调用 testloadr 然后调用discover "."为当前路径 匹配模式
suite = unittest.TestLoader().discover('.',pattern = 'demo*.py')

#生成一个runner运行器 with 打开一个report_file文件 用二进制写一个对象f
with open(report_file,'wb')as f:
    #对象  名字  详细描述
    runner=HTMLTestRunner(f,title="baogao",description='v1.2')
    runner.run(suite)
