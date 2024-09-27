import openai

def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    '''.format(brand, model, year)

    openai.api_key = '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'  # Substitua pela sua chave de API

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # ou 'gpt-4', se preferir
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=250  # Ajuste para o tamanho desejado
    )

    return response['choices'][0]['message']['content']

# Exemplo de uso
# bio = get_car_ai_bio("Fusca", "Volkswagen", 1976)
# print(bio)
