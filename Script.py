import re
from googleapiclient.discovery import build

# Konfiguracja klienta API YouTube
def get_youtube_client():
    return build('youtube', 'v3', developerKey='TWÓJ_KLUCZ_API')

# Lista "stop words"
stop_words = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers",
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does",
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down",
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here",
    "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more",
    "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
    "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
])

# Funkcja do ekstrakcji i czyszczenia słów kluczowych z tytułu
def extract_keywords(title):
    title = re.sub(r'[^\w\s]', '', title).lower()
    words = title.split()
    keywords = [word for word in words if word not in stop_words]
    return " ".join(set(keywords))

# Funkcja do wyszukiwania filmów na podstawie słów kluczowych
def search_videos_by_keywords(keywords):
    youtube = get_youtube_client()
    response = youtube.search().list(
        part='snippet',
        q=keywords,
        type='video',
        maxResults=5
    ).execute()

    videos = []
    for item in response.get('items', []):
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        videos.append({'title': title, 'url': video_url})
    return videos

# Funkcja do ekstrakcji ID filmu z URL
def extract_video_id(url):
    regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    matches = re.search(regex, url)
    if matches:
        return matches.group(1)
    return None

# Main
if __name__ == "__main__":
    youtube_url = "TUTAJ_WPISZ_LINK_DO_FILMIKU"  # Wprowadź link do filmu YouTube
    video_id = extract_video_id(youtube_url)
    youtube = get_youtube_client()
    
    if video_id:
        response = youtube.videos().list(part='snippet', id=video_id).execute()
        if response['items']:
            title = response['items'][0]['snippet']['title']
            keywords = extract_keywords(title)
            print(f"Słowa kluczowe: {keywords}")
            related_videos = search_videos_by_keywords(keywords)
            print("Podobne filmy:")
            for video in related_videos:
                print(f"{video['title']}: {video['url']}")
        else:
            print("Film nie został znaleziony.")
    else:
        print("Nieprawidłowy URL filmu.")
