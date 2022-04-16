FEATURE = [1.0, 2.0,  3.0,  4.0,  5.0,  6.0,  7.0,  8.0,  9.0, 10.0, 11.0, 12.0] 
LABEL = [5.0, 8.8,  9.6, 14.2, 18.8, 19.5, 21.4, 26.8, 28.9, 32.0, 33.8, 38.2] 
MODEL = (0.1, -0.1)

# Create model (weight, bias) that reduces MSE of model to data comparison

def compute_model(feature, model):
    ''' Computes model values for each feature '''
    weight = model[0]
    bias = model[1]
    return [ weight*x + bias for x in feature ]

def compute_mse(feature, label, model):
    ''' Computes the mean square error of a given model '''
    weight = model[0]
    bias = model[1]
    model_predictions = compute_model(feature, model) 
    mse = 0
    for i, y in enumerate(label):
        mse += (y - model_predictions[i])**2 
    mse = mse / len(feature)
    return mse

# We now want to minimize loss via gradient descent... Or assume that the loss decreases with each iteration

def train_model(model, training_rate):
    def train_weight(model, training_rate):
        mse=0 
        mse_delta=0
        feature = model['feature']
        label = model['label']
        while True:
            md = model['model']
            mse = compute_mse(feature, label, md)

            md_delta = (model['model'][0] + training_rate, model['model'][1])
            mse_delta = compute_mse(feature, label, md_delta)
            if mse_delta > mse: return model
            model['model'] = (model['model'][0] + training_rate, model['model'][1])

    def train_bias(model, training_rate):
        mse=0 
        mse_delta=0
        feature = model['feature']
        label = model['label']
        while True:
            md = model['model']
            mse = compute_mse(feature, label, md)

            md_delta = (model['model'][0], model['model'][1]+training_rate)
            mse_delta = compute_mse(feature, label, md_delta)
            if mse_delta > mse: return model
            model['model'] = (model['model'][0], model['model'][1]+training_rate)

    return train_bias(train_weight(model, training_rate), training_rate)

if __name__ == '__main__':
    m = {
        'feature': FEATURE,
        'label': LABEL,
        'model': MODEL
    }
    for i in range(10):
        train_model(m, 0.01)
    print(m['model'])
    print('my mse', compute_mse(FEATURE, LABEL, m['model'])) 
    print('tensorflow mse', compute_mse(FEATURE, LABEL, (2.7942348, 3.3259323)))
