
class User(object):

    def __init__(self,id,name,email,username,type):
        self.id=id
        self.name=name
        self.email=email
        self.username=username
        self.type=type

    def show_attr(self): #mostrar atributos
        return "\nID: {} \nNombre: {} \nEmail: {} \nUsername: {} \nTipo: {}".format(self.id,self.name,self.email,self.username,self.type)
    
    def cambiar_datos(self): #funcion cambiar datos para todo tipo de usuario
        option=int(input("\n1)Nombre \n2)Email \n3)Nombre de Usuario \nIndica que dato quieres cambiar: "))
        if option==1:
            new_name=input("Escribe tu nuevo nombre: ") 
            self.name=new_name

        elif option==2:
            new_email=input("Escribe tu nuevo email: ")
            self.email=new_email

        elif option==3:
            new_username=input("Escribe tu nuevo nombre de usuario: ")
            self.username=new_username
        
        print(self.show_attr())

class Musician(User):

    def __init__(self, id, name, email, username, type,streams):
        super().__init__(id, name, email, username, type)
        self.streams=streams

    def show_attr_album(self,albums,trackslist): #mostrar atributos mas los albums de cada musician
        atributos=super().show_attr()

        album_artist=""
        for album in albums:
            if self.id == album.artist:
                album_artist=album_artist+album.show_attr(trackslist)+"\n" 

        lista_track_ord=sorted(trackslist,key=lambda x: x.streams, reverse=True) #se ordena y se crea otra lista

        index=0
        lista_tracks=[]

        while len(lista_tracks)<10 and index<len(lista_track_ord): #para mostrar el top 10 canciones mas escuchadas de un musician

            if self.id in lista_track_ord[index].artist:
                lista_tracks.append(lista_track_ord[index])

            index=index+1

        top_tracks=""
        for track in lista_tracks:
            top_tracks=top_tracks+track.name+"\n"  

        return atributos+" \nMy Albums: {} \nStreams Musico: {} \nTop 10 canciones mas escuchadas: \n{}".format(album_artist,self.streams,top_tracks)
    

class Listener(User):

    def __init__(self, id, name, email, username, type,streams,likeM,likeA,likeT,likeP):
        super().__init__(id, name, email, username, type)
        self.streams=streams
        self.likeM=likeM
        self.likeA=likeA
        self.likeT=likeT
        self.likeP=likeP

    def show_attr(self): #mostrar atributos de un listener
        atributos=super().show_attr()
        return atributos+" \nStreams Escucha: {}".format(self.streams)   
    
    def show_attr_playlist(self,playlists,tracks): #mostrar atributos de un listener con playlists
        atributos=super().show_attr()

        playlist_creator=""
        for playlist in playlists:
            if self.id == playlist.creator:
                playlist_creator=playlist_creator+playlist.show_attr(tracks)+"\n"  

        like_Album="" #para mostrar los albums mas gustados
        for album in self.likeA:
            like_Album=like_Album+album+", "
        like_Album=like_Album+"\n"

        like_Track="" #para mostrar las canciones mas gustadas
        for track in self.likeT:
            like_Track=like_Track+track+", "
        like_Track=like_Track+"\n"

        return atributos+" \nMy Playlist: {} \nStreams Escucha: {} \nAlbums gustados: {} \nCanciones gustadas: {}".format(playlist_creator,self.streams,like_Album,like_Track)

    def agregar_listaT(self,track_id): #darle like a una cancion
        self.likeT.append(track_id)
    
    def agregar_listaA(self,album_id):  #darle like a un album
        self.likeA.append(album_id)
    
    def agregar_listaP(self,playlist_id): #darle like a una playlist
        self.likeP.append(playlist_id)

    def agregar_listaM(self,musician_id): #darle like a un musico
        self.likeM.append(musician_id)
         
