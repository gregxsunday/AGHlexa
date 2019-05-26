import spotipy
import webbrowser

#WAKEWORD play @song on spotify
def play(song):
    webbrowser.open('spotify:search:{}'.format(song))