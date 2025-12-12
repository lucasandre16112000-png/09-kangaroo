# 🦘 Kangaroo - Ferramenta de Análise de Bitcoin Puzzle

Uma ferramenta baseada em Windows para analisar e resolver puzzles de Bitcoin, combinando um núcleo de alta performance em C/C++ com uma interface de dashboard em Python.

## ✨ Funcionalidades

- **Núcleo de Alta Performance**: Executável otimizado em C/C++ para máxima velocidade.
- **Dashboard em Python**: Interface de monitoramento amigável baseada em Plotly.
- **Rastreamento de Progresso**: Monitoramento de execução e estatísticas em tempo real.
- **Sistema de Checkpoint**: Salve e retome a execução.

## 🛠️ Tecnologias

- **C/C++**: Núcleo do solver (Kangaroo.exe).
- **Python 3.8+**: Dashboard e gerenciamento.
- **Plotly**: Visualização de dados.
- **Flask**: Servidor web.

## 📋 Guia de Instalação e Execução (Para Qualquer Pessoa)

### Pré-requisitos

1.  **Git**: [**Download aqui**](https://git-scm.com/downloads)
2.  **Python**: [**Download aqui**](https://www.python.org/downloads/) (versão 3.8+)

### Passo 1: Baixar o Projeto

```bash
git clone https://github.com/lucasandre16112000-png/09-kangaroo.git
cd 09-kangaroo
```

### Passo 2: Executar o Solver (Modo Fácil)

Dê um duplo clique no arquivo `INICIAR.bat` para iniciar com as configurações padrão.

### Passo 3: (Opcional) Executar o Dashboard

```bash
# Instale as dependências (apenas na primeira vez)
pip install -r requirements.txt

# Inicie o painel
python painel_kangaroo_FINAL.py
```

Acesse `http://localhost:5000` no seu navegador.

## 👨‍💻 Autor

Lucas André S - [GitHub](https://github.com/lucasandre16112000-png)
