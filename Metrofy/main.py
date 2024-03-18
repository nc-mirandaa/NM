from App import App

#main donde se corre todo el programa 

def main():
    app=App()
    app.cargar_todo_api()
    app.cargar_todo_txt()
    app.create_user()
    app.menu_Ops()
    app.guardar_todo()

main()