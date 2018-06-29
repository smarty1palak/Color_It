from PIL import Image
import os

# All images in 'train_orig' will be resized to (dimension x dimension), and placed in 'train_resized' folder.
dimension = 256

if not os.path.exists('./train_resized'):
    os.makedirs('./train_resized')
    
for image in os.listdir('./train_orig/'):
    im = Image.open('./train_orig/' + image)
    im = im.resize((dimension, dimension))
    im.save('./train_resized/' + image)
    print('Resized', image)