How to Run

1. Run imageGenerator.py to generate our sudo ECG images

2. Run ImageLabeler to generate the labels for our CNN in a file called imageLabels.csv

imageGenerator.py: Generate the sudo ECG images
ImageLabeler.py: Generates the labels for the CNN

/data folder: Where the generated ECG images are stored when imageGenerator.py is ran

/images folder: Where the original ECG images are stored. DO NO CHANGE OR MANIPULATE THEM

NOTE: there is a bug where the last image of each potasium level is blank so make sure to delete them before running the image labeler!
