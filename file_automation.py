# Image file Automation
# If you haven't Image file's dir, It'll Automatically create it

import os
import shutil

path = "/Users/jojong-un/Downloads/"
imagePath = "/Users/jojong-un/Desktop"
cwd = os.getcwd()

def run():

    if os.path.isdir(path + 'background_image'):
        moveImages()

    else:
        os.mkdir(path + 'background_image')
        moveImages()

def moveImages():
    for(dirname, dirs, files) in os.walk(path):
        for filename in files:
            if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                os.rename(path + filename, imagePath + '/' + filename)
        break
        
if __name__ == '__main__':
    run()