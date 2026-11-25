# 📚 Simple Library System (Kitabxana İdarəetmə Sistemi)

![Python](https://img.shields.io/badge/PYTHON-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![LICENSE](https://img.shields.io/badge/LICENSE-MIT-green?style=for-the-badge)
![STATUS](https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=for-the-badge)

> Obyekt yönümlü proqramlaşdırma (OOP) prinsipləri əsasında Python dili ilə yazılmış konsol tipli kitabxana idarəetmə sistemi.

---

## 🚀 Layihə Haqqında

Simple Library System — kitabxana resurslarını (kitablar və tələbələr) effektiv şəkildə idarə etməyə kömək edən modul strukturlu konsol tətbiqidir. Layihə daxilində kitabların və tələbələrin əlavə olunması, ID üzrə axtarışı, kitabların icarəyə verilməsi (`borrow`) və qaytarılması (`return`) kimi vacib funksionallıqlar mövcuddur.

---

## 📁 Layihə Strukturu

Layihənin qovluq və fayl quruluşu aşağıdakı kimidir:

```text
SimpleLibrarySystemWithOOP/
│
├── main.py        # Tətbiqin əsas giriş nöqtəsi və menyu idarəetməsi
├── library.py     # Kitabxana məntiqlərini idarə edən ana class (Library)
├── student.py     # Tələbə məlumatlarını saxlayan class (Student)
└── book.py        # Kitab məlumatlarını saxlayan class (Book)

🛠️ Funksionallıqlar
•➕ Tələbə və Kitab Əlavə Etmə: Sistemə yeni tələbə və kitab məlumatlarının daxil edilməsi.
•📋 Siyahılama: Bütün aktiv kitabların və tələbələrin siyahısının göstərilməsi.
•🔍 ID üzrə Axtarış: Kitab və ya tələbənin ID-sinə əsasən sistemdə axtarılması.
• 📖 Kitab İcarəsi: Tələbənin kitab götürməsi (borrowBook) və geri təhvil verməsi (returnBook).

💻 Quraşdırma və İşə Salma
Repozitoriyanı kompyuterinizə endirin:
git clone [https://github.com/xasiyev70/SimpleLibrarySystemWithOOP.git](https://github.com/xasiyev70/SimpleLibrarySystemWithOOP.git)
Layihə qovluğuna keçid edin:
cd SimpleLibrarySystemWithOOP
Tətbiqi işə salın:
python main.py

👨‍💻 Müəllif
•Əli Xasiyev — @xasiyev70
