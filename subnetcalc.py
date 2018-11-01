# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 19:08:43 2018

@author: adam
"""

def validateip(ipl):
    
    if len(ipl) != 4:
        print('please enter valid IP address')
    
    elif ipl[0] >= 224 and ipl[0] <= 255:
        print('IP cannot be class D, class E or broadcast address')
        print('please Enter Valid IP address')
    
    elif ipl[0] >= 127 and ipl[0] < 128 :
        print('IP cannot be loopback address')
        print('please Enter Valid IP address')
    else:
        for i in range(len(ipl)):
            if ipl[i] > 255:
                print('Octets must be < 255')
                print('please Enter Valid IP address')
    
    

while True:
    
    ip = input(' Please Enter an IP address or enter "q" to quit :' )
    ipl = [int(x) for x in ip.split('.')] # loop through ip split cast to int
    
    if ip  == 'q':
        break
    
    validateip(ipl)
    
    #print('all ok')
    
        
