# -*- coding: utf-8 -*-

import requests


class Browsing(object):

    def __init__(self):
        self.session = requests.Session()


if __name__ is "__main__":
    browser = Browsing()
