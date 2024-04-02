import folium

coord_geo = []
dicionarios = []
dicionario = {}

def set_markup(mapa, location, ip):
    popupe = "User IP: " + str(ip) + "\n" + "Nome: " + str('teste') + "\n Born: " + str('tteste')
    folium.Marker([location[0], location[1]], popup = popupe, icon=folium.Icon(color='lightblue')).add_to(mapa)
    return mapa

def create_map(my_location):
    #Retorna um mapa com a minha localização
    mapa = folium.Map(location=[my_location[0], my_location[1]], zoom_start=1)
    popupe = "User IP: Strovertz" + "\n" + "Nome: Gleison Pires"
    folium.Marker([my_location[0], my_location[1]], popup = popupe, icon=folium.Icon(color='lightgreen', icon='home')).add_to(mapa)
    return mapa
