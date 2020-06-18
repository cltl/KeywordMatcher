"""
Create the directory to be used by Inception

Usage:
  package_sample.py --sample_dir=<sample_dir> --config_path=<config_path>

Options:
    --sample_dir=<sample_dir> the directory to be read by inception
    --config_path=<config_path> a JSON containing the settings, see ../config/keywords.json for an example

Example:
    python package_sample.py --sample_dir="../output/inception" --config_path="../config/keywords.json"
"""
import os
import json
import shutil
from docopt import docopt

# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

settings = json.load(open(arguments['--config_path']))

sample_dir = arguments['--sample_dir']

# create inception folder
os.mkdir(sample_dir)

# TODO move files to the inception folder
index_sample = json.load(open(settings['output_path_index_sample']))


for label, conll_basenames in index_sample.items():
    for conll_basename in conll_basenames:
        src = os.path.join(settings['input_folder'],
                           conll_basename)
        dst = os.path.join(sample_dir,
                           conll_basename)

        shutil.copy(src, dst)

# cp the index json file
basename = os.path.basename(settings['output_path_index_sample'])
shutil.copy(
    settings['output_path_index_sample'],
    os.path.join(sample_dir, basename)
)

# cp the settings to it
basename = os.path.basename(arguments['--config_path'])
shutil.copy(
    arguments['--config_path'],
    os.path.join(sample_dir, basename)
)
