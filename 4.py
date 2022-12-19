#Implement deep nn for binary classification task
#Code: -
from numpy import loadtxt
import tensorflow
from keras.models import Sequential
from keras.layers import Dense
dataset = loadtxt('pima-indians-diabetes.csv',delimiter=',')
print(dataset)
X=dataset[:,0:8]
Y=dataset[:,8]
print(X)
print(Y)
#creating model
model=Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
#compiling and fitting model
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=150,batch_size=10)
#evaluating the accuracy
_,accuracy=model.evaluate(X,Y)
print('acuracy of model is',(accuracy*100))
