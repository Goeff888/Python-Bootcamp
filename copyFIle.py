
import os

my_file = open('settings.txt')
my_file.read()
for zeile in open('settings.txt'):
    if ("Source" in zeile):
        source = zeile[len("Source:"):]
        for filename in os.listdir(source[:len(source)-1]):
            print(filename)
    elif ("Destination" in zeile):
        dest = zeile[len("Destination:"):len(zeile)]
        print(dest)

