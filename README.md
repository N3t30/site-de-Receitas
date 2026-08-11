# 🍳 Site de Receitas

Uma plataforma web completa para entusiastas da culinária compartilharem e descobrirem novas receitas, promovendo a interação e a troca de experiências na comunidade.

---

## 🎯 Objetivos do Projeto

* **Criar uma Comunidade Gastronômica:** Proporcionar um espaço intuitivo e acessível para entusiastas da culinária compartilharem suas criações e descobrirem novas receitas.
* **Garantir a Qualidade do Conteúdo:** Implementar um fluxo de aprovação via administrador, assegurando que apenas receitas completas, padronizadas e relevantes fiquem visíveis para o público geral.
* **Autonomia para os Autores:** Oferecer aos usuários cadastrados um painel (dashboard) dedicado para gerenciar todo o ciclo de vida de suas receitas (criação, edição e exclusão).
* **Confiabilidade e Qualidade de Código:** Desenvolver uma aplicação sólida e escalável, respaldada por testes unitários e testes automatizados de ponta a ponta (E2E com Selenium).

---

## 🚀 Recursos Principais

* **Cadastro e Login:** Os usuários podem se cadastrar no site fornecendo informações básicas e realizar login para acessar funcionalidades exclusivas.
* **Criação de Receitas:** Usuários logados têm a capacidade de criar e compartilhar suas próprias receitas, incluindo detalhes como ingredientes, instruções de preparo, tempo de cozimento, rendimento e foto de capa.
* **Publicação com Aprovação:** Após a criação da receita, o usuário solicita a aprovação do administrador para torná-la pública, garantindo a qualidade e relevância do conteúdo na comunidade.
* **Visualização e Busca:** Interface intuitiva para explorar receitas compartilhadas por outros membros, facilitando a busca por categorias, ingredientes ou termos específicos.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Desenvolvido em Python, utilizando o framework **Django** para a construção da lógica de negócio e rotas.
* **Frontend:** Utiliza HTML5, CSS3 e JavaScript para criar uma interface amigável, limpa e responsiva.
* **Testes:**
  * **Testes Unitários:** Implementados para garantir a funcionalidade correta de partes específicas do código de forma isolada.
  * **Testes Selenium:** Utilizados para automação de testes de integração e cenários E2E, garantindo que as diferentes partes do sistema funcionem bem juntas.
* **Banco de Dados:** SQLite (ambiente de desenvolvimento) / PostgreSQL.
* **Controle de Versão:** Git.

---

## 🧪 Suíte de Testes

Para executar os testes automatizados do projeto, utilize os comandos abaixo no terminal:

```bash
# Executar testes unitários do Django
python manage.py test

# Executar testes automatizados com Selenium
python manage.py test functional_tests