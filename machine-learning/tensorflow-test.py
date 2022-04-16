import numpy as np
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.get_logger().setLevel('CRITICAL')
from matplotlib import pyplot as plot

def build_model(learning_rate):
    '''Create and compile a simple linear regression model'''
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))
    model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=learning_rate), loss='mean_squared_error', metrics=[tf.keras.metrics.RootMeanSquaredError()])
    return model

def train_model(model, feature, label, epochs, batch_size):
    ''' Train the model by feeding it data '''
    history = model.fit(
        x=feature,
        y=label,
        batch_size=batch_size,
        epochs=epochs,
        verbose=0
    )
    weight = model.get_weights()[0]
    bias = model.get_weights()[1]
    epochs = history.epoch
    hist = pd.DataFrame(history.history)
    rmse = hist['root_mean_squared_error']
    return weight, bias, epochs, rmse

def plot_model(weight, bias, feature, label):
    ''' plot the trained model against the training feature and label '''
    plot.xlabel('feature')
    plot.ylabel('label')
    plot.scatter(feature, label)
    x0 = 0
    y0 = bias
    x1 = feature[-1]
    y1 = bias + weight*x1
    plot.plot([x0, y0], [y0, y1], c='r')
    plot.show()

def plot_loss(epochs, rmse):
    plot.figure()
    plot.xlabel('epoch')
    plot.ylabel('Root Mean Squared Error')
    plot.plot(epochs, rmse, label='Loss')
    plot.legend()
    plot.ylim([rmse.min()*0.97, rmse.max()])
    plot.show()


if __name__ == '__main__':
    feature = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    label = [5.0, 8.8, 9.6, 14.2, 18.8, 19.5, 21.4, 26.8, 28.9, 32.0, 33.8, 38.2]
    learning_rate = 0.1
    epochs = 70
    batch_size = 12
    model = build_model(learning_rate)
    weight, bias, epochs, rmse = train_model(model, feature, label, epochs, batch_size)
    print('WEIGHT - ', weight)
    print('BIAS - ', bias)
