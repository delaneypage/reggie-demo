import os
from os.path import expanduser
import zipfile
import zlib
import numpy as np

def get_sample(state_path, nlines):

    home = expanduser('~')
    state_data_path = home + '/projects/reggie-demo/state-data/' + state_path
    state_samples_path = home + '/projects/reggie-demo/state-samples/' + state_path
    state_samples_zips = home + '/projects/reggie-demo/state-samples/' + 'zips/'

    files = [n for n in os.listdir(state_data_path) \
        if ('.txt' in n.lower() or '.csv' in n.lower())]

    if not os.path.exists(state_samples_path):
        os.mkdir(state_samples_path)

    for f in files:

        if os.path.exists(state_samples_path + '/' + f):
            os.remove(state_samples_path + '/' + f)

        new_file = open(state_samples_path + '/' + f, 'w')

        with open(state_data_path + '/' + f, encoding='latin-1') as file:
            for i in np.arange(nlines):
                new_file.write(file.readline())
            file.close()

    def zip_sample(state_path):

        if not os.path.exists(state_samples_zips + state_path + '.zip'):
            zf = zipfile.ZipFile(state_samples_zips + state_path + '.zip', 'w')
            zfiles = [n for n in os.listdir(state_data_path) \
                 if not ('.ipynb' in n.lower() \
                 or 'MACOSX' in n.lower() \
                 or '~$' in n.lower())]
            sample_files = [n for n in os.listdir(state_samples_path) \
                 if not ('.ipynb' in n.lower() \
                 or 'MACOSX' in n.lower() \
                 or '~$' in n.lower())]

        for f in zfiles:
            if f not in sample_files:
                zf.write(state_data_path + '/' + f,
                compress_type=zipfile.ZIP_DEFLATED, arcname=f)
            else:
                zf.write(state_samples_path + '/' + f,
                compress_type=zipfile.ZIP_DEFLATED, arcname=f)

        zf.close()

    zip_sample(state_path)


# A function I may use later
def recurse_yaml(yaml_dict, exclude):
    def recurse_help(yaml_dict):
        config = {}
        for c, v in yaml_dict.items():
            if c not in exclude and not isinstance(v, bool):
                if isinstance(v, dict):
                    v = recurse_help(v)
                elif isinstance(v, list):
                    v = [n.lower() for n in v]
                elif isinstance(v, str):
                    v = v.lower()
                config[c.lower()] = v
        return config
    new = recurse_help(yaml_dict)
    for x in exclude:
        new[x] = yaml_dict[x]
    return new
