import argparse
import os

from corescore.models import CoreModel
import mlflow

def train(epochs=10, lr=0.00001, path=os.getcwd()):
    mlflow.fastai.autolog()
    coremodel = CoreModel(path, epochs=epochs)
    unet_learn = coremodel.learner()
    coremodel.fit(lr=lr, learner=unet_learn)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', help="Epochs to train, default 10")
    parser.add_argument('--lr', help="Learning rate to perform training")
    args = parser.parse_args()
    epochs = args.epochs
    if not epochs:
        epochs = 10
    lr = args.lr
    if not lr:
        lr = 0.00001
    train(epochs=int(epochs), lr=float(lr))

