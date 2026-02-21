# 📊 Customer Feedback Sentiment Analyzer (Gemini 2.0)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Gemini%202.0-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Um analisador inteligente de feedbacks que vai além do "bom ou ruim". Utilizando o poder do **Gemini 2.0 Flash**, o sistema extrai automaticamente categorias de reclamação (Entrega, Preço, Qualidade, etc.) e gera um dashboard executivo interativo.

---

## 🌟 Diferenciais

- **Classificação Multidimensonal**: Identifica a área específica da empresa que precisa de atenção.
- **Resumo Automático**: Gera uma síntese de uma frase para cada feedback.
- **Dashboard Premium**: Visualização em tempo real com KPIs e gráficos dinâmicos.
- **Segurança**: Gestão de credenciais via variáveis de ambiente (.env).


## 🚀 Como Rodar o Projeto

### 1. Pré-requisitos
- Python 3.9 ou superior
- Uma chave de API do [Google AI Studio](https://aistudio.google.com/)

### 2. Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/emocoes-ai.git

# Entre na pasta
cd emocoes-ai

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configuração
Crie um arquivo `.env` na raiz do projeto com sua chave:
```env
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

### 4. Execução
```bash
# Opcional: Gerar dados de teste
python data_mock.py

# Iniciar o dashboard
streamlit run app.py
```

## 🛠️ Stack Tecnológica

- **Linguagem**: [Python](https://www.python.org/)
- **Processamento de Dados**: [Pandas](https://pandas.pydata.org/)
- **Interface**: [Streamlit](https://streamlit.io/)
- **Visualização**: [Plotly Express](https://plotly.com/python/plotly-express/)
- **IA**: [Google Gemini 2.0 Flash](https://ai.google.dev/)

---

Desenvolvido com ❤️ por **Demorojao**
