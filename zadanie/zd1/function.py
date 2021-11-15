#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(pattern):
    def wrapper(firstname, lastname):
        return pattern.format(firstname=firstname, lastname=lastname)
    return wrapper
