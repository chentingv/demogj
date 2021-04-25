#导入  日志的级别
from loguru import logger

#输出日志不同级别
logger.debug('这是一条debug文件')
logger.info('这是一条info文件')
logger.warning('这是一条warning文件')
logger.success('这是一条success文件')
logger.error('这是一条error文件')