# -*- coding: utf-8 -*-
#Primeros pasos con matpltplib


import matplotlib.pyplot as plt



def graficaA():
    
    print('Grafica de líneas 1')
    a=[1,2,3,4]
    b=[11,22,33,44]

    plt.plot(a,b,color='blue',linewidth=3,label='linea')
    plt.legend()
    plt.show()
    
def graficaB():
   
    print('Gráfica de líneas 2')
    x1=[3,4,5,6]
    y1=[5,6,3,4]
    x2=[2,5,8]
    y2=[3,4,3]
    
    plt.plot(x1,y1,label='línea 1',linewidth=4,color='blue')
    plt.plot(x2,y2,label='línea 2',linewidth=4,color='green')
    
    plt.title('Diagrama de líneas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    
    plt.legend()
    plt.grid()
    plt.show()
    

    
    
    
    




  


              
        
        

    

