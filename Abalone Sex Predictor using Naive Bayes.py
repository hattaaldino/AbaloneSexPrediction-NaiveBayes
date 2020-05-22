# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:15:12 2020

@author: hattaldino
"""

from csv import reader
from math import sqrt
from math import exp
from math import pi

file = "abalone_original.csv"

# load data from csv file
def load_data(file):
    attribute = list()
    dataset = list()
    data_count = 0
    with open(file,'r') as abalone_data:
        data_reader = reader(abalone_data)
        for row in data_reader:
            if not row:
                continue
            if data_count == 0:
                attribute = row
                data_count += 1
            else:
                dataset.append(row)
                data_count += 1
    data_count -= 1
    data = [attribute, dataset, data_count]
    return data

def separate_by_class(dataset):
    separated_data = dict()
    for row in dataset:
        label = row[0]
        value = row.remove[0]
        if label not in separated_data:
            separated_data[label] = list()
        separated_data[label].append(value)
    return separated_data

def mean(feature):
    return sum(feature)/float(len(feature))

def stdv(feature, mean):
    variance = sum([(x - mean)**2 for x in feature])/float(len(feature)-1)
    return sqrt(variance)

def occurence(feature):
    condition = dict()
    for cell in feature:
        condition[cell] += 1
    return condition

def distribution_check(feature):
    if type(feature[0]) == int or float:
        return 'continuous'
    else:
        return 'discrete'

def statistic_measure(dataset):
    statistic = list()
    for column in zip(*dataset):
        distribution_type = distribution_check(column)
        if distribution_type == 'continuous':
            avg = mean(column)
            dev = stdv(column, mean)
            summarize = [avg, dev, len(column)]
            statistic.append(summarize)
        elif distribution_type == 'discrete':
            summarize = [occurence(column), len(column)]
            statistic.append(summarize)
    return statistic

def statistic_by_class(dataset):
    separated = separate_by_class(dataset)
    statistic = dict()
    for class_label, row in separated.items():
        statistic[class_label] = statistic_measure(row)
    return statistic
    
            
            
        