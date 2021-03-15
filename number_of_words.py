import re
import string

def number_of_words(s: str) -> int:
    allow = f'{string.ascii_letters}{string.digits} '
    s2 = re.sub('[^%s]' % allow, '', s)
    return len(s2.split())
