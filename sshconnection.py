#import sys
#sys.path.insert(1,'C:\Agiloft\Python\Lib\site-packages')
import paramiko
import hash1_2

#replace as needed, requires server in local network
serverip = "192.168.0.28"
serverusername = "ale"
serverpassword = "1235"

ssh = paramiko.SSHClient()

ssh.load_system_host_keys()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(serverip,
            username=serverusername,
            password=serverpassword,
            look_for_keys=False)

stdin, stdout, stderr = ssh.exec_command("show ip route")

ssh.exec_command("cd /home/ale/")

#filename is Blockchain.txt

def readchain():
    stdin, stdout, stderr = ssh.exec_command("cat Blockchain.txt")
    return(stdout.read())

def writechain(text):
    ssh.exec_command(f"echo {text} &>> Blockchain.txt")
    return

#danger with this, resets file
def resetchain():
    ssh.exec_command("rm Blockchain.txt")
    ssh.exec_command("touch Blockchain.txt")
    return

#to append to file, echo "a" &>> file.txt
#to get data, a,b,c = ssh.exec_command("cat new.txt"), THEN
#b.read()

#output = ssh_stdout.readlines()
#ssh.close()

adam = hash1_2.User("jimbo",10)
tang = hash1_2.User("tang",10)
userlist = []

def createuser():
    name = input("Enter a name: ")
    balance = int(input("Enter your starting balance: "))
    a = hash1_2.User(name, balance)
    userlist.append(a)
    return(a)

def checkbalance(user):
    #print userlist[user].balance
    return
#same for check funds


def main():
    while(True):
        choice = int(input("1.Create User\n2.Check Balance\n" +
                           "3.Transfer funds\n4.Deposit funds\n" +
                           "5.Withdraw funds\n6.View Chain\n"))
        
