import json
import requests

url='http://127.0.0.1:8000/api/'

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=url,data=json_data)
    data=r.json()
    print(data)


def post_data():
    data={
    'id':1,
    'movie_name':'The Incredible Hulk',
    'release_year' : 2008,
    'rating': 4.5,
    }
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)

def update_data():
    data={
        'id':2,
        'movie_name':'Iron man',
        'release_year' : 2008,
        'rating': 4.5,
    }
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)

def delete_data():
    data={
        'id':4,
    }
    json_data=json.dumps(data)
    r=requests.delete(url=url,data=json_data)
    data=r.json()
    print(data)


#post_data()
get_data()