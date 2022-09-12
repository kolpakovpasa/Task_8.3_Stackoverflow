import requests
import time
from pprint import pprint


def get_questions(days):
    url = 'https://api.stackexchange.com/2.3/questions/'
    date = int(time.time()) - days*24*60*60
    resume = True
    page_number = 1
    question_number = 1
    while resume:
        print(f'page number: {page_number}')
        params = {'page': f'{page_number}', 'fromdate': f'{date}', 'order': 'desc', 'sort': 'activity', 'tagged': 'python', 'site': 'stackoverflow'}
        response = requests.get(url, params=params)
        questions = response.json()
        if questions.get('items'):
            for element in questions.get('items'):
                print(f'{question_number}.', element.get('title'), end='\n\n')
                question_number += 1
        if not questions.get('has_more'):
            resume = False
        page_number += 1


if __name__ == '__main__':
    get_questions(1)






