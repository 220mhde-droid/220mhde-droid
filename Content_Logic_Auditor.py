# أداة محاكاة فحص الثغرات في فلاتر المحتوى
# اسم الملف: Content_Logic_Auditor.py

def analyze_filter_bypass(content_type, severity_score):
    print("--- [ جاري فحص منطق الخوارزمية ] ---")
    
    # محاكاة لثغرة: إذا كان الرابط من منصة موثوقة (مثل فيسبوك) 
    # فإن الفلتر يتجاهل الفحص العميق للمحتوى العنيف بالداخل
    if content_type == "Official_Platform_Link" and severity_score > 8:
        print("[!] تنبيه: تم اكتشاف ثغرة 'الثقة العمياء' (Blind Trust).")
        print("[!] الخوارزمية تسمح بمرور المحتوى العنيف لأنه يحمل رابطاً رسمياً.")
        print("[+] الحل المقترح: تفعيل الفحص العميق (Deep Packet Inspection) للروابط الموثوقة.")
    else:
        print("[+] النظام يعمل بشكل طبيعي (ظاهرياً).")

# اختبار المحاكاة
analyze_filter_bypass("Official_Platform_Link", 9)