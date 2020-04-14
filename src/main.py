import requests
import json
import sys 
from utils import call_stackoverflow_api

input_tags = sys.argv[1:]

if input_tags.__len__() > 0:

    tags = ";".join(input_tags)
    data = call_stackoverflow_api(tags)

    if data is not None:
        if data['items'].__len__() > 0:
            for item in data['items']:
                print('\nQuestion: {0} \nScore: {1}\nLink: {2}\n\n'.format(item['title'],item['score'], item['link'] )) 
        else:
            print('nenhum resultado')
    else:
        print('Houve um problema na requisição')
else:
    print('Nenhum termo foi inserido')