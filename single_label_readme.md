# Instructions For Dataset Annotations
Intended to be used by a virtual assistant.

# Getting Started:

1. Open Google Drive.
1. Click new Google Sheet.
1. Title the Google Sheet: `annotations.csv`.

# Column 1:

Using `TBD` fill in the first column. Each label should be on a new row.

# Every Column After That: 

`TBD` instructions will go here.

# Notes For ML Engineer:

This csv file will be used by `single_label_scraper.py`.

I like telling my virtual assistant to start with the first 5 rows, then send me the link to confirm we are in agreement about the instructions. After I spot check it, and make any corrections in communication, I confirm for them to continue through the rest of the document.

### Additional Notes On CSV Format:

- Don't include any headers.
- The first column is a list of terms you want to return from inference, a.k.a the class labels you will be training. For example: if you are classifying types of trees, this column would be a list of the different types of trees you want to recognize within an image.
- Every column after that is the search term you want the scraper to type into google image search. So if the first cell says, `ash tree` the next two cells could say `ash tree fall,ash tree winter`. Then the `single_label_scraper.py` script would search for `ash tree fall` and save the scraped image urls under `ash tree` directory that will be created by the script. 
- If only the first column is filled in, those labels will be used by the `sigle_label_scraper.py` to be passed into google image search.

### Running The Image Scraper:

Once you get the link to the file from your virtual assistant, download the Google Sheet as a csv file and save within the `src/annotations` directory.

Next run the following within the root directory:

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python single_label_scraper.py
```

### TODO: add flags for number of images and annotation file name