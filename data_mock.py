import pandas as pd
import random

def generate_mock_data(filename="customer_feedback.csv", num_entries=100):
    feedbacks = [
        "O produto chegou com 2 dias de atraso, mas a qualidade é excelente.",
        "Achei o preço muito alto para o que o produto oferece.",
        "Entrega super rápida! Chegou antes do esperado.",
        "O suporte ao cliente foi muito atencioso e resolveu meu problema.",
        "Infelizmente o produto quebrou na primeira semana de uso.",
        "Ótima relação custo-benefício, recomendo!",
        "A embalagem veio amassada, mas o produto está ok.",
        "Não gostei do material, parece muito frágil.",
        "O site é fácil de navegar e o checkout foi rápido.",
        "Demorou uma eternidade para chegar, nunca mais compro.",
        "Preço justo e entrega no prazo.",
        "O manual de instruções é confuso.",
        "Design bonito e acabamento premium.",
        "O atendimento via chat demorou muito para responder.",
        "O produto é menor do que eu esperava pelas fotos.",
        "Estou muito satisfeito com a compra, superou minhas expectativas.",
        "O frete foi mais caro que o produto em si.",
        "Funcionou perfeitamente para o meu caso de uso.",
        "Tive problemas com o pagamento, demorou para confirmar.",
        "A cor é diferente da que vi no site."
    ]
    
    data = []
    for i in range(num_entries):
        data.append({
            "id": i + 1,
            "date": pd.Timestamp.now() - pd.Timedelta(days=random.randint(0, 30)),
            "feedback": random.choice(feedbacks),
            "customer_name": f"Cliente {i+1}"
        })
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Generated {num_entries} mock feedback entries in {filename}")

if __name__ == "__main__":
    generate_mock_data()
