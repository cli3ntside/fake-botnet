import os
import time
from datetime import datetime

ascii_art = r"""
                                      :                  L.                     ,;         
                                  i   Ef                 EW:        ,ft       f#i          
                                 LE   E#t                E##;       t#E     .E#t  GEEEEEEEL
                                L#E   E#t     :KW,      LE###t      t#E    i#W,   ,;;L#K;;.
                               G#W.   E#t      ,#W:   ,KGE#fE#f     t#E   L#D.       t#E   
                              D#K.    E#t fi    ;#W. jWi E#t D#G    t#E :K#Wfff;     t#E   
                             E#K.     E#t L#j    i#KED.  E#t  f#E.  t#E i##WLLLLt    t#E   
                           .E#E.      E#t L#L     L#W.   E#t   t#K: t#E  .E#L        t#E   
                          .K#E        E#tf#E:   .GKj#K.  E#t    ;#W,t#E    f#E:      t#E   
                         .K#D         E###f    iWf  i#K. E#t     :K#D#E     ,WW;     t#E   
                        .W#G          E#K,    LK:    t#E E#t      .E##E      .D#;    t#E   
                       :W##########Wt EL      i       tDj..         G#E        tt     fE   
                                                                     fE                   
                                                                                          
"""

WHITE = "\033[97m"
GRAY = "\033[90m"
GREEN = "\033[0;92m"
BLUE = "\033[0;94m"
RESET = "\033[0m"

l4_methods = [
    GRAY + "UDP Flood" + RESET,
    "SYN Flood",
    GRAY + "ICMP Flood" + RESET,
    "Ping of Death",
    GRAY + "ZeroPacket" + RESET,
    "RST Flood",
    GRAY + "ACK Flood" + RESET,
    "Minecraft Flood"
]

l7_methods = [
    "HTTP Flood",
    GRAY + "CLOUDFLARE KILLER" + RESET,
    "DNS Amplification",
    GRAY + "NTP Amplification" + RESET,
    "DDOS GUARD",
    GRAY + "JS (Custom)" + RESET,
]

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(GRAY + ascii_art + RESET)
    print(WHITE + "Welcome to Luxnet" + BLUE + " root" + RESET )
    print(WHITE + "====================================" + RESET )
    print(WHITE + "Layer 4 (Transport Layer) DDoS Methods:" + RESET )
    for i in range(0, len(l4_methods), 2):
        method1 = f"{i + 1}. {l4_methods[i]}"
        method2 = f"{i + 2}. {l4_methods[i + 1]}" if i + 1 < len(l4_methods) else ""
        print(f"{method1:<30} {method2}")
    print(WHITE + "====================================" + RESET )
    print(WHITE + "Layer 7 (Application Layer) DDoS Methods:" + RESET )
    for i in range(0, len(l7_methods), 2):
        method1 = f"{i + len(l4_methods) + 1}. {l7_methods[i]}"
        method2 = f"{i + len(l4_methods) + 2}. {l7_methods[i + 1]}" if i + 1 < len(l7_methods) else ""
        print(f"{method1:<30} {method2}")
    print(WHITE + "====================================" + RESET )
    print(WHITE + "Please select a method by entering the corresponding number, or type 'exit' to quit." + RESET)

def simulate_attack(method, target, port, duration):
    if method.strip() in l7_methods:
        print(GRAY + f"\nATTACK {method} on {target} for {duration} seconds..." + RESET)
    else:
        print(GRAY + f"\nATTACK {method} on {target}:{port} for {duration} seconds..." + RESET)
    time.sleep(duration)
    print(GRAY + f"Attack started on {target} for {duration}s at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" + RESET)
    input(GRAY + "\nPress Enter to return to the main menu..." + RESET)

def authenticate():
    correct_username = "root"
    correct_password = "123"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(GRAY + ascii_art + RESET)
    print(WHITE + "Welcome to Luxnet" + BLUE + " root" + RESET )
    print(WHITE + "====================================" + RESET )
    
    for _ in range(3):
        username = input(GRAY + "Username: " + RESET).strip()
        password = input(GRAY + "Password: " + RESET).strip()
        
        if username == correct_username and password == correct_password:
            return True
        else:
            print(WHITE + "Invalid credentials, please try again." + RESET)
    
    print(WHITE + "Too many failed attempts. Exiting." + RESET)
    return False

def main():
    if not authenticate():
        return
    
    while True:
        display_menu()
        print(GRAY + "root@luxnet ~#" + RESET, end=" ")
        choice = input().strip()
        if choice.lower() == 'exit':
            print(GRAY + "Exiting Luxnet. Goodbye!" + RESET)
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(l4_methods) + len(l7_methods):
                method = (l4_methods + l7_methods)[choice - 1]
                if method.strip() in l7_methods:
                    print(GRAY + "ATTACK" + RESET, end=" ")
                    target = input("Enter target website: ").strip()
                    port = None
                else:
                    print(GRAY + "ATTACK" + RESET, end=" ")
                    target = input("Enter target IP: ").strip()
                    print(GRAY + "ATTACK" + RESET, end=" ")
                    port = input("Enter target port: ").strip()
                
                print(GRAY + "ATTACK" + RESET, end=" ")
                duration = input("Enter duration in seconds: ").strip()
                if target and (port.isdigit() if port else True) and duration.isdigit():
                    simulate_attack(method, target, int(port) if port else None, int(duration))
                else:
                    print(WHITE + "Invalid input, please try again." + RESET)
            else:
                print(WHITE + "Invalid choice, please try again." + RESET)
        else:
            print(WHITE + "Invalid choice, please try again." + RESET)

if __name__ == "__main__":
    main()
