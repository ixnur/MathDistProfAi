import requests
import itertools
import time
import string

def check_username(username):
    url = f'https://github.com/{username}'
    response = requests.get(url)
    return response.status_code == 404  # 404 durumu kullanıcı adının boşta olduğunu gösterir.

def generate_usernames(name):
    for length in range(1, 4):
        for combination in itertools.product(name + string.ascii_lowercase + string.ascii_uppercase + string.digits, repeat=length):
            yield ''.join(combination)

def find_available_usernames(name):
    for username in generate_usernames(name):
        print(f"Deneniyor: {username}")
        if check_username(username):
            print(f"Boşta olan kullanıcı adı bulundu: {username}")
        time.sleep(15)  # Her istek arasına 11 saniye bekletme ekleyin

if __name__ == "__main__":
    ad = "nur"  # Adınızı veya takma adınızı buraya girin
    find_available_usernames(ad)
