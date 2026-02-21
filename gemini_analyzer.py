import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv(override=True)

class GeminiAnalyzer:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or "your_api_key" in api_key:
            raise ValueError("GEMINI_API_KEY não encontrada ou inválida no arquivo .env.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def analyze_feedback(self, text):
        prompt = f"""
        Você é um especialista em análise de sentimentos e feedback de clientes.
        Analise o seguinte feedback e retorne um objeto JSON com:
        1. "sentimento": "Positivo", "Neutro" ou "Negativo".
        2. "categoria": Uma destas categorias: "Entrega", "Preço", "Qualidade", "Atendimento", "Site/UX", "Produto" ou "Outros".
        3. "resumo": Um breve resumo do ponto principal em uma frase.

        Feedback: "{text}"

        Retorne APENAS o JSON, sem markdown ou explicações.
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Clean response text in case Gemini adds extra chars
            clean_text = response.text.strip().replace("```json", "").replace("```", "")
            return json.loads(clean_text)
        except Exception as e:
            print(f"Error analyzing feedback: {e}")
            return {
                "sentimento": "Erro",
                "categoria": "Erro",
                "resumo": "Falha na análise da IA"
            }

if __name__ == "__main__":
    # Test call (requires valid API KEY)
    try:
        analyzer = GeminiAnalyzer()
        test_text = "O produto chegou rápido mas o preço é salgado."
        result = analyzer.analyze_feedback(test_text)
        print(f"Test result: {result}")
    except Exception as e:
        print(e)
