# Extração de Dados do Google Ads com Python

Este projeto permite a extração de dados do Google Ads utilizando Python. Você poderá obter informações detalhadas sobre suas campanhas, como custos, cliques, impressões, conversões e muito mais.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Passo a Passo](#passo-a-passo)
  - [1. Criar uma Pasta e Navegar até Ela](#1-criar-uma-pasta-e-navegar-até-ela)
  - [2. Clonar o Projeto](#2-clonar-o-projeto)
  - [3. Criar um Ambiente Virtual](#3-criar-um-ambiente-virtual)
  - [4. Ativar o Ambiente Virtual](#4-ativar-o-ambiente-virtual)
  - [5. Instalar as Bibliotecas Necessárias](#5-instalar-as-bibliotecas-necessárias)
  - [6. Configurar as Credenciais do Google Ads API](#6-configurar-as-credenciais-do-google-ads-api)
    - [6.1. Obter o Developer Token](#61-obter-o-developer-token)
    - [6.2. Obter o Client ID e Client Secret](#62-obter-o-client-id-e-client-secret)
    - [6.3. Gerar o Refresh Token](#63-gerar-o-refresh-token)
  - [7. Configurar o Arquivo `google-ads.yaml`](#7-configurar-o-arquivo-google-adsyaml)
  - [8. Executar os Scripts](#8-executar-os-scripts)
    - [8.1. Executar `atualiza_token.py`](#81-executar-atualiza_tokenpy)
    - [8.2. Executar `api_google_ads_v5.py`](#82-executar-api_google_ads_v5py)
- [Conclusão](#conclusão)

## Pré-requisitos

- **Python 3.7+** instalado no seu sistema.
- Conta no **Google Ads** com acesso à API.
- Conhecimentos básicos em Python e no uso de terminal/linha de comando.

## Passo a Passo

### 1. Criar uma Pasta e Navegar até Ela

Abra o terminal (CMD, PowerShell ou Terminal no macOS/Linux) e execute:

```bash
# Crie uma pasta para o projeto
mkdir google-ads-api

# Navegue até a pasta criada
cd google-ads-api
```

### 2. Clonar o Projeto

Clone o repositório do projeto:

```bash
git clone https://github.com/PabloFPereira/api_google_ads.git
```

Este repositório contém todos os arquivos necessários. Não é preciso gerar nenhum arquivo adicional; apenas edite com suas informações pessoais conforme os próximos passos.

### 3. Criar um Ambiente Virtual

É recomendável usar um ambiente virtual para gerenciar as dependências do projeto.

```bash
# Crie o ambiente virtual
python -m venv env
```

### 4. Ativar o Ambiente Virtual

Ative o ambiente virtual recém-criado.

```bash
# No Windows (CMD):
env\Scripts\activate.bat

# No Windows (PowerShell):
.\env\Scripts\Activate.ps1

# No macOS/Linux:
source env/bin/activate
```

### 5. Instalar as Bibliotecas Necessárias

Com o ambiente virtual ativado, instale as bibliotecas:

```bash
pip install google-ads==21.1.0 google-auth-oauthlib
```

### 6. Configurar as Credenciais do Google Ads API

Para acessar a API do Google Ads, você precisa de algumas credenciais:

- **Developer Token**
- **Client ID e Client Secret**
- **Refresh Token**

#### 6.1. Obter o Developer Token

1. Acesse sua conta do [Google Ads](https://ads.google.com/).
2. No canto superior direito, clique no ícone de **Ferramentas e Configurações** (chave inglesa).
3. Em **Configuração**, clique em **Centro de API**.
4. Copie o **Developer Token**. Se você não tiver um, siga as instruções para solicitar um.

#### 6.2. Obter o Client ID e Client Secret

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. Crie um novo projeto ou selecione um existente.
3. No menu lateral, vá em **APIs e Serviços** > **Tela de Permissões OAuth**.
   - Configure a tela de permissões se ainda não o fez.
4. Ainda em **APIs e Serviços**, vá em **Credenciais**.
5. Clique em **Criar Credenciais** > **ID do Cliente OAuth**.
6. Selecione **Aplicativo da Web**.
7. Em **URIs de redirecionamento autorizados**, adicione:

   ```
   http://localhost
   ```

8. Clique em **Criar**.
9. Copie o **Client ID** e o **Client Secret** gerados.

#### 6.3. Gerar o Refresh Token

Edite um arquivo chamado `credentials.json` na mesma pasta com o seguinte conteúdo:

```json
{
  "installed": {
    "client_id": "SEU_CLIENT_ID",
    "project_id": "SEU_PROJETO",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "SEU_CLIENT_SECRET",
    "redirect_uris": ["http://localhost"]
  }
}
```

Substitua:

- `SEU_CLIENT_ID` pelo Client ID obtido.
- `SEU_CLIENT_SECRET` pelo Client Secret obtido.
- `SEU_PROJETO` pelo ID do seu projeto no Google Cloud Console.


### 7. Configurar o Arquivo `google-ads.yaml`

Edite o arquivo `google-ads.yaml` presente no repositório com o seguinte conteúdo:

```yaml
developer_token: "SEU_DEVELOPER_TOKEN"
client_id: "SEU_CLIENT_ID"
client_secret: "SEU_CLIENT_SECRET"
refresh_token: "SEU_REFRESH_TOKEN"
login_customer_id: "SEU_LOGIN_CUSTOMER_ID"
```

Substitua:

- `SEU_DEVELOPER_TOKEN` pelo Developer Token obtido.
- `SEU_CLIENT_ID` e `SEU_CLIENT_SECRET` pelos valores anteriores.
- `SEU_REFRESH_TOKEN` pelo Refresh Token gerado.
- `SEU_LOGIN_CUSTOMER_ID` pelo ID da sua conta de gerenciamento (sem hífens ou espaços).

**Observação:** O `login_customer_id` é o ID da sua conta de gerente (MCC). Se você não usa uma conta de gerente, pode deixar esse campo em branco ou removê-lo.

### 8. Executar os Scripts

#### 8.1. Executar `atualiza_token.py`

Caso precise atualizar o Refresh Token no futuro, execute:

```bash
python atualiza_token.py
```

- O navegador será aberto para que você faça login com a conta do Google Ads.
- Autorize o acesso.
- O terminal exibirá `Refresh token: SEU_REFRESH_TOKEN`.

**Anote o Refresh Token gerado e atualize o `google-ads.yaml` novamente.**

#### 8.2. Executar `api_google_ads_v5.py`

Este script extrai os dados desejados.

**Certifique-se de que os IDs e datas estão atualizados no script:**

- Abra o arquivo `api_google_ads_v5.py` e edite as seguintes linhas:

  ```python
  client.login_customer_id = "SEU_LOGIN_CUSTOMER_ID"  # Substitua pelo seu login_customer_id
  customer_id = "SEU_CUSTOMER_ID"  # Substitua pelo seu customer_id (ID da conta de anúncio)
  ```

- Defina as datas `start_date` e `end_date` no formato `AAAA-MM-DD`.

  ```python
  start_date = "YYYY-MM-DD"  # Data de início
  end_date = "YYYY-MM-DD"    # Data de término
  ```

**Execute o script:**

```bash
python api_google_ads_v5.py
```

Se tudo estiver configurado corretamente, o script irá gerar um arquivo `google_ads_data.json` com os dados extraídos.

## Conclusão

Seguindo estes passos, você configurou com sucesso o ambiente para extrair dados do Google Ads usando Python. Certifique-se de manter suas credenciais seguras e de não compartilhá-las publicamente.

---

**Nota:** Este guia foi elaborado para facilitar a configuração e execução do projeto. Se você encontrar algum problema ou tiver dúvidas, sinta-se à vontade para abrir uma [issue](https://github.com/PabloFPereira/api_google_ads/issues) no repositório.
