import os
import configparser


class ConfigValue:
    def __init__(self):
        self.current_path = os.path.dirname(__file__)
        self.conf_path = os.path.join(self.current_path, '../conf/config.ini')
        self.conf = configparser.ConfigParser()
        self.conf_data = self.conf.read(self.conf_path, encoding='utf-8')

    @property
    def grant_type(self):
        return self.conf.get("default", "grant_type")

    @property
    def appid(self):
        return self.conf.get("default", "appid")

    @property
    def secret(self):
        return self.conf.get("default", "secret")

    @property
    def hosts(self):
        return self.conf.get("default", "hosts")

    @property
    def report_path(self):
        return self.conf.get("default", "report_path")
    @property
    def case_path(self):
        return self.conf.get("default", "case_path")

config = ConfigValue()

if __name__ == '__main__':
    secret = config.secret
    print(secret)
