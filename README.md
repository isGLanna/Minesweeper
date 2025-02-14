# Projeto Campo Minado - Implementação em Python

## Sobre o Projeto

Este projeto foi desenvolvido em Python, utilizando as bibliotecas **pygame** e **sqlite3**. Essas tecnologias foram escolhidas por sua simplicidade e adequação ao desenvolvimento de jogos básicos que não exigem relacionamentos complexos de banco de dados.

### Notas Importantes

- Este código não é um exemplo ideal para um projeto, pois contém várias decisões que se desviam dos princípios da programação orientada a objetos.
- Os padrões e convenções do Python (PEP8) não foram seguidos estritamente.
- O código contém comentários que podem ser considerados "poluição de escrita" e não são relevantes para a funcionalidade do programa.

## Estrutura do Código

### Configurações Iniciais

As configurações padrão são definidas, tais como:

- **Cores**
- **Variáveis principais**
- **Volume**
- **Fontes**
- **Imagens**
- **Configurações da tela**

### Loop Principal

- O código começa no loop principal, chamando a função `main_menu()`.
- No menu principal, objetos "Button" são criados, recebendo parâmetros como tamanho, nome e posição.
- O loop aguarda interações (colisões) com os botões, que retornam uma "ação" para o loop principal.

### Início do Jogo

- Após selecionar as opções para jogar e nomear um jogador, a partida (`current_match`) é iniciada.
- As propriedades do campo são definidas com base no número de bombas e no tamanho do mapa.
- Duas matrizes são criadas:
  - **Matriz base**: contém números, bombas e campos vazios.
  - **Matriz do jogo**: contém caixas não reveladas e bandeiras.
- As bandeiras e o contador de sorte são carregados na tela antes da chamada de `request_image_rendering_user()`.

### Renderização do Jogo

- As configurações dos botões são ajustadas conforme o nível de dificuldade.
- Um loop interno de renderização é iniciado:
  - **Variáveis principais**:
    - `count`: conta as iterações do loop para calcular o tempo.
    - `last_render`: analisa se o jogador venceu após o último clique.
  - O loop atualiza os botões apenas quando ocorrem cliques.

### Gerenciamento de Cliques

A função `click_manager` gerencia as ações realizadas no jogo:

- Recebe a matriz, o tamanho e as posições das caixas em jogo.
- Verifica duas ações principais:
  - **Clique direito**: define uma bandeira.
  - **Clique esquerdo**: pressiona e abre o mapa.

---

## Requisitos

- Python 3.x
- Bibliotecas necessárias:
  ```bash
  pip install pygame
  pip install sqlite3
