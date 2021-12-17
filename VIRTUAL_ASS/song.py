import pandas as pd
from speech_recognition import Recognizer, Microphone, UnknownValueError
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

######################## USER CONFIGURATION  ########################
#setup = pd.read_csv("spotify.txt",sep = "=", index_col = 0, squeeze = True, header = None)
client_id = "675feac1a4d44c5e866f895a6a085965"
client_secret = "a1cfadc3fa0e49f3b82c3ac6b799f08"
device_name = "pop-os"
redirect_uri = "https://example.com/callback/"
scope = "read-private user-read-playback-state user-modify-playback-state"
username = "31mowu4sdws7rnyfhaaybysrbhwq"

auth_manager = SpotifyOAuth(
    client_id = client_id,
    client_secret = client_secret,
    redirect_uri = redirect_uri,
    scope = scope,
    username = username
)
spotify = sp.Spotify(auth_manager = auth_manager)

devices = spotify.devices()
deviceID = None
for d in devices["devices"]:
    d["name"] = d["name"].replace("'","\'")
    if d["name"] == device_name:
        deviceID = d["id"]
        break


class InvalidSearchError(Exception):
    pass

def get_album_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: album name
    :return: Spotify uri of the desired album
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='album')
    if not results['albums']['items']:
        raise InvalidSearchError(f'No album named "{original}"')
    album_uri = results['albums']['items'][0]['uri']
    return album_uri


def get_artist_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: album name
    :return: Spotify uri of the desired artist
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='artist')
    if not results['artists']['items']:
        raise InvalidSearchError(f'No artist named "{original}"')
    artist_uri = results['artists']['items'][0]['uri']
    print(results['artists']['items'][0]['name'])
    return artist_uri


def get_track_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: track name
    :return: Spotify uri of the desired track
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='track')
    if not results['tracks']['items']:
        raise InvalidSearchError(f'No track named "{original}"')
    track_uri = results['tracks']['items'][0]['uri']
    return track_uri


def play_album(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, context_uri=uri)


def play_artist(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, context_uri=uri)


def play_track(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, uris=[uri])


################################# INPUT ##################################33
r = Recognizer()
m = Microphone()
done = False

while not done:
    command = None
    try:
        with m as source:
            r.adjust_for_ambient_noise(source)
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()
    except UnknownValueError:
        continue
    print(command)
    words = command.split()
    if len(words) <= 1:
        print('could not understand, please try again')
        continue

    name = " ".join(words[1:])
    try:
        if words[0] == 'album':
            uri = get_album_uri(spotify=spotify, name=name)
            play_album(spotify=spotify, device_id=deviceID, uri=uri)
        elif words[0] == 'artist':
            uri = get_artist_uri(spotify=spotify, name=name)
            play_artist(spotify=spotify, device_id=deviceID, uri=uri)
        elif words[0] == 'play':
            uri = get_track_uri(spotify=spotify, name=name)
            play_track(spotify=spotify, device_id=deviceID, uri=uri)
        else:
            print('Specify either "album", "artist" or "play". Try Again')
    except InvalidSearchError:
            print('InvalidSearchError. Try Again')