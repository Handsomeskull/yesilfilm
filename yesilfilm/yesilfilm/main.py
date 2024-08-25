import webbrowser
import sys

FILMLER = {
    "Kemal Sunal Filmleri": {
        5: "https://www.example.com/film5",  # Kemal Sunal filmi 5
        6: "https://www.example.com/film6",  # Kemal Sunal filmi 6
        7: "https://www.example.com/film7",  # Kemal Sunal filmi 7
        8: "https://www.example.com/film8",  # Kemal Sunal filmi 8
        9: "https://www.example.com/film9",  # Kemal Sunal filmi 9
    },
    "Türkan Şoray Filmleri": {
        10: "https://www.example.com/film10",  # Türkan Şoray filmi 10
        11: "https://www.example.com/film11",  # Türkan Şoray filmi 11
        12: "https://www.example.com/film12",  # Türkan Şoray filmi 12
        13: "https://www.example.com/film13",  # Türkan Şoray filmi 13
        14: "https://www.example.com/film14",  # Türkan Şoray filmi 14
    },
    "Şener Şen Filmleri": {
        15: "https://www.example.com/film15",  # Şener Şen filmi 15
        16: "https://www.example.com/film16",  # Şener Şen filmi 16
        17: "https://www.example.com/film17",  # Şener Şen filmi 17
        18: "https://www.example.com/film18",  # Şener Şen filmi 18
        19: "https://www.example.com/film19",  # Şener Şen filmi 19
    },
    "Diğer Filmler": {
        20: "https://www.example.com/film20",  # Diğer film 20
        21: "https://www.example.com/film21",  # Diğer film 21
        22: "https://www.example.com/film22",  # Diğer film 22
        23: "https://www.example.com/film23",  # Diğer film 23
        24: "https://www.example.com/film24",  # Diğer film 24
    },
}

def film_secimi():
    print("Yeşilçam Filmleri Seçim Sistemi")
    print("=============================")
    
    film_listesi = []
    for kategori, filmler in FILMLER.items():
        print(f"\nKategori: {kategori}")
        for numara, url in filmler.items():
            print(f"{numara}. Film {numara}")
            film_listesi.append(numara)
    
    while True:
        try:
            secim = int(input("\nBir film numarası seçin: "))
            if secim in film_listesi:
                break
            else:
                print("Geçersiz seçim. Lütfen geçerli bir numara girin.")
        except ValueError:
            print("Lütfen geçerli bir numara girin.")
    
    url = None
    for filmler in FILMLER.values():
        if secim in filmler:
            url = filmler[secim]
            break
    
    if url:
        print(f"\nSeçilen film: {secim}. Film {secim}")
        print(f"URL: {url}")
        webbrowser.open(url)
    else:
        print("Seçilen film bulunamadı.")

if __name__ == "__main__":
    film_secimi()
