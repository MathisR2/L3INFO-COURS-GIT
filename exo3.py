#test c5
dic={'t' : 3, 'kg' : 2, 'g' : 1}
def convertion(poids : int, unite : str, unite2 : str) : 
    if unite in dic.keys():
        number=dic[unite]
    if unite == "kg" and unite2 == "g":
        poids=poids*1000
    elif unite == "g" and unite2 == "kg":
        poids=poids/1000
    print (poids)
    
convertion(45, "g", "kg")
