from plexapi.myplex import MyPlexAccount
import os

artistToSearch = input('Artist: ')
albumToSearch = input('Album: ')

account = MyPlexAccount(PLEX_USER, PLEX_PASSWORD)
plex = account.resource(PLEX_SERVER).connect()
music = plex.library.section(PLEX_LIBRARY)
playlist = music.playlist(PLEX_PLAYLIST)

for track in os.listdir(ROOT_DIRECTORY\\'+artistToSearch+'\\'+albumToSearch):
    track = track.lower().replace(albumToSearch + ' - ' + artistToSearch + ' - ', '').replace('.mp3','').lstrip('01234567879.- ')
    try:
        playListTrack = playlist.item(track)
        if(playListTrack is not None and playListTrack.grandparentTitle.lower() == artistToSearch):
            print(track)
    except:
        pass
