import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import  linear_model

class mlp():
    def __int__(self):
        w0=[[1.15,-0.29,0.01], [1.44,1.53,-1.41], [-1.9,-1.27,0.68], [-2.21,-1.35,1.58]]
        w1=[[1.04,1.06,-2.01], [2.45,-2.1, -1.65], [-1.94, 0.36, 2.06]]
        w=[w0, w1]
        b=[[1.46,1.19,-0.94], [-0.81, 0.55, 0.94]]

        self.weights=w
        self.biases=b

    def sigmoid(self,z):
        return 1 / (1 + np.exp(-z))
    def softmax(self,x):
        return np.exp(x)/sum(np.exp(x))


    def feedforward(self,input):
        hidden_layer_value= self.sigmoid(np.matmul(input, self.weights[0])+self.biases[0])
        ouput_value=self.softmax(np.matmul(hidden_layer_value, self.weights[1])+self.biases[1])
        return hidden_layer_value, ouput_value
    def predict(self, input):
        h,o =self.feedforward(input)
        class_index=np.argmax(o, axis=-1)
        if class_index==0:
            class_name='sentosa'
        else:
            if class_index==1:
                class_name="versicolor"
            else:
                class_name="virginica"
        return h,o,class_name

network = mlp()
print(network.weights)
print(network.biases)

x=[6.3, 2.3, 4.4, 1.3]
h,o, class_name= network.predict(x)

print("Probability vector:", o)
print("Predict class:", class_name)





