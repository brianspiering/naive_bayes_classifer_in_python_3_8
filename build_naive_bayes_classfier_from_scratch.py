#!/usr/bin/env python
# coding: utf-8

""" Build a Naive Bayes Classifer from scratch in Python 3.8

Source - https://docs.python.org/3/library/statistics.html#normaldist-examples-and-recipes
"""

# Double check we are using Python 3.8
from platform import python_version

assert python_version().startswith('3.8')


# What is Naive Bayes?


# Machine learning models needs data

# https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Sex_classification

from statistics import NormalDist

# Historical data

height_male      = NormalDist.from_samples([6, 5.92, 5.58, 5.92])
height_female    = NormalDist.from_samples([5, 5.5, 5.42, 5.75])
weight_male      = NormalDist.from_samples([180, 190, 170, 165])
weight_female    = NormalDist.from_samples([100, 150, 130, 150])
foot_size_male   = NormalDist.from_samples([12, 11, 12, 10])
foot_size_female = NormalDist.from_samples([6, 8, 7, 9])

# Build Naive Bayes Classifier

# Starting with a 50% prior probability of being male or female, 

prior_male, prior_female = 0.5, 0.5

# New person

ht = 6.0        # height
wt = 130        # weight
fs = 8          # foot size

# We compute the posterior as the prior times the product of likelihoods for the feature measurements given the gender:

posterior_male = (prior_male * 
                 height_male.pdf(ht) *
                 weight_male.pdf(wt) * 
                 foot_size_male.pdf(fs))

posterior_female = (prior_female * 
                   height_female.pdf(ht) *
                   weight_female.pdf(wt) * 
                   foot_size_female.pdf(fs))


# Prediction

# The final prediction goes to the largest posterior. 
# This is known as the maximum a posteriori or MAP:
prediction = 'male' if posterior_male > posterior_female else 'female'
print(prediction)


# Summary
