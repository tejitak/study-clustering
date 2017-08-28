import os
from PIL import Image
import numpy as np
from sklearn import decomposition
import pylab as pl

STANDARD_SIZE = (120, 120)

def img_to_matrix(filename, verbose=False):
    img = Image.open(filename)
    if verbose:
        print('changing size from %s to %s' % (str(img.size), str(STANDARD_SIZE)))
    img = img.resize(STANDARD_SIZE)
    imgArray = np.asarray(img)
    return imgArray  # imgArray.shape = (167 x 300 x 3)

def flatten_image(img):
    """
    takes in an (m, n) numpy array and flattens it 
    into an array of shape (1, m * n)
    """
    if len(img.shape) == 2:
      return None

    # s = img.shape[0] * img.shape[1]
    s = img.shape[0] * img.shape[1] * img.shape[2]
    img_wide = img.reshape(1, s)
    return img_wide[0]

# main
if __name__ == "__main__":
    img_dir = "./images_data/"
    images = [img_dir+ f for f in os.listdir(img_dir)]
    data = []
    for image in images:
        if image == "./images_data/.DS_Store":
            continue
        img = img_to_matrix(image)
        img = flatten_image(img)
        if img is not None:
            data.append(img)
        #else:
        #   print(' No data contains!' + image)

    data = np.array(data)

    pca = decomposition.PCA(n_components=2)
    print(len(data))
    pca.fit(data)
    X = pca.transform(data)
    df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1], "label":"Logo"})
    pl.scatter(df['x'], df['y'], c="red", label="Logo")
    pl.legend()
    pl.show()
