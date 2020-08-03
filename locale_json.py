import yaml
import json
from os.path import expanduser

state = 'oklahoma'
key = 'county_codes'
home = expanduser('~')
config_file = home + '/projects/reggie-demo/venv-rd/lib/python3.7/site-packages/reggie-0.1-py3.7.egg/reggie/configs/data/' + state + '.yaml'
json_file =  home + '/projects/reggie-demo/venv-rd/lib/python3.7/site-packages/reggie-0.1-py3.7.egg/reggie/configs/primary_locale_names/' + state + '.json'

with open(config_file) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

data = [{"name": k, "id": str(v)} for k, v in config[key].items()]

with open(json_file, 'w') as j:
    json.dump(data, j, indent=4)
