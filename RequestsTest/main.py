import requests

token = 'd3c6804a16b1471b8356ff2294dbfb3b'
host = 'https://pokemonbattle.me:9104'

answer = requests.post(f'{host}/pokemons', json = 
                        { 
    "name": "Кот Бегемот",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type": "application/json", "trainer_token": token})
print(answer.text)

answer_2 = requests.put(f'{host}/pokemons', json = 
                        { 
    "pokemon_id": "12542",
    "name": "Leo"
}, headers = {"Content-Type": "application/json", "trainer_token": token})
print(answer_2.text)

answer_3 = requests.post(f'{host}/trainers/add_pokeball', json = 
                        { 
    "pokemon_id": "12542",
}, headers = {"Content-Type": "application/json", "trainer_token": token})
print(answer_3.text)