import re


def top_3_words(text):
    elements = {}  # key = word value =how meny time times is used
    pattern = r"[^a-z^']"  # Regex pattern to mark unnecessary elements
    text = text.lower()  # The result should be lowercase, so we do the hole text lowercase
    my_list = re.split(pattern, text)  # Split the text by regex pattern, add result to list

    for element in my_list:
        if element == "" or element == "'" or element == "'''":
            continue
        if element not in elements:
            elements[element] = 1
        else:
            elements[element] += 1
    dd = [k for k, v in sorted(elements.items(), key=lambda item: item[1], reverse=True)][:3]
    return dd


print(top_3_words("a a a  b  c c  d d d d  e e e e e"))  # ["e", "d", "a"]
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))  # ["e", "ddd", "aa"]
print(top_3_words("  //wont won't won't "))  # ["won't", "wont"]
print(top_3_words("  , e   .. "))  # ["e"]
print(top_3_words(" '  ''' "))  # []
print(top_3_words("____"))  # []
print(top_3_words(""""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))  # ["a", "of", "on"]


