from PyQt5 import QtWidgets, QtGui, QtCore
from gui import Ui_MainWindow
import sys
import cv2
import numpy as np
import scipy
import scipy.spatial
import imageio
import pickle
import os
import matplotlib.pyplot as plt

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.setFixedSize(700,575)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tombolLoad.clicked.connect(lambda: self.loadkiri())
        self.ui.tombolCosi.toggled.connect(lambda: self.choose())
        self.ui.tombolEuc.toggled.connect(lambda: self.choose())
        self.ui.tombolFind.clicked.connect(lambda: self.find())
        self.ui.tombolFind.clicked.connect(lambda: self.loadkanan())        
        self.ui.tombolNext.clicked.connect(lambda: self.nextnext())
        self.ui.tombolPrev.clicked.connect(lambda: self.prevprev())
        self.ui.spinBox.valueChanged.connect(lambda: self.count())
        self.ui.home.clicked.connect(lambda: self.removehome())

        self.ui.tombolNext.setStyleSheet("background-image: url('next.png'); background-color: rgba(0, 0, 0, 0); background-repeat: no-repeat")
        self.ui.tombolPrev.setStyleSheet("background-image: url('prev.png'); background-color: rgba(0, 0, 0, 0); background-repeat: no-repeat")
        self.ui.tombolFind.setStyleSheet("background-color: rgba(205, 255, 245, 80); color: rgb(205, 255, 245)")
        self.ui.tombolLoad.setStyleSheet("background-color: rgba(205, 255, 245, 80); color: rgb(205, 255, 245)")
        self.ui.home.setStyleSheet("background-image: url('start1.jpg')")
        self.ui.judul.setStyleSheet("color: rgb(205, 255, 245)")
        self.ui.query.setStyleSheet("color: rgb(205, 255, 245)")
        self.ui.result.setStyleSheet("color: rgb(205, 255, 245)")
        self.ui.similarity.setStyleSheet("color: rgb(205, 255, 245)")
        self.ui.similarity2.setStyleSheet("color: rgb(205, 255, 245)")
        self.ui.similarity2.setAlignment(QtCore.Qt.AlignRight)
        self.ui.tombolCosi.setStyleSheet("color: rgb(205, 255, 245)")
        self.ui.tombolEuc.setStyleSheet("color: rgb(205, 255, 245)")
        self.ui.label.setStyleSheet("color: rgb(205, 255, 245)")

        self.timer1 = QtCore.QTimer(self)
        self.timer1.setInterval(2638)
        self.timer1.timeout.connect(lambda: self.ui.home.setStyleSheet("background-image: url('start2.jpg')"))
        self.timer1.start()

        self.movie = QtGui.QMovie("bg.gif") 
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()  

        self.ui.spinBox.setMinimum(1)
        self.ui.tombolEuc.setChecked(True)
        
        self.ui.tombolFind.setEnabled(False)
        self.ui.tombolNext.setEnabled(False)
        self.ui.tombolPrev.setEnabled(False)

    def removehome(self):
        self.ui.home.deleteLater()
        self.timer1.stop()

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QtGui.QPainter(self) 
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)

    def loadkiri(self):
        loader = QtWidgets.QFileDialog()
        self.name, _ = loader.getOpenFileName()
        self.ui.gambar.setPixmap(QtGui.QPixmap(self.name))
        if(len(self.name)!=0):
            self.ui.tombolFind.setEnabled(True)

    def loadkanan(self):
        loader = QtWidgets.QFileDialog()
        self.ui.gambar2.setPixmap(QtGui.QPixmap(self.names_arr[0]))
        self.ui.similarity2.setText('%s / %s' % (self.iterate+1, self.num))
        self.ui.tombolNext.setEnabled(True)
        self.ui.tombolPrev.setEnabled(True)
        if (self.option==1) :
            self.ui.similarity.setText('Match %s%%' % round((1 - 0.1*self.match[self.iterate])*100,4))
        elif (self.option==2) :
            self.ui.similarity.setText('Match %s%%' % round(self.match[self.iterate]*100,4))

    def count(self):
        self.num = self.ui.spinBox.value()

    def choose(self):
        if self.ui.tombolCosi.isChecked()==True:
            self.option = 1
        if self.ui.tombolEuc.isChecked()==True:
            self.option = 2
            
    def find(self):
        images_path = 'images/references/'
        files = [self.name]
    
        ma = Matcher('references.pck')
        self.iterate = 0
        
        for s in files:
            self.names_pic, self.match = ma.match(s, self.option, self.num)
            self.names_arr = ["" for i in range(self.num)]
            self.names_arr[self.iterate] = os.path.join(images_path, self.names_pic[self.iterate])
       
    def nextnext(self) :
        images_path = 'images/references/'
        self.iterate += 1
        if (self.iterate == self.num) :
            self.iterate = 0
        self.names_arr[self.iterate] = os.path.join(images_path, self.names_pic[self.iterate])
        self.ui.gambar2.setPixmap(QtGui.QPixmap(self.names_arr[self.iterate]))
        self.ui.similarity2.setText('%s / %s' % (self.iterate+1, self.num))
        if (self.option==1) :
            self.ui.similarity.setText('Match %s%%' % round((1 - 0.1*self.match[self.iterate])*100,4))
        elif (self.option==2) :
            self.ui.similarity.setText('Match %s%%' % round(self.match[self.iterate]*100,4))

    def prevprev(self) :
        images_path = 'images/references/'
        self.iterate -= 1
        if (self.iterate == -1) :
            self.iterate = self.num-1
        self.names_arr[self.iterate] = os.path.join(images_path, self.names_pic[self.iterate])
        self.ui.gambar2.setPixmap(QtGui.QPixmap(self.names_arr[self.iterate]))
        self.ui.similarity2.setText('%s / %s' % (self.iterate+1, self.num))
        if (self.option==1) :
            self.ui.similarity.setText('Match %s%%' % round((1 - 0.1*self.match[self.iterate])*100,4))
        elif (self.option==2) :
            self.ui.similarity.setText('Match %s%%' % round(self.match[self.iterate]*100,4))

class Matcher(object):
    def __init__(self, pickled_db_path="references.pck"):
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
    
    def match(self, image_path, option, topn):
        features = extract_features(image_path)
        if (option==1) :
            img_distances = self.euclidian_distance(features)
            nearest_ids = np.argsort(img_distances)[:topn].tolist()
        elif (option==2) :
            img_distances = self.cosine_similarity(features)
            nearest_ids = np.argsort(img_distances)[::-1][:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()

    sys.exit(app.exec_())

def extract_features(image_path, vector_size=32):
    image = imageio.imread(image_path, pilmode="RGB")
    try:
        alg = cv2.KAZE_create()
        kps = alg.detect(image)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        kps, dsc = alg.compute(image, kps)
        dsc = dsc.flatten()
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
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
    
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)
    
if __name__ == "__main__":
    main()