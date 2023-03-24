import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.mnist

(train_data, train_labels), (test_data, test_labels) = data.load_data()

train_data = train_data / 255
test_data = test_data / 255

'''
# Model
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28))) #1x784 now
model.add(keras.layers.Dense(160, activation="relu"))
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax")) #softmax will add the neurons up to 1 (so give %)

model.summary()
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Training the model
model.fit(train_data, train_labels, epochs=30, batch_size=1000)

test_loss, test_acc = model.evaluate(test_data, test_labels)
print("Loss: ", test_loss)
print("Acc: ", test_acc)

# Saving model
model.save("numbermodel.h5")
'''
# Call model
model = keras.models.load_model("numbermodel.h5")

# print output
model.summary
outputnumbers = list(range(0,10))

# Prediction
test_pred = test_data[0]
test_pred = test_pred[None, :]

prediction = model.predict(test_data)

# Plot
for i in range(10):
    plt.grid(False)
    plt.imshow(test_data[i], cmap=plt.cm.binary) #Making it b/w
    plt.xlabel("Actual number: " + str(outputnumbers[test_labels[i]]))
    plt.title("Predicted number: " + str(outputnumbers[np.argmax(prediction[i])]))
    plt.show()
    print(prediction[i])

# Models result
## batch_size = 5000
# 160 sigm, 16 sigm             ep = 10 - 1,24 - 0,81       ep = 20 - 0,7665 - 0,8834       0,74 - 0,8908
# 160 relu, 16 relu             ep = 10 - 0,25 - 0,93       ep = 20 - 0,1483 - 0,9588       0,15 - 0,9563
# 160 relu, 16 relu, 16 relu    ep = 10 - 0,26 - 0,93       ep = 20 - 0,1377 - 0,9617       0,16 - 0,9588

## batch_size = 10000
# 160 relu, 16 relu             ep = 10 - 0,36 - 0,90       ep = 20 - 0,2194 - 0,9391       0,21 - 0,9382

## batch_size = 1000
# epochs = 15                                               ep = 15 - 0.0578 - 0.9836       0.09 - 0.9727
# 160 relu, 16 relu             ep = 10 - 0,08 - 0,9769     ep = 20 - 0,0335 - 0,9915       0,08 - 0,9757
# epochs = 25                                               ep = 30 - 0.0346 - 0.9915       0.09 - 0.9760
# epochs = 30                                               ep = 30 - 0.0152 - 0.9973       0.07 - 0.9795 -> 1
# #2                                                        ep = 30 - 0.0159 - 0.9970       0.07 - 0.9795 -> 1
# MODEL USED 160, 16, 16, ep=30         Training data:  loss = 0.0165 - acc = 0.9970        Test: 0.0776 - 0.9774
# 128 relu, 16 relu                                         ep = 30 - 0.0212 - 0.9953       0.08 - 0.9774
# 200 relu, 20 relu             ep = 10 - 0.07 - 0.9804     ep = 30 - 0.0097 - 0.9988       0.08 - 0.9787 -> 2
# 64 relu, 16 relu              ep = 10 - 0.14 - 0.9604     ep = 30 - 0.0506 - 0.9861       0.10 - 0.9721
# 64 relu, 16 relu, 16 relu     ep = 10 - 0.12 - 0.9654     ep = 30 - 0.0410 - 0.9886       0.11 - 0.9712
# epochs = 50                                               ep = 30 - 0.0035 - 0.9999       0.10 - 0.9770

## batch_size = 500
# 160 relu, 16 relu             ep = 10 - 0,05 - 0,9844     ep = 20 - 0,0167 - 0,9967       0,08 - 0,9771
# epochs = 30                                               ep = 30 - 0.0055 - 0.9995       0.09 - 0.9784
# #2                                                        ep = 30 - 0.0068 - 0.9990       0.08 - 0.9784 -> 3
# 128 relu, 16 relu                                         ep = 30 - 0.0078 - 0.9987       0.09 - 0.9755