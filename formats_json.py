from collections import Counter
import json


def top_words_list():
    # ищет топ-10 из счетчика
    long_words = []
    word_top = ''
    for x in range(10):
        word_counter = 0
        for words in cnt:
            if words not in long_words:
                if cnt.get(words) > word_counter:
                    word_top = words
                    word_counter = cnt.get(words)
        long_words.append(word_top)
    return long_words


with open('newsafr.json', encoding='utf-8') as datafile:
    json_data = json.load(datafile)


item_json = json_data.get('rss').get('channel').get('items')
descriptions = []
for news in item_json:
    descriptions += news.get('description').split(' ')


# description_sort = sorted(descriptions)


cnt = Counter()
for word in descriptions:
    if len(word) > 5:
        cnt[word] += 1


print(top_words_list())
