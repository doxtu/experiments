import numpy as np
import pandas as pd

def task1():
    ''' Assign a sequence of integers from 6 to 20 to a numpy array
    Assign 15 values to a numpy array named label such that
    label = 3*feature + 4
    Add some random noise between -2 and 2 to label
    '''
    feature = np.arange(6,21)
    label = 3*feature + 4 + (2 - 4*np.random.random())
    print(feature, label)

def task2():
    ''' Create a pandas dataframe with columns Eleanor, Chidi, Tahani, Jason
    Populate the 3x4 12 cells with random numbers between 1-100
    '''
    data = np.zeros((3, 4)) + np.random.randint(low=0, high=100, size=(3,4))
    dataframe = pd.DataFrame(data=data, columns=['Eleanor', 'Chidi', 'Tahani', 'Jason'])
    dataframe['Janet'] = dataframe['Tahani'] + dataframe['Jason']
    print(dataframe)
    print('Eleanor row 1 value', dataframe['Eleanor'][1:2])


if __name__ == '__main__':
    #task1()
    task2()

