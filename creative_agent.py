import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyD_R0vghIN9qGi7mNxQWnuE5b85pGJNHJs")

model = genai.GenerativeModel(model_name="gemini-2.5-pro")

st.set_page_config(page_title="Cycls Creative Agent", layout="centered")
st.title(" Cycls Creative Agent")
st.write("قم بإدخال تفاصيل الحملة واختر نوع الإعلان وسنقوم بابتكار فكرة تسويقية مميزة معًا ")

client_name = st.text_input(" اسم العميل")
product_description = st.text_area(" وصف المنتج")
target_audience = st.text_area(" الجمهور المستهدف")
brand_tone = st.text_input(" صوت العلامة ")
ad_type = st.selectbox(" نوع الإعلان", ["قصصي", "فكاهي", "تثقيفي", "عاطفي", "مباشر"])


def build_prompt(ad_type, client_name, product_description, target_audience, brand_tone):
    templates = {
        "قصصي": f"""اكتب إعلانًا تسويقيًا بأسلوب قصصي، شبابي، منعش، ومرِح ✨
اسم العميل: {client_name}
وصف المنتج: {product_description}
الجمهور المستهدف: {target_audience}
نبرة العلامة التجارية: {brand_tone}""",

        "فكاهي": f"""اكتب إعلانًا تسويقيًا مضحكًا وساخرًا عن منتج {product_description} من {client_name}.
استهدف {target_audience} بنبرة {brand_tone}، واجعل الضحكة جزء من الرسالة الإبداعية ✨""",

        "تثقيفي": f"""اكتب إعلانًا تسويقيًا تثقيفيًا عن منتج {product_description}، يوضح فائدته وأهميته بأسلوب مهني ومقنع.
العلامة التجارية: {client_name}
الجمهور المستهدف: {target_audience}
نبرة الحملة: {brand_tone}""",

        "عاطفي": f"""اكتب إعلانًا تسويقيًا مؤثرًا وعاطفيًا عن منتج {product_description} من {client_name}.
يستهدف {target_audience} بنبرة {brand_tone} ويخاطب القلب والمشاعر ✨""",

        "مباشر": f"""اكتب إعلانًا تسويقيًا مباشرًا وواضحًا لمنتج {product_description} من {client_name}.
الجمهور: {target_audience}
النبرة: {brand_tone}
اربط الرسالة بعرض أو دعوة لاتخاذ قرار فوري 🔥"""
    }
    return templates.get(ad_type, "")


def generate_creative_copy(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"تأكد من الاتصال بالانترنت {e}"


if st.button("🚀 انطلق يا مبدع"):
    if not all([client_name.strip(), product_description.strip(), target_audience.strip(), brand_tone.strip()]):
        st.warning("⚠️ من فضلك املأ جميع الحقول أولاً.")
    else:
        prompt = build_prompt(ad_type, client_name, product_description, target_audience, brand_tone)
        with st.spinner("⏳ جاري توليد الفكرة الإبداعية..."):
            creative_text = generate_creative_copy(prompt)
        st.markdown("### ✨ الفكرة الإبداعية")
        st.markdown(
            f"""
            <div style='
                direction: rtl;
                text-align: right;
                font-size: 20px;
                padding: 10px;
                border-radius: 8px;
                line-height: 1.6;
                color: #333;
                background-color: #f9f9f9;
                border: 1px solid #eee;
            '>{creative_text}</div>
            """,
            unsafe_allow_html=True
        )