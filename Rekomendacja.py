#!/usr/bin/env python
#-*- coding: utf-8 -*-

#  Wzorowane na przyk�adzie Rona Zacharskiego
#

from math import sqrt
from numpy import corrcoef
users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odleg�o�� w metryce taks�wkowej mi�dzy dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwr�� -1, gdy zbiory nie maj�� wsp�lnych element�w"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1






def pearson(rating1, rating2):
    korelacja=0
    klucze1=rating1.keys()
    klucze2=rating2.keys()
    wartosci1=rating1.values()
    wartosci2=rating2.values()
    suma_iloczyn=0
    iksy=0
    igreki=0
    iksykw=0
    igrekikw=0
    #===========================================================================
    # for klucz in klucze1
    #     if klucz in klucze2
    #===========================================================================
    for i in xrange(0, len(wartosci1)):       
        suma_iloczyn=suma_iloczyn+wartosci1[i]*wartosci2[i]  
        iksy=iksy+wartosci1[i]
        igreki=igreki+wartosci2[i]
        iksykw=iksykw+wartosci1[i]**2
        igrekikw=igrekikw+wartosci2[i]**2
    korelacja=(suma_iloczyn-((iksy*igreki)/len(wartosci1)))/(sqrt(iksykw-(iksy**2/len(wartosci1)))*sqrt(igrekikw-(igreki**2/len(wartosci2))))    
    return korelacja

print pearson(users["Ania"], users["Bonia"])






def pearsonNumpy(rating1, rating2):
    korelacje=corrcoef(rating1.values(), rating2.values())
    korelacja=korelacje[1,0]
    return korelacja
print pearsonNumpy(users["Ania"], users["Bonia"])