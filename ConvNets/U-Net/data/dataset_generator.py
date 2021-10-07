# -*- coding: utf-8 -*-
"""dataset_generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aNSZTPoVDF27D72Zr-93SLfHjvAs2J1B
"""

import os
import matplotlib.pyplot as plt
from torch.utils.data import Dataset
import numpy as np

class Cityscapes(Dataset):
  def __init__(self, root_dir, transform = None):
    self.root_dir = root_dir
    self.images = os.listdir(self.root_dir+'inputs/')
    self.labels = os.listdir(self.root_dir+'labels/')
    assert len(self.labels) == len(self.images)
    self.transform = transform
  
  def __len__(self):
    return len(self.labels)
  
  def __getitem__(self, index):
    image = plt.imread(root_dir + 'inputs/' + str(index+1) + '.jpg') / 255
    label = plt.imread(root_dir + 'labels/' + str(index+1) + '.jpg') / 255

    if self.transform is not None:
      augmentations = self.transform(image = image, mask = label)

    return image, label