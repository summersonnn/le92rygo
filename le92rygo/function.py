import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    #Convert incoming array to PIL image object
    im = Image.fromarray(X)

    #Resize it and show
    plt.imshow( im.resize(resize) )
