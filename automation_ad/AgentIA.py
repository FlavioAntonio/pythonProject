
import PIL.Image
import genai

# Configuração da API
genai.configure(api_key="SUA_CHAVE_AQUI")
model = genai.GenerativeModel('gemini-1.5-flash')

def agente_validador(caminho_documento):
    img = PIL.Image.open(caminho_documento)
    
    # O "Cérebro" do Agente: O Prompt de Sistema
    prompt = """
    Você é um auditor de documentos rigoroso. 
    Analise esta imagem e verifique:
    1. Se todos os campos (Nome, Data, CPF) estão preenchidos.
    2. Se existe uma assinatura feita à mão no campo designado.
    
    Responda EXCLUSIVAMENTE no formato JSON abaixo:
    {
        "documento_valido": boolean,
        "campos_vazios": ["lista", "de", "campos"],
        "assinatura_detectada": boolean,
        "confianca": 0-100
    }
    """

    response = model.generate_content([prompt, img])
    return response.text

# Execução e Decisão
resultado = agente_validador("contrato_cliente.jpg")
print(resultado)

# Aqui seu Python toma a decisão baseada no JSON
if '"documento_valido": true' in resultado:
    print("✅ Documento processado com sucesso!")
else:
    print("❌ Documento rejeitado. Verifique os campos.")