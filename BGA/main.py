import configparser
import sys
import pymongo

# Parse INI file for settings

def get_db():
    config = configparser.ConfigParser()
    config.read('../settings.ini')
    return config['database']['db_connection_string']


def main():
    MONGODB_URI = get_db()
    pass

if __name__ == '__main__':
    print("Running BGA")
    main()