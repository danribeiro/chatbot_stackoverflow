import requests

def call_stackoverflow_api(tags):
    """Return the list of answers for questions that contains the inputed tags"""
    
    headers = {'content-type':'application/json'}
    url = 'https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&tagged='+tags+'&site=stackoverflow'
    result_search = requests.get(url, headers=headers) 
    data_json = result_search.json()
    
    if result_search.status_code == 200:
        return data_json
    return None