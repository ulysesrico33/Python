# -*- coding: utf-8 -*-


import mysql.connector

print('Hey dude...')
cnx = mysql.connector.connect(user='root', 
                              password='P@ssw0rd',
                              host='localhost',
                              database='bd_python')
cnx.close()

  


              
        
        

    

