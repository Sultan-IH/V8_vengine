from Vengine.Layers import DenseLayer, ConvLayer, PoolLayer
from Vengine.main import train, Network
from Vengine.Engines import Adam_engine
from Vengine.Costs import CrossEntropy

from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

mnist = input_data.read_data_sets("../Cases/MNIST/MNIST_data/", one_hot=True)

batch_xs, batch_ys = mnist.train.next_batch(50000)

layers = [
    ConvLayer((5, 5, 1, 15)),
    PoolLayer(),
    ConvLayer((5, 5, 15, 30)),
    PoolLayer(),
    DenseLayer([7 * 7 * 30, 250])  # the shape of this tensor was the problem

]

data_sets = {
    "Train_data": [batch_xs, batch_ys],
    "Test_data": [mnist.test.images, mnist.test.labels],
    "Validation_data": False

}
data_sets["Train_data"][0] = np.reshape(data_sets["Train_data"][0], [-1, 28, 28, 1])
data_sets["Test_data"][0] = np.reshape(data_sets["Test_data"][0], [-1, 28, 28, 1])


model = Network(layers=layers)

model.add_layer(DenseLayer([250, 10]), 5)
model.fit_engine(engine=Adam_engine(CrossEntropy, lr=1e-3))

train(net=model, data_sets=data_sets, epochs=30, batch_size=32, log=True)
