import sys
sys.path.insert(1,'C:\Agiloft\Python\Lib\site-packages')
import paramiko

routerip = "192.168.0.28"
routerusername = "ale"
routerpassword = "1235"

ssh = paramiko.SSHClient()

ssh.load_system_host_keys()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(serverip,
            username=serverusername,
            password=serverpassword,
            look_for_keys=False)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show ip route")

output = ssh_stdout.readlines()

ssh.close()
