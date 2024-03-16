## Opis

Skrypt  służy do znajdowania filmów na YouTube, które są podobne do podanego filmu, bazując na analizie słów kluczowych wyekstrahowanych z tytułu. 
Skrypt ekstrahuje słowa kluczowe z tytułu wybranego filmu na YouTube, usuwa z nich tzw. stop words (czyli najczęściej występujące słowa, które nie niosą znaczącej wartości),
a następnie wykorzystuje pozostałe słowa kluczowe do wyszukania i wyświetlenia listy podobnych filmów.

## Wymagania

- Python 3.x
- Biblioteka `google-api-python-client`

Przed uruchomieniem skryptu, należy zainstalować wymagane zależności komendą:

```bash
pip install google-api-python-client
```

##  Instrukcja użytkowania
- Uzyskaj klucz API dla YouTube Data API v3 poprzez Google Developer Console.
- Zastąp TWÓJ_KLUCZ_API w skrypcie swoim kluczem API.
- Uruchom skrypt, wprowadzając URL do interesującego Cię filmu na YouTube w miejscu TUTAJ_WPISZ_LINK_DO_FILMIKU
