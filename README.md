# 🚀 Apotheosis Update Tracker

Este é um pequeno projeto prático desenvolvido com o objetivo de estudar e colocar em prática a integração e o consumo de APIs RESTful usando Python.

O script foi desenhado com um escopo bem específico: ele monitora exclusivamente as atualizações do mod **Apotheosis** na plataforma Modrinth e envia um alerta automatizado para o Discord. O objetivo principal foi eliminar qualquer necessidade de checagem ou aviso manual, automatizando o processo de ponta a ponta.

## 🧪 Prototipagem com Insomnia

Antes de escrever a primeira linha de código em Python, toda a comunicação do projeto foi mapeada, prototipada e testada utilizando o **Insomnia**.

Essa etapa de planejamento garantiu:

* **Validação do Endpoint de Leitura:** teste da rota `GET` da API do Modrinth para entender a estrutura do JSON recebido e identificar as chaves exatas de versão.
* **Validação do Endpoint de Escrita:** teste da rota `POST` do Webhook do Discord, ajustando o *payload* (corpo da mensagem) em JSON para garantir que o alerta chegaria com a formatação correta.
* **Isolamento de Erros:** garantia de que as APIs estavam respondendo corretamente antes da implementação da lógica em Python.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Insomnia** — para testes de rotas, payloads e prototipagem da integração.
* **Requests** — para consumo da REST API e envio de requisições HTTP (GET e POST).
* **Python-dotenv** — para gerenciamento seguro de credenciais e variáveis de ambiente (ocultando a URL do Webhook).

## ⚙️ Como executar o projeto localmente

**1. Clone este repositório:**

```bash
git clone https://github.com/Iago1610/Apotheosis Update Tracker.git
```

**2. Instale as dependências listadas no projeto:**

```bash
pip install -r requirements.txt
```

**3. Crie um arquivo `.env` na raiz do projeto** (use o `.env.example` como base) e insira a URL do seu Webhook do Discord:

```
DISCORD_WEBHOOK_URL=sua_url_do_webhook_aqui
```

**4. Execute o script:**

```bash
python main.py
```

> **Nota:** o script cria automaticamente um arquivo local `estado_versao.txt` para salvar a última versão encontrada e evitar o envio de mensagens repetidas no Discord caso não haja atualizações.