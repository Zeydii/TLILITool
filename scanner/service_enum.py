from smb.SMBConnection import SMBConnection
import socket
import requests
from helpers import print_status

def check_ftp(target):
    print_status("Checking FTP anonymous login...", "info")
    try:
        import ftplib
        ftp = ftplib.FTP(target)
        ftp.login()
        print_status("FTP anonymous login allowed.", "ok")
        ftp.quit()
    except Exception:
        print_status("FTP anonymous login failed or FTP not running.", "warn")

def check_http(target):
    print_status("Checking HTTP service...", "info")
    try:
        response = requests.get(f"http://{target}", timeout=3)
        title = response.text.split("<title>")[1].split("</title>")[0] if "<title>" in response.text else "No Title"
        print_status(f"HTTP Response: {response.status_code} | Title: {title}", "ok")
    except Exception:
        print_status("HTTP check failed or service not available.", "warn")
        
from smb.SMBConnection import SMBConnection
from helpers import print_status

def check_smb_shares(target):
    try:
        conn = SMBConnection("", "", "scanner", "scanner", use_ntlm_v2=True)
        connected = conn.connect(target, 445, timeout=5)

        if connected:
            shares = conn.listShares()
            results = []
            for share in shares:
                results.append(share.name)
            conn.close()
            return results
        else:
            return []
    except:
        return []

