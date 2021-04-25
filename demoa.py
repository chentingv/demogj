import  unittest

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



    def test_add01(self):
        print("==============执行test01方法=================")
        self.assertEqual(7,add(3,4))

    def test_add02(self):
        print("==============执行test02方法=================")
        self.assertEqual(6,add(3, 4))

    def test_add03(self):
        print("==============执行test03方法=================")
        self.assertEqual(6.2,add(2.2, 4))

#main方法让他从这来执行
if __name__ == '__main__':
#     #创建对象
     suite = unittest.TestSuite()
#     #添加一条测试用例  方法用引号引起来
     suite.addTest(TestDemoAdd('test_add03'))
#     #通过texttestrunner（类） 生成一个运行器（对象）
     runner = unittest.TextTestRunner()
#     #runner 调用run（方法） 运行测试用例
     runner.run(suite)
    #unittest.main()  #调用取值与main函数   直接调用main方法