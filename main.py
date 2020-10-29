import configparser



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    HTTP_8kCutOff = config['httpAddresses']['HTTP_8kCutOff']
    HTTP_4kCutOff = config['httpAddresses']['HTTP_4kCutOff']
    URI_MONGO = config['httpAddresses']['URI_MONGO']