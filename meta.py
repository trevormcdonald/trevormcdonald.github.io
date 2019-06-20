#!/usr/bin/python
#Go through the podcast directory and create a data csv file with metadata
#So far, only file length is saved
import os, csv

lengths = {}

for file in os.listdir("./assets/pod/"):
    if file.endswith(".mp3"):
        lengths[file] = os.path.getsize("./assets/pod/"+file)
print lengths

with open("./_data/pods.csv", 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'length'])
    for key in lengths:
        writer.writerow([key, lengths[key]])
