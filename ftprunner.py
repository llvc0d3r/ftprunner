import ftplib
from rich import print

from daten import host1
from daten import username1
from daten import passwort1

from daten import host2
from daten import username2
from daten import passwort2

from daten import host3
from daten import username3
from daten import passwort3


def HostUpload1():
    ftp = ftplib.FTP(host1, username1, passwort1)
    print ("FTP Directory: ")
    files = ftp.dir()
    print (files)

    filename = "index.html"
    
    with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
        ftp.storbinary(f"STOR {filename}", file)
        ftp.dir()
        ftp.quit()

        print("[green] File Uploaded to FTP")

HostUpload1()



def HostUpload2():
    ftp = ftplib.FTP(host2, username2, passwort2)
    print ("FTP Directory: ")
    files = ftp.dir()
    print (files)

    filename = "index.html"
    
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR {filename}", file)
        ftp.dir()
        ftp.quit()
        print("[green] File Uploaded to FTP")

HostUpload2()



def HostUpload3():
    ftp = ftplib.FTP(host3, username3, passwort3)
    print ("FTP Directory: ")
    files = ftp.dir()
    print (files)

    filename = "index.html"
    
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR {filename}", file)
        ftp.dir()
        ftp.quit()
        print("[green] File Uploaded to FTP")

HostUpload3()


