import argparse

import requests

from bs4 import BeautifulSoup


url = "https://www.fip.fr/"
req = requests.get(url).text
soup = BeautifulSoup(req, "lxml")


class Song:
    def __init__(self, title, artist, album="", label=""):
        self.title = title
        self.artist = artist
        self.album = album
        self.label = label

    def __str__(self):
        # if not self.album ....
        return "Title: % s \nArtist: % s \nAlbum: % s \nLabel: % s \n" % (
            self.title,
            self.artist,
            self.album,
            self.label,
        )


def get_current_song():
    current_title = soup.find_all("span", class_="now-info-title")[0].get_text()
    current_artist = soup.find_all("span", class_="now-info-subtitle")[0].get_text()
    current_album = soup.find_all("span", class_="now-info-details-value")[0].get_text()
    current_label = soup.find_all("span", class_="now-info-details-value")[1].get_text()

    return Song(current_title, current_artist, current_album, current_label)


def get_next_song():
    next_song_info = soup.find_all("div", class_="history-list-item-info")[2].contents
    next_title = next_song_info[1].get_text()
    next_artist = next_song_info[2].get_text()

    return Song(next_title, next_artist)


def get_previous_songs():
    previous_songs_info = soup.find_all("div", class_="history-list-item-info")[:2]
    previous_songs = []

    for previous_song in previous_songs_info:
        previous_song_info = previous_song.contents
        previous_title = previous_song_info[1].get_text()
        previous_artist = previous_song_info[2].get_text()
        previous_songs.append(Song(previous_title, previous_artist))

    return previous_songs


def output_current():
    song = get_current_song()
    print(song)


def output_next():
    song = get_next_song()
    print(song)


def output_previous():
    songs = get_previous_songs()
    for song in songs:
        print(song)


def output_playlist():
    print("=!= Current =!=")
    output_current()
    print("\n=!= Next =!=")
    output_next()
    print("\n=!= Previous =!=")
    output_previous()


# output_playlist()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--current", help="display current song", action="store_true"
    )
    parser.add_argument("-n", "--next", help="display next song", action="store_true")
    parser.add_argument(
        "-p", "--previous", help="display previous song", action="store_true"
    )
    args = parser.parse_args()

    if args.current:
        output_current()
    if args.next:
        output_next()
    if args.previous:
        output_previous()
