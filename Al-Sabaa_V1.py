import base64
import os

def alaa_lab_system():
    print("--- 🛡️ منظومة علاء المتكاملة | V1 ---")
    print("1. الدرع (تشفير رسالة)")
    print("2. الرادار (صيد شبكات Wi-Fi)")
    print("3. فك التشفير (قراءة)")
    
    choice = input("\nاختر الأمر المطلوب: ")
    
    if choice == "1":
        msg = input("ادخل الرسالة السرية: ")
        encoded = base64.b64encode(msg.encode()).decode()
        print(f"\n[✓] النص المشفر للرفع:\n{encoded}")
        
    elif choice == "2":
        print("\n[📡] جاري مسح المحيط بحثاً عن إشارة...")
        # محاولة رصد الشبكات القريبة
        networks = os.popen('nmcli device wifi list || dumpsys wifi | grep SSID').read()
        if networks:
            print(networks)
        else:
            print("[!] الرادار يعمل.. ابحث في منطقة مكشوفة.")
            
    elif choice == "3":
        code = input("ادخل الشفرة لفكها: ")
        try:
            decoded = base64.b64decode(code.encode()).decode()
            print(f"\n[✓] الرسالة الأصلية: {decoded}")
        except:
            print("[X] خطأ في المفتاح!")

if __name__ == "__main__":
    alaa_lab_system()