from sklearn import svm
import cv2
import numpy as np
import glob
from joblib import dump

# HOG
hog = cv2.HOGDescriptor(
    _winSize=(64,64),
    _blockSize=(16,16),
    _blockStride=(8,8),
    _cellSize=(8,8),
    _nbins=9
)

X = []
y = []

# データセット読み込み
for label in ['fu_up','fu_down',
              'tokinn_up','tokinn_down',
              'ou_up','ou_down',
              'gyoku_up','gyoku_down',
              'keima_up','keima_down',
              'None']:
    for file in glob.glob(f'data/{label}/*.png'):
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (64,64))
        descriptor = hog.compute(img)
        X.append(descriptor.flatten())
        y.append(label)

X = np.array(X)
y = np.array(y)

# SVM学習
clf = svm.SVC(kernel='linear')
clf.fit(X, y)
dump(clf, 'shogi_model.joblib')


img = cv2.imread('test_keima.png', cv2.IMREAD_GRAYSCALE);
img = cv2.resize(img, (64,64));
descriptor = hog.compute(img);
predicted = clf.predict([descriptor.flatten()]);

print(f"推論結果: {predicted[0]}");

