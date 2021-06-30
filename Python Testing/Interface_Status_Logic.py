
#imports the Netmiko libraries for SSH and CLI commands
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko import Netmiko
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

import re


username=input('What is the username of the switch? ')

password=input('What is the password of the switch? ')


switch = {
    'device_type': 'cisco_ios',
    'ip': '10.5.0.8',
    'username': username, 
    'password': password,
    'secret': password,

}

switchtelnet = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.5.0.8',
    'username': username, 
    'password': password,
    'secret': password,

}


try:
        net_connect = Netmiko(**switch)
except (NetMikoTimeoutException):
    print('The switch is most likely using Telnet')
    print('\n')
    try:
        net_connect = Netmiko(**switchtelnet)
    except (NetMikoTimeoutException):
        print('The switch is probably not online')
        print('\n')

interfacecounters=net_connect.send_command('show interface counters | e Po')
interfaces1=net_connect.send_command('show interfaces status | e Po')
uptime=net_connect.send_command('show ver | i uptime is')
hostname=net_connect.send_command('show run | i hostname')


net_connect.disconnect()


interfaces=interfaces1.splitlines()
interfaces= interfaces[1:]



interfacearray = []
vlanarray=[]
for i in interfaces:

    #i=i.split(' ')
    i=i.split()
    
    interfacearray.append(i[0])
    
    if 'notconnect' in i:

        t=i.index('notconnect')
        vlanarray.append(i[t+1])
        
    
    elif 'connected' in i:

       t= i.index('connected')
       vlanarray.append(i[t+1])
    
    
    else:

        t=i.index('disabled')
        vlanarray.append(i[t+1])


print(vlanarray) 



#print('Right before print interface')
#print(interfaces[0])
#print('Print right after interfaces')
#rint('interfaces')
#print('print second interface')
#print(interfaces)
#print(interfaces[6])
#print(interfaces[1])
#print(interfaces[2])
#print(interfaces[3])

data = interfacecounters.splitlines()
#print('Printer after line split')
#print(data)




# for line in data:
    
#     currentinterface=interfaces[0]
#     #print(currentinterface)
#     if currentinterface in line:
#         print('gets to if statement')
#         print(interfaces[0])
            
#     #print(line)
#         logdata+=line
    
#     #logdata+='\n'


# #This WORKS!!!
# logdata=[]
# for i in data:
#    # print(i)
#     if i not in logdata:
#         print('In If Statement - printing i again '+ i)
#         logdata.append(i)
# '''

logdata=''
for i in data:
   # print(i)
    if i not in logdata:
        #print('In If Statement - printing i again '+ i)
        logdata+=i
        logdata+='\n'

#print('about to print log data')
print (logdata)




#####Working as before.
#logdata = logdata.splitlines()
#y = re.findall(r'\b' + interfaces[0] + r'\b', logdata)
#print(len(y))
#x = logdata.count(i)
#print(x)


#t=len(interfaces)

#print(t)
print(interfacearray)

thisdict={}
j=0
for i in interfacearray:
    
    #print(interfaces[i])
    y = re.findall(r'\b' +i+ r'\b', logdata)
    if len(y) < 2:

        thisdict.update({
            i:{
                "Utilized":0,
                "VLAN": vlanarray[j]
            }
        })
        print(i+' is NOT being utilized.')
       
        
        
        #if i[0]+ ' is NOT utilized.' not in finalarray or i[0]+ ' is being utilized.' not in finalarray:
            #finalarray.append(i[0] + ' is NOT utilized.')
            #print(i[0]+' is NOT currently being utilized.')


    else:

        thisdict.update({
            i:{
                "Utilized":1,
                "VLAN": vlanarray[j]
            }
        })
        print(i +' IS being utilized.')
       
    j = j + 1
    
       
       # i=i.split(' ')
        #if i[0]+ ' is NOT utilized.' not in finalarray or i[0]+ ' is being utilized.' not in finalarray:
           # finalarray.append(i[0] + ' is being utilized.')
        #print(i[0]+' IS currently being utilized.')





################## After CHanges




'''

logdata = logdata.splitlines()
finalarray=[]

for i in logdata:
    if '0              0              0              0' in i:

        i=i.split(' ')
        if i[0]+ ' is NOT utilized.' not in finalarray or i[0]+ ' is being utilized.' not in finalarray:
            finalarray.append(i[0] + ' is NOT utilized.')
            #print(i[0]+' is NOT currently being utilized.')


    else:
        i=i.split(' ')
        if i[0]+ ' is NOT utilized.' not in finalarray or i[0]+ ' is being utilized.' not in finalarray:
            finalarray.append(i[0] + ' is being utilized.')
        #print(i[0]+' IS currently being utilized.')


# Idea - maybe split into all those that have 0 counters, and those that dont. Do the ones that have zero first and set a value Dictionary? Then the ones that dont 0s will get over written?

print(finalarray)

'''
print(thisdict)


#items = [ dict(x) for x in list(thisdict) ]

#print(items)
'''for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])

for inter, interinfo in thisdict.items():
    print (inter)
    for key in interinfo:
    #for j in thisdict[i]:
        print(interinfo[key])
        <td>{{interinfo[key]}} </td>
        '''
        
    


input('Hit Enter to close window.')
