import folium

coord_geo = []
dicionarios = []
dicionario = {}

def set_markup(mapa, location, ip, infos):
    popupe = "User IP: " + str(ip) + "\n | CountryName: " + str(infos['data']['countryName']) + "\n | UsageType: " + str(infos['data']['usageType']) + '\nIsp: ' + str(infos['data']['isp']) + '\n | Domain: ' + str(infos['data']['domain']) + '\n\n | isTor: ' + str(infos['data']['isTor']) + '\n | abuseConfidenceScore:' + str(infos['data']['abuseConfidenceScore'])
    folium.Marker([location[0], location[1]], popup = popupe, icon=folium.Icon(color='lightblue')).add_to(mapa)
    return mapa

def create_map(my_location):
    #Retorna um mapa com a minha localização
    mapa = folium.Map(location=[my_location[0], my_location[1]], zoom_start=1)
    popupe = "User IP: Strovertz" + "\n" + "Nome: Gleison Pires"
    folium.Marker([my_location[0], my_location[1]], popup = popupe, icon=folium.Icon(color='lightgreen', icon='home')).add_to(mapa)
    return mapa
