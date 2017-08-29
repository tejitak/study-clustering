import os
from PIL import Image
import numpy as np
from sklearn import decomposition
import pylab as pl
import pandas as pd

# STANDARD_SIZE = (120, 120)

def img_to_matrix(filename):
    img = Image.open(filename)
    # img = img.resize(STANDARD_SIZE)
    imgArray = np.asarray(img)
    return imgArray

def flatten_image(img, filename):
    # no channels containing means no data?
    if len(img.shape) == 2:
      return None
    # additional prop 'channels' indicates alpha for 4
    # 3 means RGB?
    if img.shape[2] == 4:
      return None

    # s = img.shape[0] * img.shape[1]
    s = img.shape[0] * img.shape[1] * img.shape[2]
    img_wide = img.reshape(1, s)
    # print(len(img_wide[0]), img_wide[0])
    return img_wide[0]

# main
if __name__ == "__main__":
    img_dir = "./images_data/"
    images = [img_dir+ f for f in os.listdir(img_dir)]
    data = []
    for image in images:
        if image == img_dir + ".DS_Store":
            continue
        img = img_to_matrix(image)
        img = flatten_image(img, image)
        if img is not None:
            data.append(img)
        #else:
        #   print(' No data contains!' + image)

    print('Count', len(data))
    data = np.asarray(data)
    pca = decomposition.PCA(n_components=2)
    pca.fit(data)
    X = pca.transform(data)
    df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1], "label":"Logo"})
    pl.scatter(df['x'], df['y'], c="red", label="Logo")
    # pl.legend()
    pl.show()
