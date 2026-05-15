# 🤖 QA-Brazil_Python_Automation

Projeto de automação de testes desenvolvido durante o **Bootcamp de Analista de QA da TripleTen**, simulando cenários reais de garantia de qualidade em aplicações web.

---

## 🎯 Objetivo do Projeto

Automatizar fluxos de teste em uma aplicação web utilizando Selenium WebDriver com Python, aplicando boas práticas de organização de código, nomenclatura padronizada e estrutura modular. O projeto simula um ambiente real de QA com foco na automação de cenários de ponta a ponta (end-to-end).

---

## ✅ Resultado

- Desenvolvimento de scripts de automação de testes funcionais para aplicação web
- Implementação de estrutura modular com separação de responsabilidades (pages, helpers, data, main)
- Cobertura de fluxos críticos da aplicação com casos de teste automatizados
- Código organizado seguindo convenções de nomenclatura e boas práticas de desenvolvimento

---

## 🛠️ Ferramentas Utilizadas

| Ferramenta | Finalidade |
|---|---|
| Python | Linguagem principal de desenvolvimento |
| Selenium WebDriver | Automação de interações com o navegador |
| PyCharm | IDE de desenvolvimento |
| Git / GitHub | Controle de versão |
| pytest | Execução e organização dos testes |

---

## 📁 Estrutura do Projeto

```
QA-Brazil_Python_Automation/
│
├── main.py          # Arquivo principal com os casos de teste
├── pages.py         # Page Objects — mapeamento dos elementos da interface
├── helpers.py       # Funções auxiliares reutilizáveis
├── data.py          # Dados de teste (constantes e variáveis)
├── requirements.txt # Dependências do projeto
└── .gitignore
```

---

## 📐 Diretrizes de Código

- **Variáveis** escritas em `snake_case` com nomes descritivos
- **Constantes** escritas em `MAIÚSCULAS`
- **Comentários** para explicar blocos importantes de código
- **Organização modular** com blocos reutilizáveis importados onde necessário
- **Nomenclatura de testes** iniciando com `test_` seguido de descrição clara do cenário
- Sem funções de espera (`wait`) desnecessárias para otimizar a execução

---

## 📚 O Que Aprendi

- ✔️ Estruturação de projetos de automação com o padrão **Page Object Model (POM)**
- ✔️ Escrita de scripts de automação com **Selenium WebDriver e Python**
- ✔️ Organização modular de código para **reaproveitamento e manutenibilidade**
- ✔️ Boas práticas de **nomenclatura e documentação** em projetos de QA
- ✔️ Uso de **Git e GitHub** para controle de versão em projetos de teste
- ✔️ Identificação e cobertura de **fluxos críticos** em aplicações web

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/soaresjacqueline-rhaenys/QA-Brazil_Python_Automation.git

# Acesse a pasta do projeto
cd QA-Brazil_Python_Automation

# Instale as dependências
pip install -r requirements.txt

# Execute os testes
pytest main.py
```

---

## 👩‍💻 Autora

**Jacqueline Soares** — Analista de QA Jr. em formação

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jacquelinemsoares/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/soaresjacqueline-rhaenys)
