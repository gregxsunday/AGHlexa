import spotipy
import webbrowser

def play(song):
    webbrowser.open('spotify:search:{}'.format(song))