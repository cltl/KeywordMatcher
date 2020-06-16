"""
Given a collection of CoNLL files,
obtain an index mapping a category, e.g., D450, to the files
that contain keywords that belong to this category, e.g., lopen, loopt, gelopen, traplopen

Usage:
  keyword_index.py --config_path=<config_path>

Options:
    --config_path=<config_path> a JSON containing the settings, see ../config/keywords.json for an example

Example:
    python keyword_index.py --config_path="../config/keywords.json"
"""
from docopt import docopt
import json
import os
from collections import defaultdict, Counter
from glob import glob

from utils import get_sample

# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

label_to_basenames = defaultdict(set)

settings = json.load(open(arguments['--config_path']))
label_to_keywords = settings['label_to_keywords']

# inspect overlap
all_keywords = [keyword
                for label, keywords in label_to_keywords.items()
                for keyword in keywords]
label_to_freq = Counter(all_keywords)
for label, freq in label_to_freq.items():
    assert freq == 1, f'{label} occurs in more than once label. Please inspect.'

input_dir = settings['input_folder']
suffix = settings['suffix']
delimiter = settings['conll_delimiter']
for conll_path in glob(f'{input_dir}/*{suffix}'):
    basename = os.path.basename(conll_path)

    with open(conll_path) as infile:
        for line in infile:
            split = line.strip().split(delimiter)
            value = split[settings['index_column']]

            for label, keywords in label_to_keywords.items():
                if value in keywords:
                    label_to_basenames[label].add(basename)

with open(settings['output_path_index'], 'w') as outfile:
    label_to_list = {label: list(basenames)
                     for label, basenames in label_to_basenames.items()
                     }
    json.dump(label_to_list, outfile)

print(f'written index to {settings["output_path_index"]}')

label_to_basenames_sample = {}

for label, basenames in label_to_basenames.items():
    sample = get_sample(list(basenames),
                        settings['sample_size_per_label'])
    label_to_basenames_sample[label] = sample

with open(settings['output_path_index_sample'], 'w') as outfile:
    json.dump(label_to_basenames_sample, outfile)

print(f'written index sample to {settings["output_path_index_sample"]}')


