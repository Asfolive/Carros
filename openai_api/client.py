import openai

def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    '''.format(brand, model, year)

    openai.api_key = 'CHAVE_API'  # Substitua pela sua chave de API

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
