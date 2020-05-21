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

def distribution_check(feature):
    value_differential = 0

def statistic_measure(dataset):
    for column in zip(*dataset):
        distribution_type = distribution_check(column)
        