import pandas as pd
import numpy as np

train_file = 'data/train.csv'
test_file = 'data/test.csv'

#Explore the training dataset
#Note: For some reason, if you dont specify the encoding as latin-1, the interpreter will throw an UTF-8 encoding error
data = pd.read_csv(train_file, error_bad_lines=False, encoding='latin-1')
data.columns = ['id', 'sentiment', 'text']
print(data.head(2), "\n\n")

#Id information is not useful. So let's remove it
#axis=1 indicates columns
data = data.drop(labels=['id'], axis=1)
print(data.head(10), "\n\n")

'''
Observations:
1. Data has a mix of alphabets, numbers and symbols
2. Mix of words with uppercase and lowercase letters
3. We need to normalize the words to their base word. Leaving capitalizaed words in the middle of the tweet can be
   experimented with as they may hold different feature space like name of the person, country, etc.. 
4. No particular order of sentiment and tweets. If data is not randomly distributed then it can introduce bias to a learning model
5. Need to split and shuffle the data to reduce variance (makes sure the model can generalize better on the data) 
   and does not lead to overfitting 
6. Need to get an idea of the distribution of data
'''

#calculate the number of positive and negative tweets
positives = data['sentiment'][data.sentiment == 1]
negatives = data['sentiment'][data.sentiment == 0]

print('Number of postive tweets {}' .format(len(positives)))
print('Number of negative tweets {}' .format(len(negatives)))
print('Total Length of the data is: {}' .format(data.shape[0]))

#Are there any duplicates in the data? Get the unique counts to identify this
print(data.groupby('sentiment').describe())
