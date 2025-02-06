## پروژه چت گروهی با Django و Django Channels

این پروژه یک اپ ساده چت گروهی مبتنی بر Django و Django Channels می‌باشد که امکان ارسال و دریافت پیام‌های متنی به صورت Real-time در گروه‌های مختلف را فراهم می‌کند.

### امکانات

- **چت گروهی Real-time:** امکان برقراری ارتباط و ارسال پیام‌های متنی به صورت بلادرنگ در اتاق‌های چت مختلف.
- **مدیریت کاربران:** امکان ثبت‌نام، ورود و خروج کاربران از طریق فرم‌های موجود.
- **استفاده از WebSocket:** استفاده از Django Channels برای مدیریت ارتباطات بلادرنگ.
- **ناوبری آسان:** صفحات طراحی شده برای ورود به چت، ایجاد اتاق‌های چت و مشاهده تاریخچه گفتگو.

### ساختار پروژه

```
django_group_chat/
├── django_group_chat
│   ├── chat
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── consumers.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── routing.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── core
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── routing.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   └── templates
│       ├── account
│       │   ├── login.html
│       │   ├── logout.html
│       │   └── register.html
│       ├── base.html
│       └── chat
│           ├── 404.html
│           ├── chat.html
│           ├── index.html
│           └── join_chat.html
├── LICENSE
├── README.md
└── requirments.txt
```

### پیش نیازها

برای اجرای این پروژه به موارد زیر نیاز دارید:

- **Python**
- **Django**
- **Django Channels**
- **Redis Server** (برای مدیریت ارتباطات WebSocket)
- **Daphne** (به عنوان سرور ASGI)

### نصب و راه‌اندازی

#### 1. کلون کردن مخزن

```bash
git clone https://github.com/eric-py/DjangoGroupChat.git
cd django_group_chat
```

#### 2. ایجاد محیط مجازی و نصب وابستگی‌ها

```bash
python -m venv .venv
source .venv/bin/activate  # در ویندوز: .venv\Scripts\activate
pip install -r requirments.txt
```

#### 3. راه‌اندازی Redis

اطمینان حاصل کنید که Redis بر روی سیستم شما نصب و در حال اجرا است. (در صورت نیاز می‌توانید از کانتینر داکر نیز استفاده کنید.)

#### 4. اجرای Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. اجرای اپلیکیشن

```bash
python manage.py runserver
```

### استفاده

1. پس از اجرای سرور، مرورگر خود را باز کنید و به آدرس `http://127.0.0.1:8000/` مراجعه نمایید.
2. از طریق فرم‌های ثبت‌نام و ورود که در بخش حساب کاربری موجود است، وارد سیستم شوید.
3. پس از ورود به سیستم، به صفحه‌ی اصلی چت گروهی هدایت خواهید شد.
4. در صفحه‌ی چت، با انتخاب یا ایجاد یک اتاق چت، می‌توانید پیام‌های خود را به صورت بلادرنگ ارسال و دریافت کنید.