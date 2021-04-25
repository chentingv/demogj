import  unittest
#导入参数化的包
from parameterized import parameterized

def add(x,y):
    z=x+y
    return z


class TestDemoAdd(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("================执行setupclass方法=================")
    #
    #
    #
    # def setUp(self)->None:
    #      print("================执行setup方法=================")
    #
    # def tearDown(self) -> None:
    #      print("================执行testdown方法=================")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #      print("================执行teardownclass方法=================")

    #1 @parameterized.expand([(7,3,4),(4,0,4),(1,-3,4)])

    date = [(7, 3, 4), (4, 0, 4), (1, -3, 4)]
    @parameterized.expand(date)
    def test_add(self,c,a,b):
        res = add(a,b)
        self.assertEqual(c,res)
"""
    def test_add01(self):
        print("==============执行test01方法=================")
        res1 = add(3,4)
        self.assertEqual(7,res1)

    def test_add02(self):
        print("==============执行test02方法=================")
        res2 = add(2, 4)
        self.assertEqual(6,res2)

    def test_add03(self):
        print("==============执行test03方法=================")
        res3 = add(3,-1)
        self.assertEqual(2,res3)
"""
#main方法让他从这来执行
if __name__ == '__main__':
#     #创建对象
     suite = unittest.TestSuite()
#     #添加一条测试用例  方法用引号引起来
     suite.addTest(TestDemoAdd('test_add01'))
#     #通过texttestrunner（类） 生成一个运行器（对象）
     runner = unittest.TextTestRunner()
#     #runner 调用run（方法） 运行测试用例
     runner.run(suite)
    #unittest.main()  #调用取值与main函数   直接调用main方法