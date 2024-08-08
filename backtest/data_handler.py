import os, sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, PROJECT_ROOT)

import warnings
warnings.filterwarnings('ignore')

import pandas as pd

class DataHandler:
    def __init__(self,data):
        self.data = data
    
    #定義使用[]進行索引操作的行為
    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError("Key not in data")

