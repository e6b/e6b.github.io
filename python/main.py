import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

client_id = '10eee56f5906469a8a1e8f6383ba25e6'
client_secret = '4e2d655b7b1145ba9bbcbb318ad6463f'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
    client_id, client_secret)
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)

# 曲の特徴 カネコアヤノ「栄えた町の」
audio_features_result = spotify.audio_features('6gma2RNOZyIAIqHchkt5K0')
pprint.pprint(audio_features_result)

# アーテイスト情報
name = 'Ayano Kaneko'
name_result = spotify.search(q='artist:' + name, type='artist')
pprint.pprint(name_result['artists'])

# 類似アーティストの取得
artist_id = name_result['artists']['items'][0]['id']
related_artists = spotify.artist_related_artists(artist_id)
for artist in related_artists['artists']:
    artist_name = artist['name']
    popularity = artist['popularity']
    genres = artist['genres']
    info = 'アーティスト名:{0} - 人気{1} ジャンル:{2}'.format(
        artist_name, popularity, genres)
    print(info)
