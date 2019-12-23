# dataNotLore
usage TBD, work in progress.

# Getting Started:
```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Single Label Fine Grain Image Classification

This section relates to the `single_label_scraper.py` script.

## Create a csv file within the src/annotations directory

You can label this anything you want. I like to label the csv files the same name as the experiment that I want to run within jupyter notebook.

### Annotation csv file format

The end result of the `single_label_scraper.py` script will be a directory called `data_csv` with the following structure:

```
data_csv/
    ash_tree/
        ash_tree.csv
    bigleaf_maple/
        bigleaf_maple.csv
    ...
```

the folder names will be the class labels, and the csv files will contain the image urls that were scraped from google image search. This is output format will later be consumed by `download_images` in the fastai library, in order to download the images locally for training the classifier.

CSV format:
- Don't include any headers.
- The first column is a list of terms you want to return from inference, a.k.a the class labels you will be training. For example: if you are classifying types of trees, this column would be a list of the different types of trees you want to recognize within an image.
- Every column after that is the search term you want the scraper to type into google image search. So if the first cell says, `ash tree` the next two cells could say `ash tree fall,ash tree winter`. Then the `single_label_scraper.py` script would search for `ash tree fall` and save the scraped image urls under `ash tree` directory that will be created by the script. 
- If only the first column is filled in, those labels will be used by the `sigle_label_scraper.py` to be passed into google image search.

# Testing
Run within root directory.
```
python -m pytest tests
```

# Additional Notes:
This project is using selenium, and requires chrome browser version Version 77. If you need a different chrome version, [you can find it here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
