import logging

#创建logger 对象
logger = logging.getLogger()
#创建文件操作符
fh = logging.FileHandler('log.log',encoding='utf-8')#创建输出到文件的对象,文件操作符

#设置格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#将文件操作符和格式关联
fh.setLevel(logging.DEBUG)

fh.setFormatter(formatter)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setFormatter(formatter)

logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.debug('满意')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('错误')
logger.critical('logger critical message')