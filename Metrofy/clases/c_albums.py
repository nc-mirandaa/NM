class Album(object):

    def __init__(self,id,name,description,cover,published,genre,artist,tracklist,streams):
        self.id=id
        self.name=name
        self.description=description
        self.cover=cover
        self.published=published
        self.genre=genre
        self.artist=artist
        self.tracklist=tracklist
        self.streams=streams
    
    def show_attr(self,tracks):

        tracks_album=""
        for id in self.tracklist:
            for track in tracks:
                if id == track.id:
                    tracks_album=tracks_album+track.show_attr()+"\n"

        return "\nID: {} \nNombre: {} \nDescripcion: {} \nPortada: {} \nFecha: {} \nGenero: {} \nArtista: {} \nTracklist: {} \nStreams Album: {} ".format(self.id,self.name,self.description,self.cover,self.published,self.genre,self.artist,tracks_album,self.streams)


        
