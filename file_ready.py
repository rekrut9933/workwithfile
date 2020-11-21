import os
import re


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words






def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict



def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        longest = max(words, key=len)
        smallest = min(words, key=len)
        print("Кол-во слов: %d" % len(words))
        print("Кол-во уникальных слов: %d" % len(words_dict))
        print("Наибольшее слово: ", longest)
        print("Наименьшее слово: ", smallest)
        print("Все уникальные слова:")

        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()