# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 19:08:43 2018

@author: adam
"""
import sys
import numpy as np

def validateip(ipl):
    '''this funtion vlidates the ip address by checking each condition'''
    
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
    '''this funtion vlidates the subnetmask address by checking each condition'''
    #predefine valid mask to check against
    validmask = [255, 254, 248, 240, 224, 192, 128, 0]
    
    for m in maskl:
        if m not in validmask:
            print('please Enter Valid Subnet Mask')
    
    for i in maskl:
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
    '''this function calculates the number of usable hosts'''
    #count zeros 
    countzero = 0
    for x in binmaskl_pad:
        if x == '0':
            countzero += 1
    #calculate usable hosts and return 
    numhosts = (2**countzero)-2
    return numhosts
    
def findwildcard(maskl):
    '''this funtion calculates the wildcardmask'''
    #calculate by subtrating broadcast address subnetmask
    broacastmask = np.array([255,255,255,255])
    subnetmask = np.array(maskl)
    wilcardmask = broacastmask - subnetmask
    #retuns the result
    return wilcardmask
    
def findnetadd(ipl,maskl):
    '''this function calculates the network address by performaing a logic and operation
        on the IP and Subnetmask'''
     #convert to numpy arrays   
    ip = np.array(ipl) 
    mask  = np.array(maskl)
    #perform and operation
    netaddress = np.bitwise_and(ip , mask)
    #format as address
    netstr = [str(x) for x in netaddress]
    netstr='.'.join(netstr)
    #return result
    return netstr

def findbroad(ipl,maskl):
    '''this funtion calculates the broadcast address by performing a logic or operation 
        on the IP and the invers of the subnet mask'''
     #convert to numpy arrays
    ip = np.array(ipl)           #eg.[10, 1, 129, 1]
    mask = np.array(maskl)       #eg.[255, 255, 128, 0]
    #invert mask and perform logic or to find 
    invertmask  = np.invert(np.array(mask, dtype = np.uint8))
    broadaddress = np.bitwise_or(ip , invertmask)
    #format like an address
    broadstr = [str(x) for x in broadaddress]
    broadstr='.'.join(broadstr)
    return broadstr
        
def netcalc():
    ''' this funtion performs the main operations of the program 
        gets user inputs, does some formatting, calls the other functions 
        and displays the output to the user'''
        
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
    
    #call get network address
    netaddress = findnetadd(ipl,maskl)
    
    #call get broadcast address
    broadaddress = findbroad(ipl,maskl)
    
    print(' ')
    print('Network Address : ' + netaddress)
    print('Broadcast Address : ' + broadaddress) 
    print('Binary IP : ' + binipl_pad)
    print('Binary Subnet Mask : ' + binmaskl_pad)
    print('Hosts : ' + str(hosts))
    print('WildCard Mask : ' + wildcard_pad)
    
    #print(type(binipl[0]))

#if run call netcalc function  elif imported  ignore
if __name__ == '__main__':
    netcalc()   
        
