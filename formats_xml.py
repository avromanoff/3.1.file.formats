from collections import Counter
import xml.etree.ElementTree as ET


def top_words_list():
    # ищет топ-10 из счетчика
    long_words = {}
    word_top = ''
    for x in range(10):
        word_counter = 0
        for words in cnt:
            if words not in long_words:
                if cnt.get(words) > word_counter:
                    word_top = words
                    word_counter = cnt.get(words)
        long_words[word_top] = word_counter
    return long_words


parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall("channel/item")
descriptions = []
for item in xml_items:
    description = item.find("description")
    descriptions += description.text.split(" ")


descriptions_lower = [item.lower() for item in descriptions]


cnt = Counter()
for word in descriptions_lower:
    if len(word) > 5:
        cnt[word] += 1


print(top_words_list())
