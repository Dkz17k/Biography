# Biography

Auto Biografia em Django

---

## 📝 Descrição

Este projeto é uma biografia simples construída com Django.  
Ele possui uma página inicial com informações pessoais e uma página de contato com um formulário.

---

## 🎨 O que foi feito com Inteligência Artificial

- O **front-end HTML/CSS** (layout, estilo, componentes visuais, cartões, gradientes, botões, etc) foi gerado com auxílio de Inteligência Artificial.

---

## 🔧 O que foi feito manualmente

- As **views** do Django (`index`, `contato`) para renderizar os templates.  
- A configuração das **URLs** (`path('', index, ...)`, `path('contato/', contato, ...)`).  
- A integração entre templates, views e rotas.  
- A adaptação do front-end para funcionar dentro do Django.

---

## 🛠 Tecnologias usadas

- Python  
- Django  
- HTML  

---

## 🚀 Como rodar o projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/Dkz17k/Biography.git
Acesse a pasta do projeto:

bash
cd Biography
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
Instale as dependências:

bash
pip install -r requirements.txt
Aplique as migrações:

bash
python manage.py migrate
Inicie o servidor:

bash
python manage.py runserver
Acesse no navegador:

Página inicial: http://127.0.0.1:8000/

Contato: http://127.0.0.1:8000/contato/

