from PIL import Image
import os

# All images in 'train_orig' will be resized to (dimension x dimension), and placed in 'train_resized' folder.
dimension = 300

if not os.path.exists('./result_resized'):
    os.makedirs('./result_resized')
    
for image in os.listdir('./result/'):
    im = Image.open('./result/' + image)
    im = im.resize((dimension, dimension))
    im.save('./result_resized/' + image)
    print('Resized', image)
