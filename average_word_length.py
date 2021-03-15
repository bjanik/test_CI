import re
import string

def average_word_length(s: str) -> float:
    allow = f'{string.ascii_letters}{string.digits} '
    s2 = re.sub('[^%s]' % allow, '', s)
    num_words = len(s2.split())
    if num_words == 0:
        return 0
    return (len(s2) - s2.count(" ")) / num_words
