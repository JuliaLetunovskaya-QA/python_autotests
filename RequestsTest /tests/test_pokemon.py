import requests
import pytest

token = 'd3c6804a16b1471b8356ff2294dbfb3b'
host = 'https://pokemonbattle.me:9104'

def test_status_code():
    answer = requests.get(f'{host}/trainers')
    assert answer.status_code == 200

def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers', params = {'trainer_id' : 4618})
    assert answer_body.json()['trainer_name'] == 'Юлия'
   