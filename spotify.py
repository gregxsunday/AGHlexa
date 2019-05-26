import spotipy
import webbrowser

#WAKEWORD spotify @song
def play(song):
    webbrowser.open('spotify:search:{}'.format(song))