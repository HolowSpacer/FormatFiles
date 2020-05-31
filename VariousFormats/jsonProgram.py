import json
from pprint import pprint

def pop_news(doc):       #Создание словаря key = слова, value = их количество в тексте
    values = {}
    for descriptions in (doc['rss']['channel']['items']):
        for word in descriptions['description'].split():
            if len(word) > 6:
                if values.get(word):
                    values[word] += 1
                else:
                    values[word] = 1
    return values

def sort_news(news):      #Сортировка словаря и создание списка топ-10
    list_dict_words = list(news.items())
    sort_dict_list_words = sorted(list_dict_words, key=lambda i: i[1], reverse=True)
    top_words = []
    for i in range(10):
        top_words.append(sort_dict_list_words[i])
    return top_words


with open("documents/newsafr.json", encoding= "utf-8") as f:
    data = json.load(f)
    pprint(sort_news(pop_news(data)))
