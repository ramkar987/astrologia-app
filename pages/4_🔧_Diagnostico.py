"""
Página de Diagnóstico das APIs
"""
import streamlit as st

st.set_page_config(page_title="Diagnóstico", page_icon="🔧", layout="wide")

st.title("🔧 Diagnóstico de APIs")
st.markdown("### Teste as conexões com Gemini e OpenAI")

# Verificar quais secrets estão configurados
st.markdown("---")
st.markdown("## 📋 Secrets Configurados")

secrets_status = {
    "GEMINI_API_KEY": "GEMINI_API_KEY" in st.secrets,
    "OPENAI_API_KEY": "OPENAI_API_KEY" in st.secrets
}

col1, col2 = st.columns(2)

with col1:
    if secrets_status["GEMINI_API_KEY"]:
        st.success("✅ GEMINI_API_KEY configurado")
        st.caption(f"Primeiros caracteres: {st.secrets['GEMINI_API_KEY'][:10]}...")
    else:
        st.error("❌ GEMINI_API_KEY não encontrado")

with col2:
    if secrets_status["OPENAI_API_KEY"]:
        st.success("✅ OPENAI_API_KEY configurado")
        st.caption(f"Primeiros caracteres: {st.secrets['OPENAI_API_KEY'][:10]}...")
    else:
        st.error("❌ OPENAI_API_KEY não encontrado")

st.markdown("---")

# Testar Gemini
st.markdown("## 🤖 Teste do Gemini")

if st.button("🧪 Testar Gemini API", type="primary"):
    if not secrets_status["GEMINI_API_KEY"]:
        st.error("Configure GEMINI_API_KEY nos Secrets primeiro!")
    else:
        with st.spinner("Testando Gemini..."):
            try:
                import google.generativeai as genai
                
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                
                # Listar modelos disponíveis
                st.info("📋 Listando modelos disponíveis...")
                modelos_disponiveis = []
                
                for model in genai.list_models():
                    if 'generateContent' in model.supported_generation_methods:
                        modelos_disponiveis.append(model.name)
                        st.write(f"✅ {model.name}")
                
                if modelos_disponiveis:
                    st.success(f"Encontrados {len(modelos_disponiveis)} modelos!")
                    
                    # Testar geração com o primeiro modelo
                    modelo_teste = modelos_disponiveis[0]
                    st.info(f"🧪 Testando geração com: {modelo_teste}")
                    
                    model = genai.GenerativeModel(modelo_teste)
                    response = model.generate_content("Diga apenas 'Olá, teste bem-sucedido!' em português.")
                    
                    st.success("✅ GEMINI FUNCIONANDO!")
                    st.markdown("**Resposta:**")
                    st.info(response.text)
                else:
                    st.warning("Nenhum modelo com generateContent encontrado")
                    
            except Exception as e:
                st.error(f"❌ Erro no Gemini: {str(e)}")
                st.caption("Detalhes do erro:")
                st.code(str(e))

st.markdown("---")

# Testar OpenAI
st.markdown("## 🤖 Teste da OpenAI")

if st.button("🧪 Testar OpenAI API", type="primary"):
    if not secrets_status["OPENAI_API_KEY"]:
        st.error("Configure OPENAI_API_KEY nos Secrets primeiro!")
    else:
        with st.spinner("Testando OpenAI..."):
            try:
                from openai import OpenAI
                
                client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                
                st.info("🧪 Gerando texto de teste com gpt-3.5-turbo...")
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Você é um assistente útil."},
                        {"role": "user", "content": "Diga apenas 'Olá, teste bem-sucedido!' em português."}
                    ],
                    max_tokens=50,
                    temperature=0.7
                )
                
                st.success("✅ OPENAI FUNCIONANDO!")
                st.markdown("**Resposta:**")
                st.info(response.choices[0].message.content)
                
                # Mostrar uso
                st.markdown("**Uso de tokens:**")
                st.caption(f"Total: {response.usage.total_tokens} tokens")
                st.caption(f"Custo estimado: ~${response.usage.total_tokens * 0.0000015:.6f} USD")
                
            except Exception as e:
                erro_str = str(e)
                st.error(f"❌ Erro na OpenAI: {erro_str}")
                
                # Diagnóstico específico
                if "429" in erro_str or "quota" in erro_str.lower():
                    st.warning("⚠️ **Erro de Quota Excedida**")
                    st.markdown("""
                    **Soluções:**
                    1. Acesse: https://platform.openai.com/settings/organization/billing
                    2. Adicione um método de pagamento (cartão de crédito)
                    3. Adicione pelo menos $5 USD de crédito
                    4. Aguarde 5-10 minutos e tente novamente
                    """)
                elif "401" in erro_str or "Incorrect" in erro_str:
                    st.warning("⚠️ **API Key Incorreta**")
                    st.markdown("""
                    **Soluções:**
                    1. Verifique se a key está correta
                    2. Crie uma nova key em: https://platform.openai.com/api-keys
                    3. Atualize nos Secrets do Streamlit
                    """)
                else:
                    st.caption("Detalhes do erro:")
                    st.code(erro_str)

st.markdown("---")

# Informações
st.markdown("## ℹ️ Informações")

st.info("""
**Como usar esta página:**

1. Certifique-se de que as API keys estão configuradas nos Secrets
2. Clique em "Testar Gemini API" ou "Testar OpenAI API"
3. Veja os resultados e diagnósticos
4. Siga as instruções caso haja erros

**Nota**: Esta página só deve ser visível para administradores em produção.
""")

# Botão para esconder página (opcional)
if st.button("🗑️ Remover esta página do menu"):
    st.warning("Para remover esta página, delete o arquivo `pages/4_🔧_Diagnostico.py` do GitHub")
