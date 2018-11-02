# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 19:08:43 2018

@author: adam
"""
import sys

def validateip(ipl):
    
    for i in ipl:
        if i > 255:
            print('IP address Octets must be < 255')
            print('please Enter Valid IP address')
            return False
    
    if len(ipl) != 4:
        print('Subnet Mask must have 4 octets please enter valid IP address')
        return False
    elif ipl[0] >= 224 and ipl[0] <= 255:
        print('IP cannot be class D, class E or broadcast address')
        print('please Enter Valid IP address')
        return False
    elif ipl[0] >= 127 and ipl[0] < 128 :
        print('IP cannot be loopback address')
        print('please Enter Valid IP address')
        return False
            
    else:
        return True
                
def validatemask(maskl):
    
    validmask = [255, 254, 248, 240, 224, 192, 128, 0]
    
    for m in maskl:
        if m not in validmask:
            print('please Enter Valid Subnet Mask')
    
    for i in ipl:
        if i > 255:
            print('Subnet Mask Octets must be < 255')
            print('please Enter Valid IP address')
        
    if len(maskl) != 4:
        print('Subnet Mask must have 4 octets please enter valid Subnet Mask')
    
    elif maskl[0] != 255:
        print('Subnet Mask must start with 255')
        print('please Enter Valid IP address')
                
    else:
        return True
            
    
    
    
    
    

while True:
    
    ip = input('Please Enter an IP address or enter "q" to quit :' )
    if ip  == 'q':
        sys.exit()
        
    ipl = [int(x) for x in ip.split('.')] # loop through ip split cast to int
    
    if validateip(ipl) is True:
        break 

while True:
    
    mask = input('Please Enter an Subnet Mask or enter "q" to quit :' )
    if mask  == 'q':
        sys.exit()
        
    maskl = [int(y) for y in mask.split('.')]
    
    validatemask(maskl)
    
    if validatemask(maskl) is True:
        break


        
