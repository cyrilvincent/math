import numpy as np
import sklearn.neighbors as nn
import sklearn.ensemble as rf
import sklearn.neural_network as neural

with np.load("data/mnist/mnist.npz", allow_pickle=True) as f:
    x_train, y_train = f["x_train"], f["y_train"] # 60000
    x_test, y_test = f["x_test"], f["y_test"] # 10000
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

# model = rf.RandomForestClassifier()
model = neural.MLPClassifier(hidden_layer_sizes=(784,500,300))
model.fit(x_train, y_train)

score = model.score(x_test, y_test)
print(score)

predicted = model.predict(x_test)

import matplotlib.pyplot as plt

# plt.imshow(model.feature_importances_.reshape(28, 28))
# plt.show()

images = x_test.reshape((-1, 28, 28))
select = np.random.randint(images.shape[0], size=12)



for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: %i' % predicted[value])

plt.show()

# Gestion des erreurs
# on récupère les données mal prédites
misclass = (y_test != predicted)
misclass_images = images[misclass]
misclass_predicted = predicted[misclass]

# on sélectionne un échantillon de ces images
select = np.random.randint(misclass_images.shape[0], size=12)

# on affiche les images et les prédictions (erronées) associées à ces images
for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(misclass_images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: %i' % misclass_predicted[value])

plt.show()