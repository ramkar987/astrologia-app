"""
Teste específico para Groq API (GRATUITA!)
"""
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Teste Groq", page_icon="⚡", layout="wide")

st.title("⚡ Teste Groq API (GRATUITA - 14.400 requests/dia)")
st.markdown("### Configure GROQ_API_KEY nos Secrets e teste!")

# Verificar secret
st.markdown("---")
st.markdown("## 📋 Status")

if "GROQ_API_KEY" in st.secrets:
    st.success("✅ GROQ_API_KEY configurada")
    st.caption(f"Primeiros chars: `{st.secrets['GROQ_API_KEY'][:15]}...`")
    
    key_length = len(st.secrets["GROQ_API_KEY"])
    st.caption(f"✅ Tamanho correto: {key_length} caracteres")
else:
    st.error("❌ GROQ_API_KEY não encontrada!")
    st.markdown("""
    **Configure nos Secrets:**
    ```
    GROQ_API_KEY = "gsk_sua_key_aqui"
    ```
    """)
    st.stop()

st.markdown("---")

# Listar modelos disponíveis
st.markdown("## 📋 Modelos Disponíveis")

if st.button("🔍 Listar Modelos Groq", type="secondary"):
    with st.spinner("Listando modelos..."):
        try:
            client = OpenAI(
                api_key=st.secrets["GROQ_API_KEY"],
                base_url="https://api.groq.com/openai/v1"
            )
            
            response = client.models.list()
            
            st.success("✅ Conexão OK! Modelos encontrados:")
            
            modelos_gratis = []
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🔥 **Modelos GRATUITOS Recomendados**")
                recomendados = [
                    "llama-3.3-70b-versatile",
                    "llama3-70b-8192",
                    "mixtral-8x7b-32768",
                    "gemma2-9b-it"
                ]
                
                for model in recomendados:
                    st.code(f"`{model}`", help="Excelente para horóscopos!")
            
            with col2:
                st.subheader("📊 Todos os Modelos")
                for model in response.data[:10]:  # Primeiros 10
                    st.caption(f"• {model.id}")
            
        except Exception as e:
            st.error(f"❌ Erro listando modelos: {str(e)}")

st.markdown("---")

# Teste de geração
st.markdown("## 🤖 Teste de Geração")

modelo = st.selectbox(
    "Escolha modelo:",
    ["llama-3.3-70b-versatile", "llama3-70b-8192", "mixtral-8x7b-32768"]
)

if st.button("🚀 Testar Horóscopo (Áries)", type="primary"):
    with st.spinner("Gerando com Groq... ⚡"):
        try:
            client = OpenAI(
                api_key=st.secrets["GROQ_API_KEY"],
                base_url="https://api.groq.com/openai/v1"
            )
            
            prompt = """Gere horóscopo para Áries hoje.

Estrutura:
- ❤️ Amor
- 💼 Trabalho
- 🧘 Bem-estar

Místico e acolhedor."""

            response = client.chat.completions.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=250,
                temperature=0.8
            )
            
            st.success("✅ **GROQ FUNCIONANDO PERFEITAMENTE!** ⚡")
            st.markdown("### 🎯 Horóscopo Gerado:")
            st.markdown(response.choices[0].message.content)
            
            st.caption(f"**Modelo**: {modelo}")
            st.caption(f"**Tokens**: {response.usage.total_tokens}")
            st.caption("**Custo**: $0.00 (GRATUITO!)")
            
        except Exception as e:
            st.error(f"❌ Erro: {str(e)}")
            
            if "401" in str(e):
                st.warning("🔑 **API Key inválida**")
                st.markdown("""
                **Solução:**
                1. console.groq.com/keys
                2. Create API Key
                3. Copiar gsk_...
                4. Streamlit Secrets → GROQ_API_KEY = "gsk_..."
                """)
            elif "429" in str(e):
                st.warning("⏱️ **Rate limit** - tente em 1 min")

st.markdown("---")

st.markdown("""
## ℹ️ **Como Configurar Groq**

1. **console.groq.com/keys** → Create API Key
2. **Copiar** `gsk_...`
3. **Streamlit Cloud → Settings → Secrets**:
