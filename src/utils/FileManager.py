#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from random import random

__all__ = ['parse', 'output']  # Add in the list every symbols that you want to import


def parse(path):
    with open(path) as file:
        data = []
        for row in file.read().split("\n"):
            object = []
            for col in row.strip().split(" "):
                if col.isdigit():
                    object.append(int(col))
                elif col.isdecimal():
                    object.append(float(col))
                else:
                    object.append(col)
            data.append(object)
        return data


def output(path, data):
    if not os.path.exists('./out'):
        os.makedirs('./out')

    string = ""
    with open(path, "w+") as out:
        for row in data:
            for col in row:
                string += str(col)
            string += "\n"

        out.write(string)

