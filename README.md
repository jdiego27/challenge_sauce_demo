# Challenge Sauce Demo – Automation Test Suite

## 📌 Project Overview
This project is an automated testing framework built to validate the main functionalities of the SauceDemo web application using **Selenium + Pytest** with the **Page Object Model (POM)** design pattern.

The objective of this framework is to demonstrate best practices in UI automation including:
- Clean architecture
- Reusable page objects
- Structured reporting
- Maintainable and scalable test design

---

## 🛠 Technology Stack
- Python 3
- Pytest
- Selenium WebDriver
- Page Object Model (POM)
- Virtual Environment (venv)
- HTML Test Reports

---

```bash
challenge_sauce_demo/
│── config/              # Configuration and environment settings
│── pages/               # Page Object Models
│── tests/               # Test cases
│── reports/             # Generated test reports
│── pytest.ini           # Pytest configuration
│── requirements.txt     # Dependencies list
│── .gitignore           # Ignored files and folders
│── README.md            # Project documentation

--- 
```
## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
git clone https://github.com/jdiego27/challenge_sauce_demo.git  
cd challenge_sauce_demo

### 2️⃣ Create Virtual Environment
python3 -m venv venv  
source venv/bin/activate   # Mac / Linux  
venv\Scripts\activate    # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Create your environment file
cp .env.example .env

### 5️⃣ Update `.env` with your credentials.

## ▶️ Run Tests

Run all tests:
pytest (will run chrome by default)

pytest --browser=chrome
pytest --browser=firefox

Run test with HTML report:
pytest --html=reports/report.html

---

## 🧪 Test Scope
- Login/Logout functionality
- Add a product and products to cart
- Remove a product from the cart
- Checkout process
- Attempt to check out process with missing details
- Error validations
- UI flows for end-to-end purchase

---

## 📊 Reports
After execution, an HTML report will be generated:
reports/report.html

Open it in any browser to view test results.

---

## ✅ Best Practices Implemented
- Page Object Model (POM)
- Clear naming conventions
- Reusable methods
- Scalable structure
- Git version control
- Environment isolation

---

## 👤 Author
Juan Leon Rivas  
Sr. Manual QA Engineer  
Location: Lima, Peru  

---

## 📬 Contact
GitHub: https://github.com/jdiego27  
LinkedIn: https://www.linkedin.com/in/juan-leon-rivas/

---

## 📄 License
This project is for learning and demonstration purposes only.
