def get_city(city,country,population=None):
    if population:
        cityform = city+","+country+" - "+str(population)
    else:
        cityform =  city+","+country
    return cityform.title()
    
citta =get_city('milano','italia',500)
print (citta)
