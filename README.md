# Sistema de Cadastro de Empresas e Vagas

Este projeto implementa um sistema de cadastro de empresas e vagas que permite o gerenciamento de empresas, estudantes e oportunidades de estágio. O sistema utiliza JSON para persistência de dados e fornece uma interface de console para navegação.

## Funcionalidades Principais

1. **Cadastro de Empresas**: Permite o registro de empresas com `empresaId` gerado automaticamente.
2. **Cadastro de Vagas**: Permite o cadastro de vagas vinculadas a empresas, com validação de `empresaId`.
3. **Navegação Intuitiva**: Sistema de menus e navegação em loop, permitindo operações contínuas ou encerramento do programa.
4. **Exibição de Registro Temporário**: Exibe um índice temporário ao listar empresas e vagas, facilitando a navegação.

---

## Alterações e Melhorias Implementadas

### 1. **Implementação do `empresaId` Automático**
   - **Motivo**: Para relacionar vagas a empresas específicas, o sistema requer um `empresaId` único para cada empresa.
   - **Alteração**: Criamos a função `obter_proximo_id_empresa()` para gerar automaticamente o próximo `empresaId` com base no maior ID existente em `empresas.json`, garantindo que cada `empresaId` seja único e incremental.
   - **Impacto**: Simplificou o cadastro, garantindo consistência e unicidade nos IDs de empresas.

### 2. **Adição do Campo `empresaId` ao Cadastro de Empresa**
   - **Motivo**: Inicialmente, o `empresas.json` não continha o campo `empresaId`, impossibilitando o sistema de vagas de validar o ID da empresa.
   - **Alteração**: Atualizamos o cadastro de empresas para incluir o `empresaId` gerado automaticamente.
   - **Impacto**: Agora, cada empresa possui um `empresaId` no `empresas.json`, permitindo que o sistema relacione empresas e vagas sem conflitos.

### 3. **Ajuste na Função `empresa_existe()`**
   - **Motivo**: A função `empresa_existe()` precisa confirmar se um `empresaId` fornecido ao cadastrar uma vaga existe no `empresas.json`.
   - **Alteração**: Modificamos a função para verificar o campo `empresaId` em cada entrada no `empresas.json`.
   - **Impacto**: Garantiu que apenas IDs válidos sejam usados no cadastro de vagas, evitando inconsistências.

### 4. **Melhoria na Função `VisualizarJson()`**
   - **Motivo**: O índice `Registro`, usado apenas para exibição, gerava confusão ao aparecer como se fosse um dado salvo no JSON.
   - **Alteração**: Mantivemos `Registro` como uma contagem temporária no console, destacando que ele é apenas para exibição.
   - **Impacto**: Clarificou a distinção entre `Registro` (temporário) e `empresaId` (permanente no JSON), melhorando a experiência do usuário.

### 5. **Reorganização do `MenuPrincipal()` e `sistema_vagas()`**
   - **Motivo**: Inicialmente, `sistema_vagas()` era chamada antes de ser definida, causando um erro `NameError`.
   - **Alteração**: Reorganizamos o código para que todas as funções sejam definidas antes do `MenuPrincipal()` e da chamada principal no `__main__`.
   - **Impacto**: Garantiu que todas as funções estivessem disponíveis quando chamadas, eliminando erros de execução.

### 6. **Estrutura do Loop Principal para o Menu**
   - **Motivo**: Para melhorar a usabilidade, adicionamos a opção de sair do sistema após cada operação.
   - **Alteração**: Colocamos o `MenuPrincipal()` dentro de um loop `while` no final do script, permitindo que o usuário escolha entre continuar ou encerrar o sistema.
   - **Impacto**: Tornou o sistema mais intuitivo, permitindo múltiplas operações sem reiniciar o programa.

### 7. **Correção de Testes e JSON Inicial**
   - **Motivo**: O arquivo `empresas.json` inicial estava sem `empresaId`, o que dificultava o teste do cadastro de vagas.
   - **Alteração**: Adicionamos uma entrada de teste com `empresaId` ao `empresas.json` para garantir o funcionamento da função `empresa_existe()` e do cadastro de vagas.
   - **Impacto**: Facilitou testes precisos, confirmando que todas as validações e relações entre empresas e vagas funcionam corretamente.

