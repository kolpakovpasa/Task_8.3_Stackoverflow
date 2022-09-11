import requests
import time


def get_questions(days):
    url = 'https://api.stackexchange.com/2.3/questions/'
    date = int(time.time()) - days*24*60*60
    params = {'fromdate': f'{date}', 'order': 'desc', 'sort': 'activity', 'tagged': 'python', 'site': 'stackoverflow'}
    response = requests.get(url, params=params)
    questions = response.json()

    for element in questions.get('items'):
        print(element.get('title'), end='\n\n')


if __name__ == '__main__':
    get_questions(2)






