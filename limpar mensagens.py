import re
import pandas as pd

# Função para extrair as mensagens e suas informações
def processar_whatsapp(txt_file):
    # Abrir o arquivo de conversa do WhatsApp
    with open(txt_file, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    # Listas para armazenar os dados extraídos
    datas = []
    horas = []
    nomes = []
    mensagens = []

    # Expressão regular para capturar data, hora, nome e mensagem
    # Exemplo de formato: "12/04/2023 14:23 - João: Olá, tudo bem?"
    padrao = r'(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - (.*?): (.*)'

    for linha in linhas:
        # Usando regex para identificar se a linha contém data, hora, nome e mensagem
        match = re.match(padrao, linha)
        
        if match:
            data = match.group(1)
            hora = match.group(2)
            nome = match.group(3)
            mensagem = match.group(4)

            # Ignorar mensagens com "foto ocultada"
            if "foto ocultada" in mensagem.lower():
                continue

            # Adicionar as informações nas listas
            datas.append(data)
            horas.append(hora)
            nomes.append(nome)
            mensagens.append(mensagem)

    # Criar um DataFrame do pandas com as informações
    df = pd.DataFrame({
        'Data': datas,
        'Hora': horas,
        'Nome': nomes,
        'Mensagem': mensagens
    })

    return df

# Função principal para gerar o arquivo CSV
def exportar_para_csv(txt_file, csv_file):
    # Processar o arquivo de texto
    df = processar_whatsapp(txt_file)

    # Salvar o DataFrame como CSV
    df.to_csv(csv_file, index=False, encoding='utf-8')

# Caminho para o arquivo de texto exportado do WhatsApp
# txt_file = 'C: '

# Caminho para o arquivo CSV de saída
# csv_file = 'C: '

# Exportar o conteúdo para CSV
exportar_para_csv(txt_file, csv_file)

print(f'Arquivo CSV gerado com sucesso: {csv_file}')