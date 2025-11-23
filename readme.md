# Stokki - Gestão de Estoque Inteligente

![Stokki](https://github.com/Gylerme0/stokki-app/blob/main/static/img/dashboard-stokki.png)

A simplicidade que o operador precisa com a inteligência que o gestor exige.

# 📦 Sobre o Projeto

O Stokki é uma aplicação web (SaaS Desktop-First) desenvolvida para preencher uma lacuna crítica no mercado de logística para PMEs.

Atualmente, gestores de estoque enfrentam um dilema: usar planilhas inseguras ou contratar ERPs complexos e caros ("faz-tudo") que dificultam a vida do operador logístico com menus irrelevantes.

O Stokki resolve isso sendo um WMS (Warehouse Management System) Hiper-Especializado. Focamos 100% na eficiência do chão de armazém, oferecendo funcionalidades avançadas de logística com uma interface limpa, intuitiva e livre de ruídos.

# 🎯 Objetivo

Fornecer uma ferramenta que garanta acuracidade de estoque e agilidade na separação de pedidos, reduzindo a curva de aprendizado do operador para minutos, não semanas.

# 🚀 Funcionalidades (MVP v1.0)

O Stokki foca no essencial para fazer o almoxarifado funcionar sem burocracia:

# 📊 Dashboard de Controle

KPIs em Tempo Real: Valor total do inventário, itens em alerta e itens esgotados.

Ações Rápidas: Atalhos diretos para entrada, saída e transferência (menos cliques).

Monitor de Ordens: Visualização clara do status de separação de pedidos.

# 🏭 Operações de Estoque (Core)

Recebimento: Entrada de mercadorias vinculada a fornecedores e endereçamento.

Movimentação Interna: Transferência fácil entre endereços (ex: do Pulmão para o Picking).

Ajuste de Inventário: Ferramenta para correção rápida de divergências físicas.

# 🛒 Gestão de Picking (Diferencial WMS)

Criação de Ordens: Agrupamento de pedidos para separação.

Lista de Separação: Geração de listas otimizadas para o operador saber exatamente onde ir.

# 📈 Inteligência & Relatórios

Curva ABC: Classificação automática de produtos por relevância (A, B, C).

Rastreabilidade: Log completo de auditoria (Quem, Quando, Onde e O Quê).

Posição de Estoque: Relatório detalhado de saldo por endereço físico.

# 🎨 Design System

O projeto segue rigorosamente um guia de estilos baseado no Google Material Design, priorizando a legibilidade e a hierarquia visual para evitar erros operacionais.

# 🗺️ Roadmap do Produto

O desenvolvimento é dividido em fases estratégicas:

[x] Fase 1: MVP (Atual) - CRUD: Cadastros, Movimentações, Picking

[ ] Fase 2: Stokki Inteligente - Alertas automatizados e sugestões de compras via IA.

[ ] Fase 3: Controle Rígido - Implementação de Lote e Validade (FIFO/FEFO).

[ ] Fase 4: Conectividade - API para integração com E-commerce e ERPs Financeiros.

# 🛠️ Tecnologias

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

Frontend: HTML, CSS, JavaScript

Backend: Python, FastAPI

Banco de Dados: SQLite

Prototipagem: Figma

# 🚀 Como Rodar o Projeto

Pré-requisitos

Python 3.10+ 

# Instalação

Clone o repositório:

git clone [https://github.com/Gylerme0/stokki-app.git](https://github.com/Gylerme0/stokki-app.git)


# Instale as dependências:

cd stokki
pip install -r requirements.txt

Configure as variáveis de ambiente:

cp .env.example .env
Edite o arquivo .env com suas credenciais

Inicie o servidor de desenvolvimento:

uvicorn main:app --reload

# 🐳 Como Rodar com Docker

Certifique-se de ter o Docker e o Docker Compose instalados.

1. Construa e inicie os containers:
```bash
docker-compose up --build
```

2. Acesse a aplicação em: [http://localhost:8000](http://localhost:8000)

Para parar a execução:
```bash
docker-compose down
```


# 🤝 Contribuição

Este projeto é parte de um trabalho acadêmico de [Nome da Disciplina] da [Nome da Faculdade].

Membros da equipe:

Guilherme Oliveira

Leonardo Andrade

Eric Carneiro

Vinicius Pires

Desenvolvido com 💙 pela equipe Stokki.
