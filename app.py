import streamlit as st
import pandas as pd
import plotly.express as px
from data_processor import DataProcessor
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Feedback Analyzer AI", layout="wide")

st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 15px 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        background-color: rgba(255, 255, 255, 0.1);
    }
    [data-testid="stMetricValue"] {
        color: #00d4ff !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
        opacity: 0.8;
        font-size: 0.9rem !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Customer Feedback Sentiment Analyzer")
st.markdown("Analise milhares de avaliações em segundos usando a potência do **Gemini AI**.")

# Sidebar
st.sidebar.header("Configurações")

uploaded_file = st.sidebar.file_uploader("Upload de CSV de Feedback", type="csv")
use_mock = st.sidebar.checkbox("Usar dados de exemplo", value=True)

try:
    processor = DataProcessor()
    api_ready = True
except ValueError as e:
    st.error(f"⚠️ Erro de Configuração: {e}")
    st.info("Por favor, verifique se o arquivo .env contém sua GEMINI_API_KEY corretamente.")
    api_ready = False
except Exception as e:
    st.error(f"Erro inesperado: {e}")
    api_ready = False

# Main Logic
df = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif use_mock:
    if os.path.exists("customer_feedback.csv"):
        df = pd.read_csv("customer_feedback.csv")
    else:
        st.error("Arquivo de exemplo não encontrado. Execute 'python data_mock.py' primeiro.")

if df is not None:
    st.subheader("📋 Dados Carregados")
    st.dataframe(df.head(), use_container_width=True)
    
    if st.button("🚀 Iniciar Análise com IA", disabled=not api_ready):
        with st.spinner("O Gemini está analisando seus feedbacks..."):
            # Limit to 10 for demo purposes if it's too large
            if len(df) > 20:
                st.warning("Para demonstração, analisaremos apenas os primeiros 20 itens.")
                df_to_analyze = df.head(20).copy()
            else:
                df_to_analyze = df.copy()
                
            processed_df = processor.enrich_with_ai(df_to_analyze)
            
            st.success("Análise concluída!")
            
            # KPIs
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total de Feedbacks", len(processed_df))
            with col2:
                pos_count = len(processed_df[processed_df['Sentimento'] == 'Positivo'])
                st.metric("Sentimento Positivo", f"{(pos_count/len(processed_df)*100):.1f}%")
            with col3:
                neg_count = len(processed_df[processed_df['Sentimento'] == 'Negativo'])
                st.metric("Sentimento Negativo", f"{(neg_count/len(processed_df)*100):.1f}%")
            
            # Visualizations
            col_left, col_right = st.columns(2)
            
            with col_left:
                st.subheader("Categorias de Reclamações/Elogios")
                cat_counts = processed_df['Categoria'].value_counts().reset_index()
                cat_counts.columns = ['Categoria', 'Contagem']
                fig_bar = px.bar(cat_counts, x='Categoria', y='Contagem', 
                                 color='Categoria', title="Distribuição por Categoria",
                                 color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig_bar, use_container_width=True)
                
            with col_right:
                st.subheader("Visão Geral do Sentimento")
                sent_counts = processed_df['Sentimento'].value_counts().reset_index()
                sent_counts.columns = ['Sentimento', 'Contagem']
                fig_pie = px.pie(sent_counts, values='Contagem', names='Sentimento', 
                                 title="Sentimento Geral",
                                 color_discrete_map={'Positivo': '#00CC96', 'Negativo': '#EF553B', 'Neutro': '#636EFA'})
                st.plotly_chart(fig_pie, use_container_width=True)
            
            # Detailed Table
            st.subheader("🔍 Detalhes da Análise")
            st.dataframe(processed_df[['feedback', 'Sentimento', 'Categoria', 'Resumo']], use_container_width=True)
            
            # Export
            csv = processed_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar Relatório Completo", csv, "feedback_analisado.csv", "text/csv")
else:
    st.info("Aguardando carregamento de dados...")
