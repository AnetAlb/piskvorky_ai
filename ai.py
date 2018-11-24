from random import randint


def umisti_symbol(pole, historie, symbol, index_pole):
     'index pole se definuje jako dany parametr pri volani fce napr. cislo_policka-1'
     pole_list=list(pole)
     pole_list[index_pole] = symbol
     historie.append(index_pole)
     return "".join(pole_list) #join listu do stringu


def overeni_pole(pole):
    if len(pole) <3:
        raise ValueError ("Pole je prilis kratke.")
    if '-' not in pole:
        raise ValueError ("Pole je plne.")


def tah_pc(pole, historie, symbol):
    overeni_pole(pole)
    delka_pole = len(pole)
    if delka_pole <3:
        print ("Pole je prilis kratke ke hre. Nastavuji pole na delku 10")
        pole = "-" *10
    pocet_kol=len(historie)
    'prvni kolo nehraj to kraju'
    if pocet_kol == 0:
        cislo_policka=randint(2,delka_pole-1)
        # pole[cislo_policka] = symbol
        #pole=pole[:cislo_policka-1] + symbol + pole[cislo_policka:]
        return umisti_symbol(pole, historie, symbol, cislo_policka-1)
        #return(pole)

    'druhe kolo a vice kol'
    if pocet_kol > 0:
        cislo_policka = historie[-1]
        if 'xx-' or '-xx' or 'x-x' not in pole:
            'pokud hra nelze skoncit jednim tahem'
            'najdi na jake pozici se nachazi posledni o'
            'potom zmer na jake srane ma vice volnych policek a tam hraj'

            prvni_cast_pole = pole[0:cislo_policka]
            vyskyt_nejblizsiho_x_vlevo=prvni_cast_pole.rfind('x') #posledni vyskyt z nejbliz k o
            if vyskyt_nejblizsiho_x_vlevo < 0:
                vyskyt_nejblizsiho_x_vlevo = 0
                pocet_volnych_mist_vlevo = cislo_policka - vyskyt_nejblizsiho_x_vlevo
            else:
                pocet_volnych_mist_vlevo = cislo_policka - vyskyt_nejblizsiho_x_vlevo

            druha_cast_pole = pole[cislo_policka:delka_pole]
            vyskyt_nejblizsiho_x_vpravo = druha_cast_pole.find('x') #vrati 1. vyskyt o z prava, vrati -1 pokud tam takova hodnota neni
            if vyskyt_nejblizsiho_x_vpravo < 0:
                vyskyt_nejblizsiho_x_vpravo = 100
                pocet_volnych_mist_vpravo = vyskyt_nejblizsiho_x_vpravo - cislo_policka
            else:
                pocet_volnych_mist_vpravo = vyskyt_nejblizsiho_x_vpravo - cislo_policka


            if pocet_volnych_mist_vlevo > pocet_volnych_mist_vpravo or cislo_policka ==19 :
                'hraj vlevo od o'
                #pole=pole[:cislo_policka-2] + symbol + pole[cislo_policka-1:]
                return umisti_symbol(pole, historie, symbol, cislo_policka-1)

                #return(pole)
            else:
                'hraj vpravo od o'
                #pole=pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
                return umisti_symbol(pole, historie, symbol, cislo_policka+1)

        else:
            'else hraj na jakejkoliv volne pole v danem stingu a pak tim nahrad dany string'
            if 'xx-' in pole:
                 print(pole.find('xx-'))
                 pozice_volne_pro_vyhry = pole.find('xx-')
                 #pole=pole[:pozice_volne_pro_vyhry+2] + symbol + pole[pozice_volne_pro_vyhry+3:]
                 return umisti_symbol(pole, historie, symbol, pozice_volne_pro_vyhry+2)

            if '-xx' in pole:
                print(pole.find('-xx'))
                pozice_volne_pro_vyhry = pole.find('-xx')
                #pole=pole[:pozice_volne_pro_vyhry] + symbol + pole[pozice_volne_pro_vyhry+1:]
                return umisti_symbol(pole, historie, symbol, pozice_volne_pro_vyhry)

            if 'x-x' in pole:
                print(pole.find('x-x'))
                pozice_volne_pro_vyhry = pole.find('x-x')
                #pole=pole[:pozice_volne_pro_vyhry+1] + symbol + pole[pozice_volne_pro_vyhry+2
                return umisti_symbol(pole, historie, symbol, pozice_volne_pro_vyhry+1)
