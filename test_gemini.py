"""
Teste para validar se a API key do Gemini está funcionando
"""
import google.generativeai as genai

# Substitua pela sua nova key
API_KEY = "cole_sua_nova_key_aqui"

print("🔍 Testando API do Gemini...")
print("-" * 50)

try:
    # Configurar API
    genai.configure(api_key=API_KEY)
    print("✅ API configurada com sucesso")
    
    # Listar modelos disponíveis
    print("\n📋 Modelos disponíveis:")
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"  - {model.name}")
    
    # Testar geração de conteúdo
    print("\n🤖 Testando geração de conteúdo...")
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content("Diga 'Olá, mundo!' em português")
    print(f"✅ Resposta: {response.text}")
    
    print("\n🎉 SUCESSO! A API está funcionando perfeitamente!")
    print("Você pode usar 'gemini-pro' no seu app.")
    
except Exception as e:
    print(f"\n❌ ERRO: {str(e)}")
    print("\n🔧 Possíveis soluções:")
    print("1. Verifique se a API key está correta")
    print("2. Acesse https://aistudio.google.com/app/apikey")
    print("3. Certifique-se de que a API está habilitada")
    print("4. Tente criar uma nova key")
