class Musique:
    def __init__(self,  album:Album, artists:Artist, duration_ms:int, explicit:bool,isrc:str,name:str):
        self.album = album
        self.artists = artists
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.isrc = isrc
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return (self.artists == other.artists and self.name == other.name) or self.isrc == other.isrc
    
    def __hash__(self):
        return hash(self.isrc)
     

class Album:
    def __init__(self, album_type, artists, available_markets, external_urls, genres, href, id, images, name, release_date, release_date_precision, total_tracks):
        pass

class Artist:
    def __init__(self, external_urls, followers, genres, href, id, images, name, popularity, type, uri):
        pass
    