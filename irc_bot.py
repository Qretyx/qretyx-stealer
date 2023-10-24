import socket
import sys
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def baglan(server,botnick):
    print("connecting to:"+server)
    irc.connect((server, 6667))#connects to the server
    irc.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n", "UTF-8"))
    irc.send(bytes("NICK "+ botnick +"\n", "UTF-8"))
    irc.send(bytes("PRIVMSG nickserv :iNOOPE\r\n", "UTF-8"),)#auth
def kanal_mesaj(mesaj,kanal):
    global irc
    irc.send(bytes('PRIVMSG '+kanal+" "+":"+mesaj+ "\r\n", "UTF-8"))
def ozel_mesaj(mesaj,kisi):
    global irc
    irc.send(bytes('PRIVMSG '+kisi+" "+":"+mesaj+ "\r\n", "UTF-8"))
def kanal_giris(kanal):
    global irc
    irc.send(bytes("JOIN "+ kanal +"\n", "UTF-8"))
def mesaj_al():
    global irc
    return str(irc.recv(2040).decode("UTF-8"))

       
