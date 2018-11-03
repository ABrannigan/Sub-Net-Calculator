# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 19:08:43 2018

@author: adam
"""
import sys
import numpy as np

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
            
def counthosts(binmaskl_pad):
    
    countzero = 0
    for x in binmaskl_pad:
        if x == '0':
            countzero += 1
    
    numhosts = (2**countzero)-2
    return numhosts
    
def findwildcard(maskl):
    
    broacastmask = np.array([255,255,255,255])
    subnetmask = np.array(maskl)
    wilcardmask = broacastmask - subnetmask
    
    return wilcardmask
    
def findnetadd(ipl,maskl):
    
    ip = np.array(ipl)
    mask  = np.array(maskl)
    netaddress = np.bitwise_and(ip , mask)
    netstr = [str(x) for x in netaddress]
    netstr='.'.join(netstr)
    return netstr

def findbroad(ipl,maskl):
    
    ip = np.array(ipl)           #[10, 1, 129, 1]
    mask = np.array(maskl)       #[255, 255, 128, 0]
    invertmask  = np.invert(np.array(mask, dtype = np.uint8))
    #nota = np.binary_repr(mask.all(),width=8)
    broadaddress = np.bitwise_or(ip , invertmask)
    broadstr = [str(x) for x in broadaddress]
    #broadint = [int(x,10) for x in broadstr]
    broadstr='.'.join(broadstr)
    return broadstr
        

while True:
    
    ip = input('Please Enter an IP address or enter "q" to quit :' )
    if ip  == 'q':
        sys.exit()
        
    ipl = [int(x) for x in ip.split('.')] # loop through ip split cast to int
    
    #call validate mask funtion if ok break loop
    if validateip(ipl) is True:
        break 

while True:
    
    mask = input('Please Enter an Subnet Mask or enter "q" to quit :' )
    if mask  == 'q':
        sys.exit()
        
    maskl = [int(y) for y in mask.split('.')]
    
    #call validate mask funtion if ok break loop
    if validatemask(maskl) is True:
        break

#convert mask and ip octets to binary format and cast to int
binipl = [int(bin(i)[2:]) for i in ipl]
binmaskl = [int(bin(j)[2:]) for j in maskl]

#pad with zeros 
binipl_pad = [str(i).zfill(8) for i in binipl]
binmaskl_pad = [str(j).zfill(8) for j in binmaskl]
binipl_pad = '.'.join(binipl_pad)
binmaskl_pad = '.'.join(binmaskl_pad)

#calculate number of hosts
hosts =counthosts(binmaskl_pad)

#get wildcard
wildcard = findwildcard(maskl)
wildcard_pad = [str(i) for i in wildcard]
wildcard_pad = '.'.join(wildcard_pad)

#grt network address
netaddress = findnetadd(ipl,maskl)

#get broadcast address
broadaddress = findbroad(ipl,maskl)

print('Network Address : ' + netaddress)
print('Broadcast Address : ' + broadaddress) 
print('ip : ' + binipl_pad)
print('mask : ' + binmaskl_pad)
print('Hosts : ' + str(hosts))
print('WildCard Mask : ' + wildcard_pad)

#print(type(binipl[0]))

    
        
