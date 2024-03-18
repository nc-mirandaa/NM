class Playlist(object):
    
    def __init__(self,id,name,description,creator,tracks):
        self.id=id
        self.name=name
        self.description=description
        self.creator=creator
        self.tracks=tracks

    def show_attr(self,tracks):

        tracks_playlist=""
        for id in self.tracks:
            for track in tracks:
                if id == track.id:
                    tracks_playlist=tracks_playlist+track.show_attr()+"\n"

        return "\nID: {} \nNombre: {} \nDescripcion: {} \nCreador: {} \nTracks: {} ".format(self.id,self.name,self.description,self.creator,tracks_playlist)


#hacer show_attr()

#solo tiene que aparecer las canciones sin todas sus especificaciones = name
#hacer un buscar id 