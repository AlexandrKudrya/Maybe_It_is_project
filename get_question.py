import csv

import requests
from bs4 import BeautifulSoup, GuessedAtParserWarning
import wikipedia


def get_page(random):
    result = wikipedia.summary(random, sentences=2)
    return result.split(' — ')[1].lower().capitalize().split("\n")[0]



def random_calling():
    quesion = wikipedia.random(1)
    print(quesion, len(str(quesion).split()))
    if len(str(quesion).split()) == 1:
        return str(quesion)
    else:
        return random_calling()

def get_question():
    wikipedia.set_lang('ru')
    call = random_calling()
    try:
        if all(i.isalpha() for i in call) and ord(call[0]) > 1000:
            return [call.lower().capitalize(), get_page(call)]
        else:
            return get_question()
    except:
        return get_question()

print(ord('а'))
with open('questions.csv', mode='w', encoding='utf-8') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for _ in range(10):
        question = get_question()
        print([_] + question)
        writer.writerow(question)
