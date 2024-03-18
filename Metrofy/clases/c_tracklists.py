class Track(object):
    
    def __init__(self,id,name,duration,link,artist,streams):
        self.id=id
        self.name=name
        self.duration=duration
        self.link=link
        self.artist=artist
        self.streams=streams

    def show_attr(self):
        return "\nID: {} \nNombre: {} \nDuracion: {} \nLink: {} \nStreams Tracks: {} ".format(self.id,self.name,self.duration,self.link,self.streams)


#hacer show_attr()