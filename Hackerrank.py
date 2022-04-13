# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:30:10 2021

@author: erdal
"""

a={}

a["s"]=12

a["s"]=5

#%%
import math

def enKısa(adet,kelime):
    
    kelime=str(kelime)
    
    ilk_harf=kelime[0]
    
    son_harf=kelime[-1]
    
    _,b=math.sqrt(adet).as_integer_ratio()
    
    if b!=1:
        if adet%2==0:
        
            bölüm=int(adet/2)
        
            for i in range(2-1):
            
                kelime=str(ilk_harf)+kelime
            
            for i in range(bölüm-1):
            
                kelime=kelime+str(son_harf)
    
        elif adet%2!=0:
        
            for i in range(adet-1):
                kelime=kelime+str(son_harf)
                
    elif b==1:
        
        eklenecek=int(math.sqrt(adet))
        
        for i in range(eklenecek-1):
            
            kelime=str(ilk_harf)+kelime
            
        for i in range(eklenecek-1):
            
            kelime=kelime+str(son_harf)
        
        
    return len(kelime),kelime





sonuc,klm= enKısa(8,"huprog")

print(klm)
print(sonuc)
#%%