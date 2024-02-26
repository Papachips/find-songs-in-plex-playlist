from plexapi.server import PlexServer
import os
from prettytable import PrettyTable

baseurl = PLEX_SERVER_IP_WITH_PORT
token = PLEX_TOKEN
plex = PlexServer(baseurl, token)
music = plex.library.section(PLEX_LIBRARY)
plexPlaylist = music.playlist(PLAYLIST_NAME)

t = PrettyTable(['Track', 'Album'])

def menu():
    print('1. Search Playlist\n2. Backup Playlist')
    choice = input('Selection: ')
    if(choice == '1'):
        search()
    if(choice == '2'):
        backupPlaylist()
        print('Backup complete at PATH_TO_FILE')
    menu()


def backupPlaylist():
    f = open(PATH_TO_FILE, 'w', encoding="utf-8")
    playlist = plexPlaylist.items()
    for item in playlist:
        f.write(item.grandparentTitle + ' - ' + item.title +'\n')
    f.close

def search():
    artistToSearch = input('Artist: ')
    searchAll = input('Search All? ')
    if(searchAll == 'n'):
        albumToSearch = input('Album: ')

        for track in os.listdir('X:\\'+artistToSearch+'\\'+albumToSearch):
            track = track.lower().replace('’',"'").replace(albumToSearch + ' - ' + artistToSearch + ' - ', '').replace('.mp3','').lstrip('01234567879.- ')
            try:
                playListTrack = plexPlaylist.item(track.replace("'","’"))
                if(playListTrack is not None and playListTrack.grandparentTitle.lower() == artistToSearch):
                    print(track)
            except:
                pass
    else:
        albums = os.listdir('X:\\'+artistToSearch)
        for album in albums:
            dir = os.listdir('X:\\'+artistToSearch+'\\'+album)
            tracksAdded = 0
            for track in dir:
                track = track.lower().replace('’',"'").replace(album.lower() + ' - ' + artistToSearch + ' - ', '').replace('.mp3','').lstrip('01234567879.- ')
                try:
                    playListTrack = plexPlaylist.item(track.replace("'","’"))
                    if(playListTrack is not None):
                        if(playListTrack.grandparentTitle.lower() == artistToSearch):
                            tracksAdded += 1
                            t.add_row([track.title(), album])

                        #this handles duplicate song names from different artists
                        else:
                            allSongs = certifiedBangers.items()
                            for song in allSongs:
                                if(song.title.lower() == track and song.grandparentTitle.lower() == artistToSearch):
                                    tracksAdded += 1                          
                                    t.add_row([track.title(), album])
                                                                  
                except:
                    pass

            if(tracksAdded == 0):
                t.add_row(['', album], divider=True)
            else:
                t.add_row(['',''], divider=True)
    print(t)
    t.clear_rows()
    menu()

menu()
