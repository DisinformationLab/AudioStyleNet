import torch.nn as nn
import os

from utils import Config

HOME = os.path.expanduser('~')

config = Config({
    # General configs
    'use_cuda': True,


    # Dataset configs
    'train_path': HOME + '/Datasets/RAVDESS/Landmarks/train',
    'val_path': HOME + '/Datasets/RAVDESS/Landmarks/val',
    'data_format': 'landmarks',

    # Hyper parameters
    'num_epochs': 10,
    'learning_rate': 0.001,
    'batch_size': 8,

    # Model parameters
    'model': nn.Sequential(
        nn.Flatten(),
        nn.Linear(68 * 2, 8),
        nn.Softmax(dim=1)
    ),

    # Logging
    'log_interval': 10,
    'save_interval': 1,
    'save_path': '/saves/Classification_Landmarks'
})
