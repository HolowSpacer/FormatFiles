import xml.etree.ElementTree as ET
from pprint import pprint

def pop_news(doc):        #Создание словаря key = слова, value = их количество в тексте
    values = {}
    for item in doc:
        for word in item.text.split():
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

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("documents/newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall('channel/item/description')

pprint(sort_news(pop_news(xml_items)))