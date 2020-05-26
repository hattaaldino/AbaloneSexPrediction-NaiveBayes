# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:15:12 2020

@author: hattaldino
"""

from csv import reader
from math import sqrt
from math import exp
from math import pi

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

# Split dataset by class
def separate_by_class(dataset):
    separated_data = dict()
    for row in dataset:
        label = row[0]
        value = row[1:]
        if label not in separated_data:
            separated_data[label] = list()
        separated_data[label].append(value)
    return separated_data

#Convert all feature values into float
def convert(dataset):
    convert_data = list()
    for data in dataset:
        convert_data.append(float(data))
    return convert_data

# Calculate the mean (average) of feature
def mean(feature):
    return (sum(feature) / float(len(feature)))

# Calculate the Standard Deviation of feature
def stdv(feature, mean):
    variance = sum([(x - mean)**2 for x in feature]) / float(len(feature)-1)
    return (sqrt(variance))

# Quantify the occurence of feature categories in each class
def occurence(feature):
    condition = dict()
    for cell in feature:
        condition[cell] += 1
    return condition

# Check the distribution type of value
def distribution_check(value):
    if type(value) == int or float:
        return 'continuous'
    else:
        return 'discrete'

# Calculate the statistic for each column in a dataset
def statistic_measure(dataset):
    statistic = list()
    for column in zip(*dataset):
        distribution_type = distribution_check(column)
        if distribution_type == 'continuous':
            convert_column = convert(column)
            avg = mean(convert_column)
            dev = stdv(convert_column, avg)
            summarize = [len(column), avg, dev]
            statistic.append(summarize)
        elif distribution_type == 'discrete':
            summarize = [len(column), occurence(column)]
            statistic.append(summarize)
        else:
            statistic.append(None)
    return statistic

# Split dataset by class then calculate statistics for each class
def statistic_by_class(dataset):
    separated = separate_by_class(dataset)
    statistic = dict()
    for class_label, row in separated.items():
        statistic[class_label] = statistic_measure(row)
    return statistic

# Calculate the probability of discrete value
def discrete_probability(value, occurence, count):
    counted_value = occurence[value]
    return (counted_value / count)

# Calculate the probability of continuous value with Gaussian PDF
def continuous_probability(value, mean, stdv):
    exponent = exp(-((value - mean)**2 / (2 * stdv**2)))
    return (1 / (sqrt((2 * pi) * (stdv**2)))) * exponent

# Calculate the probabilities for each class
def class_probability(statistic, row, total):
    probabilities = dict()
    for class_value, class_statistic in statistic.items():
        probabilities[class_value] = class_statistic[0][0] / float(total)
        for i in range(len(class_statistic)):
            value = row[i]
            value_type = distribution_check(value)
            if value_type == 'continuous':
                _, mean, stdv = class_statistic[i]
                probabilities[class_value] *= continuous_probability(value, mean, stdv)
            elif value_type == 'discrete':
                count, occurence = class_statistic[i]
                probabilities[class_value] *= discrete_probability(value, occurence, count)
    return probabilities

# Determine the class for given value
def classifier(probabilities):
    best_class, best_prob = None, -1
    for class_value, class_prob in probabilities.items():
        if class_prob > best_prob:
            best_prob = class_prob
            best_class = class_value
    predict = best_class
    return predict

file = "abalone_original.csv"
attribute, dataset, count = load_data(file)
statistic = statistic_by_class(dataset)

new_row = list()
print("------------ Abalone Sex Classification ------------\n")
print("Masukan Nilai Atribut")
for x in attribute[1:]:
    attr = x.title().replace('-', ' ')
    val = input(f'{attr} : ')
    try:
        value = float(val)
    except TypeError:
        new_row.append(0)
    except ValueError:
        while True:
            print('The input must be float/decimal!')
            fix_val = input(f'{attr} : ')
            try:
                fix_value = float(fix_val)
            except TypeError:
                new_row.append(0)
                break
            except ValueError:
                continue
            else:
                new_row.append(fix_value)
                break
    else:
        new_row.append(value)

probabilities = class_probability(statistic, new_row, count)
potent_class = classifier(probabilities)
print('\n-----Result-----\n')
print(f'Abalone Sex : {potent_class}')

input('\nPress enter to exit...')

     
            
        