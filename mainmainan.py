from PyQt5 import QtWidgets, QtGui, QtCore
from tes1 import Ui_MainWindow
import sys
import cv2
import numpy as np
import scipy
import scipy.spatial
import imageio
import pickle
import random
import os
import matplotlib.pyplot as plt
import math


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.setFixedSize(400,750)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tombolLoad.clicked.connect(lambda: self.load())
        self.ui.gambar.setPixmap(QtGui.QPixmap("a.png"))
        self.ui.tombolCos.clicked.connect(lambda: run(2))
    def load(self):
        loader = QtWidgets.QFileDialog()
        self.name, _ = loader.getOpenFileName()
        self.ui.gambar.setPixmap(QtGui.QPixmap(self.name))

    def compare(self):
        a = 1
        print(a)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    
def extract_features(image_path, vector_size=32):
    image = imageio.imread(image_path, pilmode="RGB")
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None

    return dsc


def batch_extractor(images_path, pickled_db_path="reference.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print ('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

class Matcher(object):

    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path, 'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)
    
    def euclidian_distance(self, vector) :
        v = vector.reshape(1,-1)
        distance = np.empty([len(self.matrix), len(v)])
        for i in range(len(self.matrix)) :
            for j in range(len(v)) :
                distance[i][j] = np.sqrt(np.sum((self.matrix[i]-v[j])**2))
        return distance.reshape(-1)
    
    def cosine_similarity(self, vector):
        v = vector.reshape(1,-1)
        distance = np.empty([len(self.matrix), len(v)])
        for i in range(len(self.matrix)) :
            for j in range(len(v)) :
                distance[i][j] = (np.dot(self.matrix[i],v[j]) / (np.linalg.norm(self.matrix[i]) * np.linalg.norm(v[j])))
        return distance.reshape(-1)
    
    """def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        v = vector.reshape(1, -1)
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1)"""

    def match(self, image_path, option, topn=5):
        features = extract_features(image_path)
        if (option==1) :
            img_distances = self.euclidian_distance(features)
        elif (option==2) :
            img_distances = self.cosine_similarity(features)
        
        # getting top 5 records
        if (option==1) :
            nearest_ids = np.argsort(img_distances)[:topn].tolist()
        elif (option==2) :
            nearest_ids = np.argsort(img_distances)[::-1][:topn].tolist()

        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()

def show_img(path):
    img = imageio.imread(path, pilmode="RGB")
    plt.imshow(img)
    plt.show()
    
def run(option):
    images_path = 'images/reference/'
    files = [os.path.join('images/test/', p) for p in sorted(os.listdir('images/test/'))]
    # getting 3 random images
    #print(files)
    sample = random.sample(files, 3)

    """print("What metode would you wanna choose? Input your answer in number.")
    print("1. Euclidian Distance")
    print("2. Cosine Similarity")
    option = int(input(">> "))"""
    
    batch_extractor(images_path)

    ma = Matcher('reference.pck')
    
    for s in sample:
        print('Query image ==========================================')
        show_img(s)
        names, match = ma.match(s, option, topn=3)
        print('Result images ========================================')
        for i in range(3):
            if (option==1) :
                print('Match %s' % (1 - match[i]))
            elif (option==2) :
                print('Match %s' % (match[i]))
            show_img(os.path.join(images_path, names[i]))

if __name__ == "__main__":
    main()