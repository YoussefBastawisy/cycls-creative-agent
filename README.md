#  Cycls Creative Agent

Welcome to the **Cycls Creative Agent**! This is an intelligent and engaging marketing content generator powered by Google Gemini Pro and Streamlit. Designed to help marketing teams, creatives, and agencies come up with **unique advertising ideas** for various campaigns using the power of AI.

---

## 🌐 Live App

Access the deployed app here: [https://cycls-creative-agent.streamlit.app/](https://cycls-creative-agent.streamlit.app/)

---

## 🔍 Objective

To streamline the process of creating **creative ad copy** by simply entering a few campaign details and letting the AI generate **tailored, on-brand, and compelling marketing messages**.

---

## 📚 Features

* 📑 **Ad Copy Generation** based on:

  * Client Name
  * Product Description
  * Target Audience
  * Brand Voice/Tone
  * Ad Type (Storytelling, Humorous, Educational, Emotional, Direct)
* 🚀 Real-time AI-powered response using **Gemini Pro (Google Generative AI)**
* ✍️ Fully interactive user interface via **Streamlit**
* دعم للغة العربية (مخصص للسوق العربي)\*\*

---

## 📊 Technologies Used

| Tool                | Version | Purpose                 |
| ------------------- | ------- | ----------------------- |
| Streamlit           | Latest  | Web app frontend        |
| google-generativeai | 0.8.5  | Access to Gemini Pro AI |
| Python              | 3.10+   | Backend logic           |

---

## 🚧 How to Run Locally

### 1. Clone the repository:

```bash
git clone https://github.com/YoussefBastawisy/creative-agent.git
cd creative-agent
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up your API key:

Replace this line in `Creative_agent.py` with your actual key:

```python
genai.configure(api_key="YOUR_GOOGLE_API_KEY")
```

### 4. Run the app:

```bash
streamlit run Creative_agent.py
```

---

## 🎓 Prompt Strategy

The app uses different templates based on the selected ad type:

* **Storytelling:** Friendly, fun narrative-driven tone
* **Humorous:** Lighthearted, sarcastic, comedic copy
* **Educational:** Informative, clear, and structured explanation
* **Emotional:** Empathy-driven messaging that touches the heart
* **Direct:** Clear and urgent CTA-driven ad content

---

## ✨ Sample Usage

Enter the following:

* **Client:** Nike
* **Product:** Lightweight running shoes
* **Audience:** Gen Z athletes
* **Tone:** Energetic
* **Type:** قصصي

> The result? A vibrant, story-driven message that hooks the reader emotionally and reflects the tone and brand.

---

## 📈 Future Enhancements

* Multi-language support
* Ad export to PDF/CSV
* Campaign history and analytics

---

## 📢 Contributions

Feel free to fork this repo, open issues, and submit PRs. All contributions are welcome to enhance functionality, templates, or UX.

---

## 📍 Author

**Youssef Bastawisy**
[LinkedIn](www.linkedin.com/in/youssef-bastawisy)

---

## 🌐 License

MIT License - free to use, share, and modify.

---

> "Creativity is intelligence having fun" — Albert Einstein

---
