#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import datasets
import matplotlib.pyplot as plt

if __name__ == '__main__':

    digits = datasets.load_digits()
    print(digits.keys())
    print(digits.target[10])
    plt.imshow(digits.images[10], cmap=plt.cm.gray_r, interpolation='nearest')
    plt.savefig('./output_digit.pdf')