import configparser


from lib import Logger


# 读取配置文件
CONFIG = configparser.RawConfigParser()
CONFIG.read('../config/config.ini')
redis_host = CONFIG.get('redis', 'host')
redis_port = CONFIG.get('redis', 'port')
redis_password = CONFIG.get('redis', 'password')
print(redis_host)
print(redis_port)
print(redis_password)



logger = Logger.Logger()
_logger = logger.getLogger('self.trader_name')
_logger.info("=====取消订单成功=======")