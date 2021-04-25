from loguru import logger


#输出日志到文件
#logger.add('文件名',格式化,级别)
#示例代码
logger.add("a.log",format = "{time}{level}{message}",level="DEBUG")
logger.debug('这是一条debug文件')
logger.info('这是一条info文件')

#时间格式化
#logger.add("a.log",format = "{time：YYYY-MM-DD at HH:mm:ss} | {level} | {message}"

#字符串格式化
#logger.info("If you're using Python {},prefer{feature} of course!",3.6,feature="f-strings")
#方法一logger.info("hellow {},hellow{}".format("python","java"))
#方法二
logger.info("hellow {},hellow{}","python","java")
#文件保存
logger.add("file_1.log",rotation="500 MB")  #文件达到500MB新生成一个文件

