"""
Load csv file, process with spaCy and convert to CoNLL

Usage:
  convert_text_to_conll.py --config_path=<config_path>

Options:
    --config_path=<config_path> a JSON containing the settings, see ../config/convert.json for an example

Example:
    python convert_text_to_conll.py --config_path="../config/convert.json"
"""
from docopt import docopt
import json
import os

import pandas as pd
import spacy

from TextToCoNLL import text_to_conll

# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

settings = json.load(open(arguments['--config_path']))
nlp = spacy.load(settings['text_to_conll']['spacy_model_name'])

# process and convert
for csv_path in settings['csv_paths']:
    basename = os.path.basename(csv_path)
    df = pd.read_csv(csv_path)
    print(f'loaded {csv_path} containing {len(df)} rows.')

    for index, row in df.iterrows():

        if index >= settings['first_n_rows']:
            break

        text_to_conll(text=row[settings['csv_columnname']],
                      nlp=nlp,
                      delimiter=settings['text_to_conll']['delimiter'],
                      output_dir=settings['text_to_conll']['output_dir'],
                      basename=f'{basename}---{index+1}.conll',
                      spacy_attrs=settings['text_to_conll']['spacy_attrs'],
                      default_values=settings['text_to_conll']['default_values'],
                      start_with_index=settings['text_to_conll']['start_with_index'],
                      verbose=1)