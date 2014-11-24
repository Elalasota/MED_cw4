from math import sqrt
from numpy import corrcoef
import arcpy
from math import sqrt
columns = ['POP', 'POLE_KM2']
populacja=[]
powierzchnia=[]
curObj = arcpy.da.SearchCursor(r"D:/Ela Lasota/Metody eksploracji danych/lab4-master/bdo/powiaty.shp", columns)
for row in curObj:
    populacja.append(row[0])
    powierzchnia.append(row[1])
    
    
def pearson2(tab1, tab2):
    korelacja=0
    wartosci1=tab1
    wartosci2=tab2
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

print pearson2(populacja, powierzchnia)  

def pearsonNumpy2(tab1, tab2):
    korelacje=corrcoef(tab1, tab2)
    korelacja=korelacje[1,0]
    return korelacja
print pearsonNumpy2(populacja, powierzchnia)