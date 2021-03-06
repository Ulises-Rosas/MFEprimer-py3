#!/usr/bin/env python
# -*- coding:utf-8 -*-

# -----------------------------------------------------
# File: CairoNumberWidth.py
# Date: 2008-07-04
# Description: 
# -----------------------------------------------------

__version__ = '1.0'
__author__ = 'Wubin Qu <quwubin@gmail.com> @ZCGLAB @BMI @CHINA'
__blog__ = 'http://quwubin.cnblogs.com'
__license__ = 'GPL'

font50 = {
    "a": 23.0,
    "b": 26.0,
    "c": 22.0,
    "d": 25.0,
    "e": 22.0,
    "f": 17.0,
    "g": 24.0,
    "h": 26.0,
    "i": 14.0,
    "j": 14.0,
    "k": 25.0,
    "l": 14.0,
    "m": 39.0,
    "n": 25.0,
    "o": 24.0,
    "p": 25.0,
    "q": 25.0,
    "r": 17.0,
    "s": 20.0,
    "t": 15.0,
    "u": 25.0,
    "v": 25.0,
    "w": 36.0,
    "x": 25.0,
    "y": 25.0,
    "z": 22.0,
    "0": 25.0,
    "1": 26.0,
    "2": 25.0,
    "3": 25.0,
    "4": 25.0,
    "5": 25.0,
    "6": 25.0,
    "7": 25.0,
    "8": 26.0,
    "9": 25.0,
    "A": 36.0,
    "B": 34.0,
    "C": 33.0,
    "D": 36.0,
    "E": 30.0,
    "F": 28.0,
    "G": 36.0,
    "H": 35.0,
    "I": 16.0,
    "J": 19.0,
    "K": 36.0,
    "L": 30.0,
    "M": 44.0,
    "N": 36.0,
    "O": 37.0,
    "P": 28.0,
    "Q": 37.0,
    "R": 33.0,
    "S": 28.0,
    "T": 30.0,
    "U": 36.0,
    "V": 36.0,
    "W": 47.0,
    "X": 36.0,
    "Y": 36.0,
    "Z": 31.0,
    "_": 25.0,
    "-": 16.0,
    "|": 9.0,
    "!": 16.0,
    "@": 47.0,
    "#": 27.0,
    "$": 25.0,
    "%": 41.0,
    "^": 23.0,
    "&": 39.0,
    "*": 26.0,
    "(": 16.0,
    ")": 17.0,
    "+": 28.0,
    "[": 17.0,
    "]": 16.0,
    "{": 24.0,
    "}": 24.0,
    ":": 14.0,
    '"': 21.0,
    ";": 14.0,
    "'": 9.0,
    "\\": 14.0,
    ",": 13.0,
    ".": 12.0,
    "/": 14.0,
    "?": 22.0,
    ">": 28.0,
    "<": 28.0,
}

font30 = {
    " ": 14.0,
    "a": 14.0,
    "b": 15.0,
    "c": 13.0,
    "d": 15.0,
    "e": 14.0,
    "f": 10.0,
    "g": 15.0,
    "h": 15.0,
    "i": 8.0,
    "j": 9.0,
    "k": 16.0,
    "l": 9.0,
    "m": 24.0,
    "n": 15.0,
    "o": 15.0,
    "p": 15.0,
    "q": 15.0,
    "r": 10.0,
    "s": 12.0,
    "t": 8.0,
    "u": 15.0,
    "v": 15.0,
    "w": 22.0,
    "x": 15.0,
    "y": 15.0,
    "z": 13.0,
    "0": 15.0,
    "1": 15.0,
    "2": 15.0,
    "3": 15.0,
    "4": 16.0,
    "5": 14.0,
    "6": 15.0,
    "7": 15.0,
    "8": 15.0,
    "9": 15.0,
    "A": 22.0,
    "B": 19.0,
    "C": 20.0,
    "D": 21.0,
    "E": 19.0,
    "F": 17.0,
    "G": 21.0,
    "H": 21.0,
    "I": 9.0,
    "J": 12.0,
    "K": 22.0,
    "L": 18.0,
    "M": 26.0,
    "N": 21.0,
    "O": 21.0,
    "P": 17.0,
    "Q": 21.0,
    "R": 20.0,
    "S": 17.0,
    "T": 19.0,
    "U": 21.0,
    "V": 22.0,
    "W": 28.0,
    "X": 22.0,
    "Y": 21.0,
    "Z": 19.0,
    "_": 15.0,
    "-": 9.0,
    "|": 6.0,
    "!": 10.0,
    "@": 27.0,
    "#": 17.0,
    "$": 15.0,
    "%": 25.0,
    "^": 14.0,
    "&": 23.0,
    "*": 15.0,
    "(": 10.0,
    ")": 10.0,
    "+": 17.0,
    "[": 11.0,
    "]": 10.0,
    "{": 15.0,
    "}": 15.0,
    ":": 8.0,
    '"': 12.0,
    ";": 8.0,
    "'": 5.0,
    "\\": 8.0,
    ",": 8.0,
    ".": 7.0,
    "/": 8.0,
    "?": 14.0,
    ">": 17.0,
    "<": 17.0,
}

font20 = {
    " ": 9.0,
    "a": 9.0,
    "b": 10.0,
    "c": 9.0,
    "d": 11.0,
    "e": 9.0,
    "f": 7.0,
    "g": 11.0,
    "h": 9.0,
    "i": 6.0,
    "j": 6.0,
    "k": 10.0,
    "l": 6.0,
    "m": 16.0,
    "n": 11.0,
    "o": 10.0,
    "p": 11.0,
    "q": 10.0,
    "r": 7.0,
    "s": 8.0,
    "t": 5.0,
    "u": 10.0,
    "v": 10.0,
    "w": 14.0,
    "x": 10.0,
    "y": 10.0,
    "z": 9.0,
    "0": 11.0,
    "1": 10.0,
    "2": 10.0,
    "3": 10.0,
    "4": 11.0,
    "5": 10.0,
    "6": 10.0,
    "7": 10.0,
    "8": 10.0,
    "9": 11.0,
    "A": 14.0,
    "B": 12.0,
    "C": 14.0,
    "D": 15.0,
    "E": 12.0,
    "F": 12.0,
    "G": 15.0,
    "H": 14.0,
    "I": 6.0,
    "J": 8.0,
    "K": 14.0,
    "L": 12.0,
    "M": 17.0,
    "N": 14.0,
    "O": 14.0,
    "P": 11.0,
    "Q": 14.0,
    "R": 13.0,
    "S": 10.0,
    "T": 12.0,
    "U": 14.0,
    "V": 14.0,
    "W": 19.0,
    "X": 14.0,
    "Y": 14.0,
    "Z": 13.0,
    "_": 10.0,
    "-": 7.0,
    "|": 4.0,
    "!": 7.0,
    "@": 18.0,
    "#": 12.0,
    "$": 10.0,
    "%": 16.0,
    "^": 9.0,
    "&": 16.0,
    "*": 10.0,
    "(": 7.0,
    ")": 7.0,
    "+": 12.0,
    "[": 7.0,
    "]": 7.0,
    "{": 10.0,
    "}": 10.0,
    ":": 6.0,
    '"': 8.0,
    ";": 6.0,
    "'": 4.0,
    "\\": 6.0,
    ",": 5.0,
    ".": 4.0,
    "/": 6.0,
    "?": 9.0,
    ">": 12.0,
    "<": 12.0,
}
