#-*-encode:utf-8-*-
import requests
import json
import sys 

input_tags = sys.argv[1:]

if input_tags.__len__() > 0:

    tags = ";".join(input_tags)

    url = 'https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&tagged='+tags+'&site=stackoverflow'
    result_search = requests.get(url) 
    result_json = result_search.content.decode('utf8').replace("'", '"')
    data = json.loads(result_json)

    if result_search.status_code == 200:
        
        if data['items'].__len__() > 0:
            for item in data['items']:
                print('\nQuestion: {0} \nScore: {1}\nLink: {2}\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n'.format(item['title'],item['score'], item['link'] )) 
        else:
            print('nenhum resultado')

    else:
        print('Houve um problema na requisição')

else:
    print('Nenhum termo foi inserido')