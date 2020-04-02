# -*- coding: utf-8 -*-
class colors:
    HEADER = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    UNDERLINE = '\033[4m'

def header(text):
    return colors.HEADER+str(text)+colors.end

def blue(text):
    return colors.blue+str(text)+colors.end

def green(text):
    return colors.green+str(text)+colors.end

def yellow(text):
    return colors.yellow+str(text)+colors.end

def red(text):
    return colors.red+str(text)+colors.end

def bold(text):
    return colors.bold+str(text)+colors.end

def underline(text):
    return colors.UNDERLINE+str(text)+colors.end
