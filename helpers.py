import sys
import time
import threading
from termcolor import colored
import os
from colorama import Fore, Style, init

# 🌀 Spinner
class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)

# 🎨 Color Print
init(autoreset=True)

def print_status(message, status="info"):
    colors = {
        "info": Fore.CYAN,
        "ok": Fore.GREEN,
        "warn": Fore.YELLOW,
        "fail": Fore.RED
    }
    color = colors.get(status, Fore.WHITE)
    print(f"{color}[{status.upper()}] {message}{Style.RESET_ALL}")

# 🧠 Banner
def show_banner():
    os.system('clear')
    banner = r"""

            ████████╗██╗     ██╗██╗     ██╗████████╗ ██████╗  ██████╗ ██╗     
            ╚══██╔══╝██║     ██║██║     ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
               ██║   ██║     ██║██║     ██║   ██║   ██║   ██║██║   ██║██║     
               ██║   ██║     ██║██║     ██║   ██║   ██║   ██║██║   ██║██║     
               ██║   ███████╗██║███████╗██║   ██║   ╚██████╔╝╚██████╔╝███████╗
               ╚═╝   ╚══════╝╚═╝╚══════╝╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                              

        ```````````````````````````````;ýâÛHÁÀœ€ðT``````````````````````````````````
        ```````````````````````````uÃÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÖ``````````````````````````````
        `````````````````````````gÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆu```````````````````````````
        ```````````````````````ïÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÃ``````````````````````````
        ``````````````````````ÓÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆŒ`````````````````````````
        ``````````````````````ÅÆ÷`ÑÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆm`ÃÆž````````````````````````
        ``````````````````````ËÆ÷`ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆm`ÃÆœ````````````````````````
        ``````````````````````þÆQ`pÆÆÑÃÛâŠËÆÆÆÆQmpÀMÆÆÆä`ÆÆ¸````````````````````````
        ```````````````````````ÆÆ`¶½````````Æð````````Œü`Æd`````````````````````````
        ``````````````````````````Æ````````LÆŒ````````|œ`Ò``````````````````````````
        `````````````õÆp`````````ÆÆ+``````²ÆÆÆÆ```````HÆ;``````````êÆÆÆu````````````
        ````````````ÆÆÆÆÆå```````ÆÆÆÆ````ÆÆ8HkþÆ‹```¤ÆÆÆw````````ÇÆÆÆÆÆÆ````````````
        ````````````ÆÆÆÆÆÆÆÆ`````ôÆÆÆÆÆÆÆÑ``L``MÆÆÆÆÆÆÆÆ``````7ÆÆÆÆÆÆÆÆÆò```````````
        ```````````ÆÆÆÆÆÆÆÆÆÆÆMÎ{``¨ÑÆÆÆÆÖ``L```ÆÆÆÆÆg```½®ÑÆÆÆÆÆÆÆÆÆÆÆÆÆ‚``````````
        ```````````ÆÆÆÆÆÆÆÆÆÆÆÆÆÆ`“[``¤ÆÆÆõ¨Šõ¸ÆÆÆÆ```â`fÆÆÆÆÆÆÆÆÆÅRÑÆÆÆÇ```````````
        ````````````````````¨&HÆÆ­`Æ`´`}ËÆÆÆÆÆÆÆÆþ```Át`þÆÆpù```````````````````````
        ```````````````````````````ÆÆ`ä``````````³V‡„ÆR`````````````````````````````
        ```````````````````````````ÆÆ3````´``6“``}r`ËÆý`````````````````````````````
        ````````````````````````²n`åÆÆT```…``O–```¨MÆÑ``Üˆ``````````````````````````
        ````````````œœÖ[´ˆumMÆÆÆÆÆZ`YÆÆÆÆÆÆÂþÁŒÆÆÆÆÆœ``ÆÆÆÆÆÆ#{`````````````````````
        ``````````¨ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ„```ÆÆÆÆÆÆÆÆÆÆÆ®```ÌÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ```````````
        ```````````ÖÆÆÆÆÆÆÆÆÆœ``````````````````````````````ÛÆÆÆÆÆÆÆÆÆÆÆÆ```````````
        ````````````ÆÆÆÆÆÆÃ````````````````````````````````````´€ÆÆÆÆÆÆÆ````````````
        ````````````ÜÆÆÆÆ`````````````````````````````````````````ÖÆÆÆÆÆ````````````
        ````````````````````````````````````````````````````````````#ÂÔ`````````````


"""

    print(colored(banner, "red"))
    print(colored("         🔥 TLILITool - Multi Protocol Scanner 🔥\n", "yellow"))

def extract_os_info(scanner, target):
    """
    Extracts OS guess and hostname from the nmap scanner result.
    """
    try:
        os_guess = "Unknown"
        hostname = "Unknown"

        if scanner[target].hostname():
            hostname = scanner[target].hostname()

        if "osmatch" in scanner[target]:
            if scanner[target]["osmatch"]:
                best_guess = scanner[target]["osmatch"][0]
                os_guess = f"{best_guess['name']} ({best_guess['accuracy']}% confidence)"

        return os_guess, hostname

    except Exception:
        return "Unknown", "Unknown"

