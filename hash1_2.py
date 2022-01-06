import sys
#sys.path.insert(1,'C:\Agiloft\Python\Lib\site-packages')
import hashlib
import time
import rsa

#running web server on own machine rn,

def hashtext(text):
    return(hashlib.sha256(text.encode()).hexdigest())

#append time to text, then hash, not needed, since not trackign time
def appendtime(text):
    text += str(time.time())
    return(hashtext(text))

#for block functionality
def checkuser(name):
    try:
        name.balance
        return(True)
    
    except NameError:
        return(False)
    
def checkbalance(name,amount):
    if(amount > name.balance):
        return(False)
    else:
        return(True)

#basics for user accounts
class User:
    name,balance = 0,0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

#can create user, access users functions

#do I want to do time appended hashes? sure, fuck it, with
#personal keys?, when running, it updates...
class Block:
    transactionhistory = []
    previoushash = ['0'] #nonce val
    currenthash = []
    def __init__(self, user, recipient, amount):
        if(checkuser(user) and checkuser(recipient)):
            if(checkbalance(user,amount)):
                user.balance -= amount
                recipient.balance += amount
                transaction = f'{user.name} sent {amount} to {recipient.name}'
                self.transactionhistory.append(transaction)
                self.currenthash = hashtext(transaction +
                                            self.previoushash[len(self.previoushash)-1])
                self.previoushash.append(self.currenthash)

adam = User("adam",10)
jon = User("jon",10)
        


#convert to integer, with int.from_bytes()
#needs to be byte-code
message = b"This is the message to be encrypted"
public_key, private_key = rsa.newkeys(1024)
encrypted_message = rsa.encrypt(message, public_key)
decrypted_message = rsa.decrypt(encrypted_message, private_key)
#print(encrypted_message, decrypted_message, sep="\n\n")
