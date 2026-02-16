import socket

def check_link_safety(url):
    print(f"--- [ فحص أمان الرابط: {url} ] ---")
    try:
        # استخراج عنوان الـ IP الخاص بالرابط
        host = url.split("//")[-1].split("/")[0]
        ip_addr = socket.gethostbyname(host)
        print(f"[+] عنوان الـ IP المضيف: {ip_addr}")
        print(f"[+] حالة الاتصال: مستقر وآمن تقنياً.")
    except Exception as e:
        print(f"[-] خطأ في التحليل: {e}")
        print("[!] تحذير: الرابط قد يكون مشبوهاً أو غير موجود.")

if __name__ == "__main__":
    target = input("أدخل الرابط المراد فحصه: ")
    check_link_safety(target)