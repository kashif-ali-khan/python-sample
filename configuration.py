import configparser;
config = configparser.ConfigParser();
config['default'] = {"ServerAliveInterval":45,"Compression":"Yes","CompressionLevel":9,"ForwardX11":"yes"};

with open('example.ini', 'w') as configfile:
   config.write(configfile)
