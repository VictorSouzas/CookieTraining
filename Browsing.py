# -*- coding: utf-8 -*-


import requests


class Browsing(object):
    """doc string for Browsing"""

    def __init__(self):
        super(Browsing, self).__init__()
        self.session = requests.Session()

    def start(self):
        google = self.session.get('http://www.google.com')
        if google.status_code is 200:
            cookies = google.cookies


if __name__ == "__main__":
    browser = Browsing()
    browser.start()
