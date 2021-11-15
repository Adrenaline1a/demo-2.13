#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(pattern):
    def wrapper(firstname, lastname):
        first = firstname
        lst = lastname
        return pattern.format(firstname=first, lastname=lst)
    return wrapper
