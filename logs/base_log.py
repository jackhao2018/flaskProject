import logging
import datetime
import configparser
from config.base_config import BASE_DIR


class MyLog:

    sh_format = '%(levelname)s %(filename)s %(funcName)s no.%(lineno)d: %(message)s'
    fh_format = '%(levelname)s %(asctime)s %(filename)s %(funcName)s no.%(lineno)d: %(message)s'

    def __init__(self):
        log_ini = configparser.ConfigParser()
        log_ini.read(BASE_DIR + "/logs/log.ini")
        self.log_level = log_ini.get('logger_root', 'level')
        self.stream_lever = log_ini.get('handler_streamHandlers', 'level')
        self.file_lever = log_ini.get('handler_fileHandler', 'level')

    def log_config(self, filename):
        # 1.创建一个日志器
        logger = logging.getLogger()
        # 设置日志级别、指定日志信息输出位置
        logger.setLevel(self.log_level)
        sh = logging.StreamHandler()

        # 把日志信息放到控制台
        logger.addHandler(sh)

        sh_formator = logging.Formatter(self.sh_format)
        fh_formator = logging.Formatter(self.fh_format)

        # 优化控制台格式
        sh.setFormatter(sh_formator)
        sh.setLevel(self.stream_lever)

        # 创建文本处理器，指定日志信息文本处理
        fh = logging.FileHandler(BASE_DIR + '/logs/log_files/{}'.format(filename), 'a', 'utf-8')

        # 日志信息输出到文本处理器，及对应的配置属性、文本处理器设置格式、级别
        logger.addHandler(fh)
        fh.setFormatter(fh_formator)
        fh.setLevel(self.file_lever)

        return logger


currenttime = datetime.datetime.now().strftime("%Y-%m-%d")
logfilename = currenttime + '.log'

log = MyLog().log_config(logfilename)
