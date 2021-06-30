
#imports the Netmiko libraries for SSH and CLI commands
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko import Netmiko
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

import re

from bottle import debug, route, run, template, debug, post, get, request,response, redirect, auth_basic


def check(user, password): 
    if user == "kite" and password == "password":
        return True
    elif user == "john" and password == "strasser":
        return True
    else:
        return False
    #return user == "kite" and password == "password" #or user == "john" and password == "strasser"

@get('/')
@auth_basic(check)
def get_default():



    return template("index")



@post("/")
def post_switch_data():
    
    IP = request.forms.get('IP')

    username = request.forms.get('username')

    password = request.forms.get('password')
   
        #data= {
        # 'items':[
            #    {'task':'Figure out how to write Python with database','done': 0},
            #   {'task':'Practice the syntax for this','done': 0},
            #    {'task':'Continue to work on this stupid database stuff','done': 0},
        # ]
    #  }






    switch = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': username, 
        'password': password,
        'secret': password,

    }

    switchtelnet = {
        'device_type': 'cisco_ios_telnet',
        'ip': IP,
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
    hostname=hostname.strip('hostname ')


    net_connect.disconnect()


    interfaces=interfaces1.splitlines()
    interfaces= interfaces[1:]



    interfacearray = []
    vlanarray=[]
    for i in interfaces:

        #i=i.split(' ')
        i=i.split()
        print(i[0])
        interfacearray.append(i[0])
        
        if 'notconnect' in i:

            t=i.index('notconnect')
            vlanarray.append(i[t+1])
            
        
        elif 'connected' in i:

            t= i.index('connected')
            vlanarray.append(i[t+1])
        
        
        elif 'disabled' in i:

            t=i.index('disabled')
            vlanarray.append(i[t+1])
        
        else:

            t=i.index('inactive')
            vlanarray.append(i[t+1])

    print(vlanarray) 




    data = interfacecounters.splitlines()


    logdata=''
    for i in data:
    # print(i)
        if i not in logdata:
            #print('In If Statement - printing i again '+ i)
            logdata+=i
            logdata+='\n'

    #print('about to print log data')
    print (logdata)




    print(interfacearray)

    thisdict={}
    j=0
    for i in interfacearray:
        
        #print(interfaces[i])
        y = re.findall(r'\b' +i+ r'\b', logdata)
        if len(y) < 2:

            thisdict.update({
                i:{
                    "Utilized":'No',
                    "Vlan": vlanarray[j]
                }
            })
            print(i+' is NOT being utilized.')
        
            
    

        else:

            thisdict.update({
                i:{
                    "Utilized":'Yes',
                    "Vlan": vlanarray[j]
                }
            })
            print(i +' IS being utilized.')
        
        j = j + 1
        
        

    print(thisdict)

    #items = [ dict(x) for x in list(thisdict) ]

    return template("response.tpl", data=thisdict, hostname=hostname, uptime=uptime)

debug(True)
run (host="localhost", port=8098, reloader=True)
