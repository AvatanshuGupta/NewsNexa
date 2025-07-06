# 📰 NewsNexa

**NewsNexa** is a modern, responsive Django-based news web application that fetches real-time headlines using the [NewsData.io API](https://newsdata.io). It offers intuitive browsing, category filtering, and keyword-based search in a beautiful, mobile-friendly interface.

---

## 🌐 Live Demo

Check out the live project here 👉 [NewsNexa on Render](https://newsnexa.onrender.com)

---


## 🚀 Features

- 🔍 **Keyword Search** – Easily find articles by typing keywords
- 🧩 **Browse by Category** – Filter news by categories (e.g. Business, Sports, Health)
- 🖼️ **Fallback Images** – Auto image fallback when API doesn't return one
- 📄 **Paginated Results** – Supports "Next Page" functionality for all views
- 🌈 **Dynamic Backgrounds** – Gradient animations enhance the UI
- 📱 **Fully Responsive** – Optimized for mobile and desktop

---

## 📂 Folder Structure

```
NewsNexa/
│
├── newsapp/
│   ├── templates/
│   │   ├── home.html
│   │   ├── category.html
│   │   ├── keyword.html
│   │   └── nextPage.html
│   ├── static/
│   │   ├── home.css
│   │   ├── category.css
│   │   ├── keyword.css
│   │   ├── nextPage.css
│   │   └── images/
│   │       ├── fallbackImage.png
│   │       └── categories/
│   │           └── [category].jpg
│   └── views.py
│
├── NewsNexa/            ← Project config and URLs
├── manage.py
└── requirements.txt
```

---

## 🛠️ Tech Stack

| Tool           | Usage                                 |
|----------------|----------------------------------------|
| Django         | Backend framework                     |
| Bootstrap 5    | Frontend layout and responsiveness    |
| HTML + CSS     | UI rendering and custom styles        |
| NewsData.io    | Real-time news API                    |
| Python         | Language for backend logic            |



---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AvatanshuGupta/NewsNexa.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your NewsData.io API key

Edit `settings.py` or use a `.env` file:

```python
# settings.py
NEWS_API_KEY = 'your_newsdata_io_api_key'
```

Or:

```
# .env
NEWS_API_KEY=your_newsdata_io_api_key
```

### 5. Run the server

```bash
python manage.py runserver
```


---

## 📈 API Usage & Rate Limiting

- NewsData.io’s free tier allows **200 API calls/day**
- You’ll receive a message like `RateLimitExceeded` if the limit is crossed
- Consider upgrading or caching requests

---

