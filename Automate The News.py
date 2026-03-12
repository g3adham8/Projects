from selenium import webdriver  # استيراد الأداة الرئيسية للتحكم في المتصفح
from selenium.webdriver.chrome.options import Options  # استيراد إعدادات متصفح كروم
# استيراد مكتبة باندا لمعالجة البيانات وتحويلها لجداول (CSV)
import pandas as pd
from datetime import datetime  # استيراد مكتبة الوقت لإضافة التاريخ لاسم الملف
import os  # مكتبة للتعامل مع مسارات الملفات في نظام التشغيل
import sys  # مكتبة للتعامل مع بيئة تشغيل البرنامج

# تحديد المسار الذي يعمل فيه البرنامج (مفيد عند تحويل الكود لبرنامج EXE)
application_path = os.path.dirname(sys.executable)

# الحصول على تاريخ اليوم وتنسيقه (سنة-شهر-يوم) لاستخدامه في تسمية الملف
now = datetime.now().strftime("%Y-%m-%d")

# الرابط المراد استخراج البيانات منه (قسم كرة القدم)
website = 'https://www.thesun.co.uk/sport/football/'

# ضبط إعدادات المتصفح
options = Options()
# تشغيل المتصفح في الخلفية (بدون ظهور نافذة أمامك)
options.add_argument("--headless=new")
# تعطيل معالج الرسوميات (لزيادة السرعة والاستقرار)
options.add_argument("--disable-gpu")

# تشغيل متصفح كروم باستخدام الإعدادات المحددة
driver = webdriver.Chrome(options=options)

# فتح الرابط المختار في المتصفح
driver.get(website)

# البحث عن جميع "الحاويات" (Divs) التي تحتوي على بيانات الأخبار باستخدام XPath
containers = driver.find_elements(
    by='xpath', value="//div[@class = 'story__copy-container']")

# إنشاء قوائم فارغة لتخزين البيانات المستخرجة
titles = []
sub_titles = []
links = []

# حلقة تكرارية للمرور على كل "حاوية" خبر واستخراج محتواها
for container in containers:
    # استخراج النص الموجود داخل وسم الـ p (غالباً يكون العنوان أو وصف قصير)
    title = container.find_element(by='xpath', value=".//p").text
    # استخراج النص الموجود داخل وسم الـ h3 (العنوان الرئيسي للخبر)
    sub_title = container.find_element(by='xpath', value=".//h3").text
    # استخراج رابط الخبر من وسم الـ a
    link = container.find_element(
        by='xpath', value=".//a").get_attribute("href")

    # إضافة البيانات المستخرجة إلى القوائم التي أنشأناها مسبقاً
    titles.append(title)
    sub_titles.append(sub_title)
    links.append(link)

# تجميع القوائم في "قاموس" (Dictionary) لتسهيل تحويلها لجدول
my_dict = {"Title": titles, "Sub Title": sub_titles, "Link": links}

# تحويل القاموس إلى جدول بيانات (DataFrame) باستخدام pandas
df_headlines = pd.DataFrame(my_dict)

# دمج مسار البرنامج مع اسم الملف الجديد الذي يحتوي على التاريخ
file_path = os.path.join(application_path, f"football_new_{now}.csv")

# حفظ الجدول في ملف CSV مع دعم اللغة العربية (utf-8-sig)
df_headlines.to_csv(file_path, index=True, encoding='utf-8-sig')

# إغلاق المتصفح وإنهاء الجلسة بعد الانتهاء
driver.quit()
