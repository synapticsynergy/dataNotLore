# Instructions For Dataset Annotations. Multi-label Classification
Intended to be quickly edited and used by a virtual assistant.

# Getting Started:

1. Open Google Drive.
1. Click new Google Sheet.
1. Title the Google Sheet: `annotations.csv`.

# Imageset and List of Labels

I will send you a link to an imageset. I want you to look at each image and write down the labels you see per image in the annotations.csv file. I will also be sending you a link to the acceptable labels I want you to use.

# Column 1:

In column 1, I want you to list filenames for each image.

# Column 2: 

In column 2, I want you to do the following:
1. Look at the image in that row, for column 1.
1. Look at the list of labels I sent you.
1. In column two in that row, I want you to write the labels separated by a `:`.

For example: `file_one.jpg, car:sign:person:bike`.

The end result should contain be two columns of data per each row, and each row is a unique image.

# Notes For ML Engineer:

This csv file is intended to be used by an experiment using standard libraries in fastai. It currently assumes you have the images saved locally.

I like telling my virtual assistant to start with the first 5 rows, then send me the link to confirm we are in agreement about the instructions. After I spot check it, and make any corrections in communication, I confirm for them to continue through the rest of the document.

### Additional Notes On CSV Format:

- The headers should be column 1: `image_name` and column 2: `tags`.
- The first column is a list of images you want for training and validation.
- The second column is a list of terms you want to return from inference, a.k.a the class labels you will be training. For example: if you are classifying satalite images, this column would be a list of the different types of things you want to recognize within an image: `forest:street:cloudy:lake`.


### TODO: add example experiment to consume this format for training.