import cv2
import numpy as np
from matplotlib import pyplot as plt

def show(image, cmap=None):
    plt.axis('off')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB )
    plt.imshow(image, cmap=cmap)
    plt.show()
    
img = cv2.imread('django_opencv/my_app/media/images-28.jpeg')
show(img) 