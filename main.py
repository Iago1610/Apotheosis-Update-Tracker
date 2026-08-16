import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações
MOD_NOME = "apotheosis"
API_URL = f"https://api.modrinth.com/v2/project/{MOD_NOME}/version"
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
ARQUIVO_ESTADO = "estado_versao.txt"


def obter_ultima_versao_salva():
    """Lê o arquivo local para saber qual foi a última versão alertada."""
    if os.path.exists(ARQUIVO_ESTADO):
        with open(ARQUIVO_ESTADO, "r") as arquivo:
            return arquivo.read().strip()
    return None


def salvar_nova_versao(versao):
    """Salva a nova versão no arquivo local."""
    with open(ARQUIVO_ESTADO, "w") as arquivo:
        arquivo.write(versao)


def verificar_atualizacoes():
    print(f"Buscando atualizações para o mod {MOD_NOME}...")

    try:
        resposta_api = requests.get(API_URL)
        resposta_api.raise_for_status()  # Lança um erro se a API estiver fora do ar
        dados = resposta_api.json()

        # Pega a versão mais recente do JSON
        versao_recente = dados[0]['version_number']
        tipo_versao = dados[0]['version_type']

        versao_salva = obter_ultima_versao_salva()

        if versao_recente != versao_salva:
            print(f"Nova versão encontrada: {versao_recente}! Enviando alerta...")
            enviar_alerta_discord(versao_recente, tipo_versao)
            salvar_nova_versao(versao_recente)
        else:
            print(f"O mod já está na versão mais recente ({versao_recente}). Nenhum alerta enviado.")

    except Exception as e:
        print(f"Erro ao verificar atualizações: {e}")


def enviar_alerta_discord(versao, tipo):
    mensagem = {
        "content": f"⚔️ **Atualização Detectada!**\nO mod **{MOD_NOME.capitalize()}** acabou de receber uma atualização.\n\n📦 Nova versão: `{versao}` ({tipo})"
    }

    resposta = requests.post(WEBHOOK_URL, json=mensagem)

    if resposta.status_code == 204:
        print("Sucesso! Alerta enviado no Discord..")
    else:
        print(f"Falha ao enviar o alerta para o Discord. Status: {resposta.status_code}")


if __name__ == "__main__":
    if not WEBHOOK_URL:
        print("Erro: DISCORD_WEBHOOK_URL não encontrada. Verifique seu arquivo .env.")
    else:
        verificar_atualizacoes()