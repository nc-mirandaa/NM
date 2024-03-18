import json
import random
import re
from os.path import exists
from datetime import datetime
from clases.c_users import Musician
from clases.c_users import Listener
from clases.c_albums import Album
from clases.c_playlists import Playlist
from clases.c_tracklists import Track

class App:

    #en esta clase se van a crear todas la funciones del programa

    def __init__(self):

        #listas donde se van a guardar todos los datos de los txt para poder accederlos

        self.listaUsers=[]
        self.listaAlbums=[]
        self.listaPlaylist=[]
        self.listaTracks=[]
        self.user_log= None

    def open_user(self): 
        
        #esta funcion es para transformar el API en base de datos del users

        archivo=open('API\\users.json','r',encoding='cp437')
        datos=archivo.read()
        archivo.close()
        listaU=json.loads(datos)
        file_name='db_users'

        with open(file_name,'w',encoding='cp437') as file:

            for i in listaU:
                
                if 'musician' in i['type']:

                    file.write(f'{i['id']},{i['name']},{i['email']},{i['username']},{i['type']},0\n') 

                elif 'listener' in i['type']:

                    file.write(f'{i['id']},{i['name']},{i['email']},{i['username']},{i['type']},0,[],[],[],[]\n')  

    def open_tracks(self,tracklist,artist):

        #esta funcion es para pasar todos los tracks a una base de datos de canciones
        #se crea una base de datos de tracks para que sea mas facil su busqueda

        file_name='db_tracks'    

        with open(file_name,'a',encoding='cp437') as file:

            for track in tracklist:
            
                file.write(f'{track['id']},{track['name']},{track['duration']},{track['link']},{artist},0\n') #hacer streams 0 como en user

    def open_album(self): 
        
        #esta funcion es para transformar el API en base de datos del album

        archivo=open('API\\albums.json','r',encoding='cp437')
        datos=archivo.read()
        archivo.close()
        listaA=json.loads(datos)
        file_name='db_albums'    

        with open(file_name,'w',encoding='cp437') as file:

            for album in listaA:
            
                tracklist_ids=""

                for j in album['tracklist']:

                    tracklist_ids=tracklist_ids+j['id']+"()"

                self.open_tracks(album['tracklist'],album['artist']) 
                file.write(f'{album['id']},{album['name']},{album['description'].replace("\n","*")},{album['cover']},{album['published']},{album['genre']},{album['artist']},{tracklist_ids},0\n') 

    def open_playlist(self):
        
        #esta funcion es para transformar el API en base de datos del playlist

        archivo=open('API\\playlists.json','r',encoding='cp437')
        datos=archivo.read()
        archivo.close()
        listaP=json.loads(datos)
        file_name='db_playlist'

        with open(file_name,'w',encoding='cp437') as file:

            for playlist in listaP:

                tracklist=""

                for id in playlist['tracks']:
                    tracklist=tracklist+id+"()"

                file.write(f'{playlist['id']},{playlist['name']},{playlist['description'].replace("\n","*")},{playlist['creator']},{tracklist}\n')
      
    def cargar_todo_api(self):

        #se llaman a todas las funciones anteriores
        #se hacen validaciones para ver si ya existian las bases de datos ya creadas // notifica si ha sido cargada por primera vez o si ya habia sido cargada

        if not exists('db_users'):
            self.open_user()
            print("db_users cargado del API")
        else:
            print("db_users ya habia sido cargado")

        if not exists('db_albums'):
            self.open_album()
            print("db_albums cargado del API")
        else:
            print("db_albums ya habia sido cargado")

        if not exists('db_playlist'):
            self.open_playlist()
            print("db_playlist cargado del API")
        else:
            print("db_playlist ya habia sido cargado")
    
    def download_user(self):

        #se pasa toda la informacion del db_users para la listaUsers vueltos objetos respectivamente de tipo Musician o Listener

        with open('db_users','r',encoding='UTF-8') as data: 

            for linea in data:

                x=linea.split(",")
                tipo=x[4]

                if 'musician' in tipo:
                    vUser=Musician(id=x[0],name=x[1],email=x[2],username=x[3],type=x[4],streams=int(x[5]))
                    self.listaUsers.append(vUser)

                elif 'listener' in tipo:

                    likeM=x[6].split("()")
                    likeM.pop()

                    likeA=x[7].split("()")
                    likeA.pop()

                    likeT=x[8].split("()")
                    likeT.pop()

                    likeP=x[9].split("()")
                    likeP.pop()

                    vUser1=Listener(id=x[0],name=x[1],email=x[2],username=x[3],type=x[4],streams=int(x[5]),likeM=likeM,likeA=likeA,likeT=likeT,likeP=likeP)
                    self.listaUsers.append(vUser1)
    
    def download_albums(self):

        #se pasa toda la informacion del db_albums para la listaAlbums como objetos de la clase Album

        with open('db_albums','r',encoding='UTF-8') as data: 

            for b in data:

                x=b.split(",")
                tracklist1=x[7].split("()")
                tracklist1.pop()
                vAlbum=Album(id=x[0],name=x[1],description=x[2],cover=x[3],published=x[4],genre=x[5],artist=x[6],tracklist=tracklist1,streams=int(x[8])) #cambiar streams

                self.listaAlbums.append(vAlbum)
               
    def download_playlist(self):

        #se pasa toda la informacion del db_playlist para la listaPLaylist como objetos de la clase Playlist

        with open('db_playlist','r',encoding='UTF-8') as data: 

            for b in data:

                x=b.split(",")
                tracklist1=x[4].split("()")
                tracklist1.pop()
                vPlaylist=Playlist(id=x[0],name=x[1],description=x[2],creator=x[3],tracks=tracklist1)

                self.listaPlaylist.append(vPlaylist)

    def download_tracks(self):

        #se pasa toda la informacion del db_tracks para la listaTracks como objetos de la clase Track

        with open('db_tracks','r',encoding='UTF-8') as data: 

            for b in data:

                x=b.split(",")
                vTracks=Track(id=x[0],name=x[1],duration=x[2],link=x[3],artist=x[4],streams=int(x[5])) 

                self.listaTracks.append(vTracks)

    def cargar_todo_txt(self):

        #se llaman a todas las funciones anteriores

        self.download_user() 
        self.download_albums()   
        self.download_playlist()
        self.download_tracks()   

    #Gestion de Perfil

    def create_user(self): 

        #se va a iniciar sesion si el nombre ya se encuentra entre los datos de la listaUsers
        #en tal caso que no, se registra pidiendo los datos necesarios

        for i in range(1):
            y=str(random.randint(1,1000))

        print("\nBienvenido a Metrofy! \nRegistrate para comenzar: ")

        name=input("Escribe tu Nombre: ") 
        varFound=False

        for user in self.listaUsers:
            if name in user.name: #esto es para ver si el nombre de el usuario ya existe
                print(user.show_attr()) #en ese caso mostrar toda su informacion
                varFound=True
                self.user_log=user
                break 

        if not varFound:

            email=input("Escribe tu Email: ")

            while not ("@" in email): #validacion para que solo se pueda ingresar correos
                print("Ese correo no es valido")
                email=input("Escribe tu email: ")            

            user=None
            while user==None:
                
                tipo=int(input("1)musician  2)listener \nEscribe que tipo de usuario te gustaria ser: ")) 
                
                if tipo ==1:
                    tipo="musician"

                elif tipo ==2:
                    tipo="listener"

                vtipo=tipo
                name=name 
                id=str(datetime.now()).replace(" ", "-").replace(".", "-").replace(":", "") #esto es para que se cree un id diferente para cada usuario nuevo
                username=y #como inicio se va a poner un numero aleatorio, luego la persona lo puede cambiar

                if "musician" in tipo:  
                    user=Musician(id,name,email,username,vtipo,streams=0) #se crea onjeto musician
                    self.listaUsers.append(user)

                elif "listener" in tipo: 
                    user=Listener(id,name,email,username,vtipo,streams=0,likeM=[],likeA=[],likeT=[],likeP=[]) #se crea objeto listener
                    self.listaUsers.append(user)

                else:
                    print("No es valido")

            print(user.show_attr()) 
            self.user_log=user

            print("\nYa estas registrado")

            if type(self.user_log) is Listener:
                print("Ya estas registrado como Listener")
            if type(self.user_log) is Musician:
                print("Ya estas registrado como Musician")
        
        

    def borrar_usuario(self):

        #un usuario podra eliminar todos los datos de su cuenta

        for user in self.listaUsers:

            if self.user_log.id==user.id:
                print(user.show_attr())
                print(self.user_log.show_attr()) 
                pos=self.listaUsers.index(user)
                self.listaUsers.pop(pos) 
                break

        self.user_log=None

    def buscar_usuario(self):

        #un usuario podra buscar a otro usuario por su nombre

        usuario=input("Escribe el nombre del usuario que quieres buscar: ") 
        for user in self.listaUsers:
            if usuario in user.name:
                print(user.show_attr())
                if type(user) == Listener:
                    print(user.show_attr_playlist(self.listaPlaylist,self.listaTracks))
                break

    def gestion_pefil(self):

        #menu donde se encuentran todas las funciones anteriores

        x=True
        while x:    
            option=int(input("\n1)Cambiar datos \n2)Borrar datos \n3)Buscar Usuario \n4)Salir \nIndica que quieres hacer ahora: "))
            print(option)

            if option ==1:
                self.user_log.cambiar_datos()
            elif option==2:
                self.borrar_usuario()
            elif option==3:
                self.buscar_usuario() 
            elif option==4:
                #salir
                x=False

    #Gestion musical

    def buscar_tracks(self):

        #se podran buscar las canciones por su nombre

        name=input("Escribe el nombre de la cancion que quieres buscar: ") 
        for track in self.listaTracks:
            if name in track.name:
                print(track.show_attr())

                if type(self.user_log) is Musician:
                    return

                #se preguntara si se quiere reproducir la cancion buscada

                print("Quieres escuchar esta cancion: ")
                stream=int(input("""
                           1) Si
                           2) No
                        (ingrese el numero)-->"""))
                    
                if stream ==1:

                    print("Reproduciendo...")
                    self.listaTracks[self.listaTracks.index(track)].streams=track.streams+1 #se suma 1 al atributo streams de Track

                    for musico in self.listaUsers:

                        if musico.id in track.artist:
                            self.listaUsers[self.listaUsers.index(musico)].streams=musico.streams+1  #se suma 1 al atributo streams de Musician
                            break

                    for escucha in self.listaUsers:

                        if escucha.id in self.user_log.id:
                            
                            self.listaUsers[self.listaUsers.index(self.user_log)].streams=escucha.streams+1  #se suma 1 al atributo streams de Listener
                            break
                    break  
                else:
                    break

    def buscar_album(self):

        #se podran buscar los albums por su nombre

        name=input("Escribe el nombre del album que quieres buscar: ") 
        for album in self.listaAlbums:
            if name in album.name:
                print(album.show_attr(self.listaTracks))

                if type(self.user_log) is Musician:
                    return

                #se preguntara si se quiere reproducir el album buscado

                print("Quieres escuchar este album: ")
                stream=int(input("""
                           1) Si
                           2) No
                        (ingrese el numero)-->"""))
                
                if stream ==1:
                    
                    print("Reproduciendo...")
                    self.listaAlbums[self.listaAlbums.index(album)].streams=album.streams+1 #se suma 1 al atributo streams de Album

                    for musico in self.listaUsers:

                        if musico.id in album.artist:

                            self.listaUsers[self.listaUsers.index(musico)].streams=musico.streams+1  #se suma 1 al atributo streams de Musician
                            break
                                    
                    for escucha in self.listaUsers:

                        if escucha.id in self.user_log.id:
                            
                            self.listaUsers[self.listaUsers.index(self.user_log)].streams=escucha.streams+1  #se suma 1 al atributo streams de Listener
                            break
                    break 
                else:
                    break

    def buscar_playlist(self):

        #se podran buscar las playlists por su nombre

        name=input("Escribe el nombre de la playlist que quieres buscar: ") 
        for playlist in self.listaPlaylist:
            if name in playlist.name:
                 
                print(playlist.show_attr(self.listaTracks))

                if type(self.user_log) is Musician:
                    return

                #se preguntara si se quiere reproducir alguna de las canciones de la playlist

                print("Quieres escuchar alguna cancion de esta playlist: ") 
                rep=int(input("""
                               1) Si
                               2) No
                            (ingrese el numero)-->"""))
                if rep ==1:
                    name=input("Escribe el nombre de la cancion que quieres escuchar: ") 
                    print("Reproduciendo...")

                    for track in self.listaTracks:
                        if name in track.name:
                            self.listaTracks[self.listaTracks.index(track)].streams=track.streams+1 #se suma 1 al atributo streams de Track

                            for musico in self.listaUsers:
                            
                                    if musico.id in track.artist:
                                        self.listaUsers[self.listaUsers.index(musico)].streams=musico.streams+1  #se suma 1 al atributo streams de Musician
                                        break

                            for escucha in self.listaUsers:
                            
                                    if escucha.id in self.user_log.id:

                                        self.listaUsers[self.listaUsers.index(self.user_log)].streams=escucha.streams+1  #se suma 1 al atributo streams de Listener
                                        break
                            break  
                else:
                    break

    def buscar_musico(self): 

        #se podran buscar un musico por su nombre

        name=input("Escribe el nombre del musico que quieres buscar: ") 

        for musico in self.listaUsers:
            if type(musico) is Musician:
                if name in musico.name:
                    print(musico.show_attr_album(self.listaAlbums,self.listaTracks))
                    break

    def buscador(self):

        #menu donde se encuentran las funciones anteriores

        x=True
        while x:    
            option=int(input("\n1)Musico \n2)Album \n3)Playlist \n4)Cancion \n5)Salir \nIndica a quien quieres buscar: "))
            print(option)

            if option ==1:
                self.buscar_musico()
            elif option==2:
                self.buscar_album()
            elif option==3:
                self.buscar_playlist() 
            elif option==4:
                self.buscar_tracks()
            elif option==5:
                #salir
                x=False

    def val_cover(self):

        #validacion para el cover del album (link)

        pattern = r'^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$' #arreglar validacion while 
        valido="si"
        cover=""

        while valido=="si":
            cover=input("Link de la portada del album: ")
            if bool(re.match(pattern,cover))==False:
                print("link invalido, asegurese que es un link lo que esta ingresando")
            else:
                break

        return cover

    def val_duration_track(self):

        #validacion para el duration de una cancion nueva

        x=True
        while x==True:
            duracion=input("""
                       Durancion de la cancion
                       tiene que mostrar los minutos y segundos
                       Ejemplo: 1:22 ---> """)
            pattern=r"\d{1}\:\d{1,2}"
            match= re.match(pattern,duracion)
            if match:
                print('Formato Valido')
                x=False
                break
            print("Eso no es una formato valido")  

        return duracion

    def val_link_track(self):

        #validacion para el link de una cancion nueva

        pattern = r'^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$' #arreglar validacion while 
        valido="si"
        while valido=="si":
            link=input("Link de la cancion: ")
            if bool(re.match(pattern,link))==False:
                print("link invalido, asegurese que es un link lo que esta ingresando")
            else:
                break
        
        return link

    def crear_track_album(self):

        #se puede crear una cancion nueva

        name=input("Escribe el nombre de la cancion: ")
        duration=self.val_duration_track()
        link=self.val_link_track()
        id=str(datetime.now()).replace(" ", "-").replace(".", "-").replace(":", "")
        artist=self.user_log.id
        streams=0
        track1=Track(id,name,duration,link,artist,streams) #se vuelve objeto de tipo Track
        self.listaTracks.append(track1)

        return track1   

    def loop_tracks_Albums(self):

        #se pregunta cuantas veces el musico quiera añadir una cancion nueva

        Tracks_Album=[]
        x=True
        while x==True:
            print("Desea agregar otra cancion al tracklist?")
            y=input("""
                       1) Si
                       2) No
                    (ingrese el numero)-->""")
            if y:
                y=int(y)
                if y==1:
                    Tracks_Album.append(self.crear_track_album().id)
                elif y==2:
                    break
            else:
                print("input no valido")
    
        return Tracks_Album

    def crear_album(self):

        #se crea un album nuevo 

        name=input("Escribe el nombre del album: ")
        description=input("Escribe la descripcion del album: ")
        cover=self.val_cover()
        published=datetime.utcnow()
        genre=input("Escribe el genero del album: ")
        tracklist=self.loop_tracks_Albums() 
        artist=self.user_log.id 
        streams=0
        id=str(datetime.now()).replace(" ", "-").replace(".", "-").replace(":", "")

        album1=Album(id,name,description,cover,published,genre,artist,tracklist,streams) #se vuelve objeto de tipo Album
        self.listaAlbums.append(album1)

        print(album1.show_attr(self.listaTracks))

    def crear_track_playlist(self):

        #se crea una playlist nueva 

        name=input("Escribe el nombre de la cancion: ")
        for track in self.listaTracks:
            if name == track.name:
                return track

    def loop_tracks_Playlist(self):

        #se pregunta cuantas veces el listener quiera añadir una cancion

        Tracks_Playlist=[]
        x=True
        while x==True:
            print("Desea agregar otra cancion al tracklist?")
            y=input("""
                       1) Si
                       2) No
                    (ingrese el numero)""")
            if y:
                y=int(y)
                if y==1:
                    Tracks_Playlist.append(self.crear_track_playlist().id)
                elif y==2:
                    break
            else:
                print("input no valido")
    
        return Tracks_Playlist

    def crear_playlist(self):

        #se crea una playlist nueva

        name=input("Escribe el nombre de la playlist: ")
        description=input("Escribe la descripcion de la playlist: ")
        creator=self.user_log.id
        id=str(datetime.now()).replace(" ", "-").replace(".", "-").replace(":", "")
        tracks=self.loop_tracks_Playlist() 

        playlist1=Playlist(id,name,description,creator,tracks) #se vuelve objeto de tipo Playlist
        self.listaPlaylist.append(playlist1)

        print(playlist1.show_attr(self.listaTracks)) 

    def gestion_musical(self):

        #menu donde aparecen las funciones anteriores
        #se valida si es de tipo musician o listener para mostrar los menu con las opciones de cada uno

        if type(self.user_log) is Musician:

            x=True
            while x:    
                option=int(input("\n1)Crear un album \n2)Buscador \n3)Salir \nIndica que quieres hacer ahora: "))
                print(option)

                if option ==1:
                    self.crear_album()
                elif option==2:
                    self.buscador()
                elif option==3:
                    #salir
                    x=False

        elif type(self.user_log) is Listener:

            x=True
            while x:    
                option=int(input("\n1)Crear una playlist \n2)Buscador \n3)Salir \nIndica que quieres hacer ahora: "))
                print(option)

                if option ==1:
                    self.crear_playlist()
                elif option==2:
                    self.buscador()
                elif option==3:
                    #salir
                    x=False

    #Gestion de Interacciones

    def dar_tracks_like(self): 

        #se le da un like a una cancion

        name=input("Escribe el nombre de la cancion que quieres buscar: ") #se busca la cancion por su nombre
        for track in self.listaTracks:
            if name in track.name:
                print(track.show_attr())

                print("Quieres darle like a esta cancion: ") #se pregunta si le quiere dar like o no
                like=int(input("""
                           1) Si
                           2) No
                        (ingrese el numero)-->"""))

                if like ==1:
                    self.user_log.likeT.append(track.name) #se hace un append a la lista likeT (atributo de listener)
                    print(self.user_log.likeT)
                else:
                    break

    def dar_playlist_like(self): 

        #se le da un like a una playlist

        name=input("Escribe el nombre de la playlist que quieres buscar: ") #se busca la playlist por su nombre
        for playlist in self.listaPlaylist:
            if name in playlist.name:
                print(playlist.show_attr(self.listaTracks))

                print("Quieres darle like a esta playlist: ") #se pregunta si le quiere dar like o no
                like=int(input("""
                           1) Si
                           2) No
                        (ingrese el numero)-->"""))

                if like ==1:
                    self.user_log.likeP.append(playlist.name) #se hace un append a la lista likeP (atributo de listener)
                    print(self.user_log.likeP)
                    break
                else:
                    break

    def dar_album_like(self): 

        #se le da un like a un album

        name=input("Escribe el nombre del album que quieres buscar: ") #se busca el album por su nombre
        for album in self.listaAlbums:
            if name in album.name:
                print(album.show_attr(self.listaTracks))

                print("Quieres darle like a este album: ") #se pregunta si le quiere dar like o no
                like=int(input("""
                           1) Si
                           2) No
                        (ingrese el numero)-->"""))

                if like ==1:
                    self.user_log.likeA.append(album.name) #se hace un append a la lista likeA (atributo de listener)
                    print(self.user_log.likeA)
                    break
                else:
                    break

    def dar_musico_like(self): 

        #se le da un like a un musico

        name=input("Escribe el nombre del musico que quieres buscar: ") #se busca el musico por su nombre
        for user in self.listaUsers:
            if type(user) is Musician:
                if name in user.name:
                    print(user.show_attr())

                    print("Quieres darle like a este musico: ") #se pregunta si le quiere dar like o no
                    like=int(input("""
                               1) Si
                               2) No
                            (ingrese el numero)-->"""))

                    if like ==1:
                        self.user_log.likeM.append(user.name) #se hace un append a la lista likeM (atributo de listener)
                        print(self.user_log.likeM)
                        break
                    else:
                        break

    def dar_likes(self):

        #menu donde aparecen todas la funciones anteriores

        x=True
        while x:    
            option=int(input("\n1)Musico \n2)Album \n3)Playlist \n4)Cancion \n5)Salir \nIndica a quien quieres derle like: "))
            print(option)

            if option ==1:
                self.dar_musico_like()
            elif option==2:
                self.dar_album_like()
            elif option==3:
                self.dar_playlist_like() 
            elif option==4:
                self.dar_tracks_like()
            elif option==5:
                #salir
                x=False

    def buscar_musico_like(self):

        #se puede consultar los likes de un musico

        for musico in self.user_log.likeM:
            print(musico)

        print("Quieres quitar un like a algunos de estos musicos: ") #se pregunta si se quiere remover un like de algun musico
        remove=int(input("""
               1) Si
               2) No
            (ingrese el numero)-->"""))
        
        if remove ==1:
            name=input("Escribe el nombre del musico que quieres buscar: ") 

            for musico in self.user_log.likeM:
                if name in musico:

                    pos=self.user_log.likeM.index(musico)
                    self.user_log.likeM.pop(pos) 
                    print("Se ha eliminado de tus favoritos")
                    print(self.user_log.likeM)

    def buscar_album_like(self): 

        #se puede consultar los likes de un album

        for album in self.user_log.likeA:
            print(album)

        print("Quieres quitar un like a algunos de estos albums: ") #se pregunta si se quiere remover un like de algun album
        remove=int(input("""
               1) Si
               2) No
            (ingrese el numero)-->"""))
        
        if remove ==1:
            name=input("Escribe el nombre del album que quieres buscar: ") 

            for album in self.user_log.likeA:
                if name in album:

                    pos=self.user_log.likeA.index(album)
                    self.user_log.likeA.pop(pos) 
                    print("Se ha eliminado de tus favoritos")
                    print(self.user_log.likeA)
                    


    def buscar_playlist_like(self): 

        #se puede consultar los likes de una playlist

        for playlist in self.user_log.likeP:
            print(playlist)

        print("Quieres quitar un like a algunos de estas playlists: ") #se pregunta si se quiere remover un like de alguna playlist
        remove=int(input("""
               1) Si
               2) No
            (ingrese el numero)-->"""))
        
        if remove ==1:
            name=input("Escribe el nombre de la playlist que quieres buscar: ") 

            for playlist in self.user_log.likeP:
                if name in playlist:

                    pos=self.user_log.likeP.index(playlist)
                    self.user_log.likeP.pop(pos) 
                    print("Se ha eliminado de tus favoritos")
                    print(self.user_log.likeP)


    def buscar_tracks_like(self):

        #se puede consultar los likes de una cancion

        for track in self.user_log.likeT:
            print(track)

        print("Quieres quitar un like a algunos de estas canciones: ") #se pregunta si se quiere remover un like de alguna cancion
        remove=int(input("""
               1) Si
               2) No
            (ingrese el numero)-->"""))
        
        if remove ==1:
            name=input("Escribe el nombre de la cancion que quieres buscar: ") 

            for track in self.user_log.likeT:
                if name in track:

                    pos=self.user_log.likeT.index(track)
                    self.user_log.likeT.pop(pos) 
                    print("Se ha eliminado de tus favoritos")
                    print(self.user_log.likeT)


    def consultar_likes(self):

        #menu donde se encuentran las funciones anteriores

        x=True
        while x:    
            option=int(input("\n1)Musico \n2)Album \n3)Playlist \n4)Cancion \n5)Salir \nIndica que likes quieres ver: "))
            print(option)

            if option ==1:
                self.buscar_musico_like()
            elif option==2:
                self.buscar_album_like()
            elif option==3:
                self.buscar_playlist_like() 
            elif option==4:
                self.buscar_tracks_like()
            elif option==5:
                #salir
                x=False

    def gestion_likes(self):

        #menu donde se muestran las opciones 

        if type(self.user_log) is Listener: #se muestran las funciones de un listener
            x=True
            while x:    
                option=int(input("\n1)Dar like \n2)Ver tus likes \n3)Salir \nIndica que quieres hacer ahora: "))
                print(option)

                if option ==1:
                    self.dar_likes()
                elif option==2:
                    self.consultar_likes() 
                elif option==3:
                    #salir
                    x=False
        
        elif type(self.user_log) is Musician: #no hay funciones para el musician
            print("Usted siendo musico no puede acceder a esta funcion")

    def buscar_album_stream(self):

        #se calculan el top 5 de streams de los albums

        lista_ord_album=sorted(self.listaAlbums,key=lambda x: x.streams, reverse=True) #se crea una lista ordenada en base a los streams
        print("Top 5 de los albums mas escuchados: ")
        
        for index in range(0,5): #se ordenan en un rango de 5 
            print("\n\tPosicion: ", index+1)
            print(lista_ord_album[index].show_attr())

    def buscar_tracks_stream(self):

        #se calculan el top 5 de streams de las canciones

        lista_ord_tracks=sorted(self.listaTracks,key=lambda x: x.streams, reverse=True) #se crea una lista ordenada en base a los streams
        print("Top 5 de las canciones mas escuchadas: ")
        
        for index in range(0,5): #se ordenan en un rango de 5 
            print("\n\tPosicion: ", index+1)
            print(lista_ord_tracks[index].show_attr())

    def buscar_escucha_stream(self):
        
        #se calculan el top 5 de streams de los listeners

        lista_ord_usuarios=sorted(self.listaUsers,key=lambda x: x.streams, reverse=True) #se crea una lista ordenada en base a los streams
        print("Top 5 de los escuchas con mas streams: ")

        index=0
        lista_escucha=[]

        while len(lista_escucha)<5:

            if type(lista_ord_usuarios[index]) is Listener: #se valida que sea un listener
                lista_escucha.append(lista_ord_usuarios[index])

            index=index+1

        for index in range(0,5): #se ordenan en un rango de 5 

            print("\n\tPosicion: ", index+1)
            print(lista_escucha[index].show_attr())

    def buscar_musico_stream(self):

        #se calculan el top 5 de streams de los musicians
        
        lista_ord_usuarios=sorted(self.listaUsers,key=lambda x: x.streams, reverse=True) #se crea una lista ordenada en base a los streams
        print("Top 5 de los musicos con mas streams: ")

        index=0
        lista_musico=[]

        while len(lista_musico)<5:

            if type(lista_ord_usuarios[index]) is Musician: ##se valida que sea un musician
                lista_musico.append(lista_ord_usuarios[index])

            index=index+1

        for index in range(0,5): #se ordenan en un rango de 5 

            print("\n\tPosicion: ", index+1)
            print(lista_musico[index].show_attr())

    def indicadores(self):

        #se muestra un meno con la funciones anteriores

        x=True
        while x:    
            option=int(input("\n1)Musico \n2)Album \n3)Cancion \n4)Escucha \n5)Salir \nIndica que ranking quieres ver: "))
            print(option)

            if option ==1:
                self.buscar_musico_stream()
            elif option==2:
                self.buscar_album_stream()
            elif option==3:
                self.buscar_tracks_stream() 
            elif option==4:
                self.buscar_escucha_stream()
            elif option==5:
                #salir
                x=False

    def menu_Ops(self):

        #se muestra un menu con las funciones principales

        x=True
        while x:
            option=int(input("\n1)Gestion de Perfil \n2)Gestion musical \n3)Gestion de interacciones \n4)Indicadores \n5)Salir \nIndica que quieres hacer ahora: "))
            print(int(option))
            if option ==1:
                self.gestion_pefil()
            elif option ==2:
                self.gestion_musical()
            elif option ==3:
                self.gestion_likes()
            elif option ==4:
                self.indicadores()
            elif option ==5:
                print("Usted ha salido de Metrofy")
                x=False

    def guardar_users(self):

        #se guardan las listas en los txt (users)

        with open('db_users','w',encoding='UTF-8') as data:

            for user in self.listaUsers:

                if type(user) is Musician: #se hacen validaciones por si es musician guardar todos los atributos de este
                    data.write(f'{user.id},{user.name},{user.email},{user.username},{user.type},{user.streams}\n') 
                
                elif type(user) is Listener: #se hacen validaciones por si es listener guardar todos los atributos de este

                    like_musico=""
                    for musico in user.likeM:
                        like_musico=like_musico+musico+"()"

                    like_album=""
                    for album in user.likeA:
                        like_album=like_album+album+"()"

                    like_track=""
                    for track in user.likeT:
                        like_track=like_track+track+"()"

                    like_playlist=""
                    for playlist in user.likeP:
                        like_playlist=like_playlist+playlist+"()"

                    data.write(f'{user.id},{user.name},{user.email},{user.username},{user.type},{user.streams},{like_musico},{like_album},{like_track},{like_playlist}\n') 
            
    def guardar_albums(self): 

        #se guardan las listas en los txt (albums)

        with open('db_albums','w',encoding='UTF-8') as data:

            for album in self.listaAlbums:

                tracklist=""
                for track in album.tracklist:
                    tracklist=tracklist+track+"()"

                data.write(f'{album.id},{album.name},{album.description},{album.cover},{album.published},{album.genre},{album.artist},{tracklist},{album.streams}\n')  

    def guardar_playlist(self):

        #se guardan las listas en los txt (playlist)

        with open('db_playlist','w',encoding='UTF-8') as data:

            for playlist in self.listaPlaylist:

                tracks=""
                for track in playlist.tracks:
                    tracks=tracks+track+"()"
  
                data.write(f'{playlist.id},{playlist.name},{playlist.description},{playlist.creator},{tracks}\n')  

    def guardar_tracks(self):

        #se guardan las listas en los txt (tracks)

        with open('db_tracks','w',encoding='UTF-8') as data:

            for track in self.listaTracks:

                data.write(f'{track.id},{track.name},{track.duration},{track.link},{track.artist},{track.streams}\n')  


    def guardar_todo(self):

        #menu donde se se realizan todas las funciones anteriores

        self.guardar_users()
        self.guardar_albums()
        self.guardar_playlist()
        self.guardar_tracks()
