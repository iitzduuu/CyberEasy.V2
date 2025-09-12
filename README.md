# CyberEasy.V2
---

### **Como Começar**

Siga as instruções abaixo para obter uma cópia local do projeto e começar a desenvolver.

#### **1. Clonar o Repositório**

Escolha uma das opções abaixo para clonar o projeto para a sua máquina local.

* **HTTPS (Recomendado):**
    ```bash
    git clone [https://github.com/iitzduuu/CyberEasy.V2.git](https://github.com/iitzduuu/CyberEasy.V2.git)
    ```
* **SSH:**
    ```bash
    git clone git@github.com:iitzduuu/CyberEasy.V2.git
    ```

Após clonar, entre na pasta do projeto:
```bash
cd CyberEasy.V2
```
---

### **Nosso Fluxo de Trabalho com Git**

Este projeto utiliza um modelo de branches para organizar o desenvolvimento. Entender o propósito e o uso de cada branch é fundamental para contribuir.

#### **Como Usar Cada Branch**

- **`main`**
  - **Propósito:** Versão de produção. Contém apenas o código estável e testado.
  - **Como usar:** Você **NÃO** deve trabalhar diretamente nesta branch. Ela é atualizada apenas ao final do ciclo de desenvolvimento, quando a branch `integration` é mesclada nela através de um Pull Request.

- **`backend`**
  - **Propósito:** Desenvolver a lógica central do scanner.
  - **Como usar:**
    1.  Mude para esta branch para criar ou editar a lógica de negócio:
        ```bash
        git checkout backend
        ```
    2.  Todo o código Python da lógica principal deve ser criado dentro da pasta `src/yara_scanner/`.
    3.  Novas regras YARA (`.yar`) devem ser adicionadas à pasta `rules/`.
    4.  Após implementar uma funcionalidade, envie suas alterações:
        ```bash
        git push origin backend
        ```

- **`frontend`**
  - **Propósito:** Desenvolver a interface do usuário (UI).
  - **Como usar:**
    1.  Mude para esta branch para criar ou editar a interface web:
        ```bash
        git checkout frontend
        ```
    2.  Todo o trabalho de UI deve ser feito no arquivo `app.py`, utilizando a biblioteca Streamlit.
    3.  Após implementar uma nova tela ou componente visual, envie suas alterações:
        ```bash
        git push origin frontend
        ```

- **`integration`**
  - **Propósito:** Unir e testar o `frontend` e o `backend` juntos.
  - **Como usar:**
    1.  Mude para esta branch quando quiser testar a integração das funcionalidades:
        ```bash
        git checkout integration
        git pull origin integration # Sempre atualize antes de mesclar
        ```
    2.  Traga as atualizações do `backend` e/ou `frontend`:
        ```bash
        git merge backend
        git merge frontend
        ```
    3.  Resolva quaisquer conflitos de mesclagem e execute o sistema para garantir que tudo funciona como esperado.
    4.  Envie a versão integrada para o repositório:
        ```bash
        git push origin integration
        ```

#### **Resumo do Fluxo de Contribuição**

1.  **Desenvolva** nas branches `frontend` ou `backend`.
2.  **Mescle** seu trabalho na branch `integration` para testes completos.
3.  **Abra um Pull Request (PR)** de `integration` para `main` para finalizar o processo.
