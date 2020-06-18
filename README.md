# Keyword matcher

The goal of this repository is to 
1. convert the text in one column of every row in a CSV file to CoNNL using [spaCy](https://spacy.io/)
2. create a dictionary indicating which rows contain the keywords you are interested in.

## Prerequisites
Python 3.6 was used to create this project. It might work with older versions of Python.

## Python modules
A number of external modules need to be installed, which are listed in **requirements.txt**.
Depending on how you installed Python, you can probably install the requirements using one of following commands:
```bash
pip install -r requirements.txt
```

## External resources
Please run the following command to download external resources

```bash
bash install.sh
```

## Usage

Step 1: conver text to CoNLL
This can be achieved using the script at **lib/convert_text_to_conll.py**.
Please call the following command for more information about how to use it.
```
python lib/convert_text_to_conll.py -h
```

Step 2: index based on keywords
We use the **lib/python keyword_index.py** to obtain this information.
Please call for more information:

```bash
python lib/keyword_index.py -h
```

The result is an index from a label to the CoNLL basenames that belong
to this label.

Step 3: package it
You can use

```bash
python lib/package_sample.py -h
```

## Authors
* **Marten Postma** (m.c.postma@vu.nl)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
