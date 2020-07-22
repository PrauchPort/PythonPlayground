from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

sub = Subscriber('asd@gmail.com', '2020-07-22')

print(sub.addr)
print(sub.joined)
