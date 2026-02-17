# ✅ CORRETO
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ❌ ERRADO (NUNCA faça isso)
genai.configure(api_key="AIzaSy...")
client = OpenAI(api_key="sk-proj-...")
