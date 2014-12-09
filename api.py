#encoding=utf-8
import pylast
import codecs

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm
API_KEY = "30403a0785018d89df9b3d2afef47187"
API_SECRET = "429be11fda61b668164b35bc51d31a83"

# In order to perform a write operation you need to authenticate yourself
username = "liwang0513"
password_hash = pylast.md5("*******")

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
    API_SECRET, username = username, password_hash = password_hash)
    

file = codecs.open('Data.txt', 'w+', 'utf-8')

artists = network.get_top_artists(1000)
for artist in artists:
    artist_name = artist.item.get_name()
    file.write(artist_name+'\t')
    
    artist_info = network.get_artist(artist_name)
    tags = artist_info.get_top_tags(limit=10)
    
    for tag in tags:
        file.write(tag.item.get_name()+'\t')
    
    file.write('\n')
