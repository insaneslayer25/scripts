import os
import shutil

source = '/Users/sujith/AIO/Courses/Django Part 1/2.Django Fundamentals (45m)'
target = '/Users/sujith/AIO/Courses/Django Part 1/new'

# Create target directory if it doesn't exist
if not os.path.exists(target):
    os.makedirs(target)

for root, dirs, files in os.walk(source):
    for file in files:
        if file.endswith(('.mp4', '.avi', '.mkv', '.mov')):
            source_file = os.path.join(root, file)
            # Move the file to the target directory
            shutil.move(source_file, target)
