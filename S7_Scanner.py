import socket

def s7_port_scanner(target_ip):
    # قائمة بالمنافذ (البوابات) الأكثر أهمية
    common_ports = [21, 22, 80, 443, 8080]
    
    print(f"📡 [S7-SENTINEL] جاري فحص الهدف: {target_ip}")
    print("------------------------------------------")
    
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # سرعة الفحص
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"🔓 البوابة {port}: مفتوحة (نقطة دخول محتملة)")
        else:
            print(f"🔒 البوابة {port}: مغلقة")
        s.close()

    print("------------------------------------------")
    print("✅ تم المسح بنجاح.. بانتظار أوامر السبع")

if __name__ == "__main__":
    # سنضع هنا IP افتراضي للفحص التجريبي
    s7_port_scanner("8.8.8.8") 