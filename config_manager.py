import configparser
from pathlib import Path

class ConfigManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        # 使用默認配置
        self.config['server'] = {'host': '0.0.0.0', 'port': '8000', 'reload': 'True'}
        self.config['development'] = {'debug': 'True'}
    
    def get(self, section, key, fallback=None):
        return self.config.get(section, key, fallback=fallback)
    
    def getint(self, section, key, fallback=0):
        return self.config.getint(section, key, fallback=fallback)
    
    def getboolean(self, section, key, fallback=False):
        return self.config.getboolean(section, key, fallback=fallback)

config = ConfigManager()
