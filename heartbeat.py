import os
import time
import requests

# عنوان الخادم لضمان بقاء الاتصال نشطاً
SERVER_URL = "https://www.google.com"

def send_heartbeat():
    print("--- نظام الاتصال الميداني (مختبر علاء) ---")
    while True:
        try:
            # إرسال نبضة سريعة للتأكد من أن الشبكة "مستيقظة"
            response = requests.get(SERVER_URL, timeout=5)
            if response.status_code == 200:
                print(f"[✓] النبضة مستقرة - الشبكة نشطة الآن: {time.ctime()}")
            else:
                print("[!] تنبيه: ضعف في الإشارة، جاري إعادة التوجيه...")
        except:
            print("[X] انقطاع في المسار الميداني.. جاري البحث عن أقرب برج...")
        
        # الانتظار لمدة دقيقتين قبل النبضة التالية لضمان عدم استهلاك البطارية
        time.sleep(120)

if __name__ == "__main__":
    send_heartbeat()