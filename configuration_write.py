import configparser;
config = configparser.ConfigParser();
config['default'] = {"ServerAliveInterval":45,"Compression":"Yes","CompressionLevel":9,"ForwardX11":"yes"};
config['database'] = {"username":"test","dbname":"hello","host":"127.0.0.1","password":"@!@ss","port":"80"};



with open('example.ini', 'w+') as configfile:
   config.write(configfile)
   
sections = config.sections();

print(sections);

status  = "default" in config;

print(status);

for key in config:
	print(key);
	print(config[key])
	for inner in config[key]:
		print(inner);
		
print(config.get("database","Compression"))		
database = config['database'];
print(database.get("Compression"))