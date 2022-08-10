import os
# from config.loadyamldata import loadyaml

current = os.path.abspath(__file__)

BASE_DIR = os.path.dirname(os.path.dirname(current))

_config_path = BASE_DIR + os.sep + 'config'

_log_path = BASE_DIR + os.sep + 'logs'

def get_config_path():
    return _config_path

def get_config_file():
    return _config_path

def get_log_path():
    """
    获取Log文件路径
    :return:
    """
    return _log_path

class ConfigYaml:

    # 初始yaml读取配置文件
    def __init__(self):
        self.config = loadyaml(get_config_file())

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        """
        获取日志级别
        :return:
        """
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """
        获取文件扩展名
        :return:
        """
        return self.config["BASE"]["log_extension"]

    def get_email_info(self):
        """
        获取邮件配置相关信息
        :return:
        """
        return self.config["email"]


if __name__ == '__main__':
    print(BASE_DIR)
