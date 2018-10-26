import pandas as pd
import numpy as np

train_file = 'data/kaggle/train.csv'
test_file = 'data/kaggle/test.csv'

#Exploring the training dataset
#Note: For some reason, if you dont specify the encoding as latin-1, the interpreter will throw an UTF-8 encoding error
data = pd.read_csv(train_file, error_bad_lines=False, encoding='latin-1')
data.columns = ['id', 'sentiment', 'text']
print(data.head(2))
