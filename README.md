# Overview

Sentiment Analysis on Twitter data

# Step by Step Guide

- Section 1: Explore the training data set
- Section 2: Process the test data
- Section 3: Preprocessing
- Section 4: Training and Evaluation
- Section 5: Metrics and Measurements
- Section 6: Conclusion

# Machine Learning Tips

## ML Algorithm Tuning

Machine Learning Models are parameterized so that their behavior can be tuned for a given dataset.
ML models have many parameters and finding the best combination of parameters can be treated as a search problem. 

Algorithmic Tuning is the final stage before presenting the results. It is also called hyperparameter optimization, where the algorithm parameters are referred to as hyperparameters whereas the coefficients found by the machine learning algorithm itself are referred to as parameters. Optimization suggests the search-nature of the problem

Phrased as a search problem, we can use different search strategies to find a good parameter or set of parameters for an algorithm. Simple strategies are Grid Search and Random Search. 

### Grid Search

It is an approach to parameter tuning that will methodically build and evaluate a model for each combination of algo parameters specified in a grid

### Random Search

Random Search is an approach that will sample algorithm parameters from a random distribution (normal) for a fixed number of iterations. A model is constructed and evaluated for each combination of parameters chosen

# Troubleshooting:

Issue1: While reading the csv file, ran into encoding issue
Fix: Use the latin-1 encoding

Issue2: While uploading data files to git, ran into space issues
Fix: Install git large file system 
