import pandas as pd
from gemini_analyzer import GeminiAnalyzer
import streamlit as st

class DataProcessor:
    def __init__(self):
        self.analyzer = GeminiAnalyzer()

    def process_csv(self, filename):
        df = pd.read_csv(filename)
        return df

    def enrich_with_ai(self, df):
        sentiments = []
        categories = []
        summaries = []
        
        progress_bar = st.progress(0)
        total = len(df)
        
        for i, feedback in enumerate(df['feedback']):
            analysis = self.analyzer.analyze_feedback(feedback)
            sentiments.append(analysis.get('sentimento', 'Neutro'))
            categories.append(analysis.get('categoria', 'Outros'))
            summaries.append(analysis.get('resumo', ''))
            progress_bar.progress((i + 1) / total)
            
        df['Sentimento'] = sentiments
        df['Categoria'] = categories
        df['Resumo'] = summaries
        
        return df
