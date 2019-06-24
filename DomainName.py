## https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python

import unittest

def domain_name(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('.')[0]

test = unittest.TestCase()

test.assertEquals(domain_name("http://google.com"), "google")
test.assertEquals(domain_name("http://google.co.jp"), "google")
test.assertEquals(domain_name("www.xakep.ru"), "xakep")
test.assertEquals(domain_name("https://youtube.com"), "youtube")