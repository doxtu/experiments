FEATURE = [1.0, 2.0,  3.0,  4.0,  5.0,  6.0,  7.0,  8.0,  9.0, 10.0, 11.0, 12.0] 
LABEL = [5.0, 8.8,  9.6, 14.2, 18.8, 19.5, 21.4, 26.8, 28.9, 32.0, 33.8, 38.2] 
# Arbitrarily large so we can reach accurate values eventually
MODEL = (100.0, 100.0)

def compute_gradient(feature, label, model):
    ''' returns a tuple containing the current gradients of a given model '''
    w = model[0]
    b = model[1]
    delta_w = 0
    delta_b = 0
    for i in range(len(feature)):
        x = feature[i]
        y = label[i]
        delta_w += 2*w*(x**2) - 2*x*b - 2*x*y
        delta_b += 2*b + 2*y - 2*w*x

    delta_w = delta_w / len(feature)
    delta_b = delta_b / len(feature)
    return (delta_w, delta_b)

def train_model(feature, label, model, training_rate=0.01, epoch=1000):
    for i in range(epoch):
        gradient = compute_gradient(feature, label, model)
        w = model[0]
        b = model[1]
        delta_w = gradient[0]
        delta_b = gradient[1]
        # update w
        if delta_w < 0:
            model = (model[0] + training_rate, model[1])
        else:
            model = (model[0] - training_rate, model[1])
        # update b
        if delta_b < 0:
            model = (model[0], model[1] + training_rate)
        else:
            model = (model[0], model[1] - training_rate)
    return model

if __name__ == '__main__':
    model = train_model(FEATURE, LABEL, MODEL, 0.1, 10000)
    print(model)
