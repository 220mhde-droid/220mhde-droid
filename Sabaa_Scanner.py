import socket
from datetime import datetime

# Lead Developer: Alaa (Al-Sabaa)
# Project: Al-Sabaa Security Scanner for Mol Al-Iraq

def scan_ports(target):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Time Started: {str(datetime.now())}")
    print("-" * 50)
    
    # قائمة بأهم المنافذ الأمنية لفحصها
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 3389, 8080]
    
    try:
        for port in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN (Potential Security Risk!)")
            s.close()
    except Exception as e:
        print(f"\nError: {e}")
    
    print("-" * 50)
    print("Scan Completed Successfully.")

if __name__ == "__main__":
    # هنا يمكنك وضع عنوان IP الخاص بالشبكة المراد فحصها
    target_ip = "127.0.0.1" 
    scan_ports(target_ip)