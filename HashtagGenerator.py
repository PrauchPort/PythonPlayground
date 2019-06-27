## https://www.codewars.com/kata/the-hashtag-generator/train/python

import unittest


def generate_hashtag(s):
    final = "#" + ''.join([item.capitalize() for item in s.split()])
    return final if len(final) <= 140 and s != '' else False


test = unittest.TestCase()


test.assertEquals(generate_hashtag(''), False, 'Expected an empty string to return False')
test.assertEquals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
test.assertEquals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
test.assertEquals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
test.assertEquals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
test.assertEquals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
test.assertEquals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
test.assertEquals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
test.assertEquals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
test.assertEquals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')