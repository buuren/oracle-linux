#!/usr/bin/python
try:
        nmConnect('weblogic_username', 'weblogic_pasword', domainName='weblogic_domain')
        connected = 1
except:
        connected = 0
        print('Could not connect to the NodeManager.')

if connected==1:
        server = sys.argv[1]
        print('Current server status: ')
        serverStatus=nmServerStatus(server)
        try:
                if serverStatus=='RUNNING':
                        nmKill(server)
                        nmStart(server)
                elif serverStatus=='SHUTDOWN':
                        nmStart(server)
                elif serverStatus=='STARTING':
                        print('Server startup has been initiated by another process.')
        except: print('Error restarting.')

        nmDisconnect()
        exit()
else:
        print('Check your connection settings')
