#!/usr/bin/env bash

python -m spacy download nl_core_news_sm

cd lib
git clone https://github.com/cltl/TextToCoNLL
cd TextToCoNLL
pip install -r requirements.txt

