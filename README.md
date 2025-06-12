# 🚀 Ferramenta de Geração de Posts para Instagram

Este é um projeto que utiliza **LangChain**, **OpenAI** e **Streamlit** para criar carrosséis e descrições otimizadas para Instagram com base em conteúdo, público-alvo e tom de voz definidos pelo usuário.

## 🧠 Funcionalidades

- Geração de **carrossel para Instagram** com estrutura em **Markdown**.
- Criação de uma **descrição atrativa** para o post.
- Personalização dos textos com:
  - Conteúdo
  - Público-alvo
  - Tom de voz (Amigável, Profissional, Urgente, Divertida)
- Interface simples e interativa com **Streamlit**.

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- LangChain
- OpenAI API
- python-dotenv
- langchain-openai


# Configuração do projeto


### 1. Realize o clone do projeto

```bash
git clone "nome do repositório"
```

## 📦 Instalar às Bibliotecas do Python

```bash
pip install Streamlit
```

```bash
pip install LangChain
```

```bash
pip install python-dotenv
```

```bash
pip install openai
```

## 🔑 Como obter sua OpenAI API Key
Para utilizar a API da OpenAI neste projeto, você precisa gerar sua própria chave de acesso (API_KEY). Siga os passos abaixo:

Acesse o site https://openai.com/ e crie uma conta (caso ainda não tenha);
Após o login, vá até a área de API Keys no painel da OpenAI;
Adicione um cartão de crédito válido à sua conta;
Escolha o modelo que deseja utilizar (ex: gpt-4o, gpt-4o-mini, etc.);
Adicione créditos à sua conta (a OpenAI cobra por uso);
Copie a chave gerada e insira no arquivo .env do projeto:


