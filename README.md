Minesweeper Project - Python Implementation

Sobre o Projeto

Este projeto foi desenvolvido em Python, utilizando as bibliotecas pygame e sqlite3. A escolha dessas tecnologias se deve à simplicidade e adequação ao desenvolvimento de jogos básicos que não exigem relacionamentos complexos no banco de dados.

Avisos Importantes

Este código não é um exemplo ideal para projeto, pois apresenta várias decisões que divergem da programação orientada a objetos.

Normas e convenções do Python (PEP8) não foram seguidas à risca.

O código contém comentários que podem ser considerados "lixo de escrita", não sendo relevantes para a funcionalidade do programa.

Estrutura do Código

Configurações Iniciais

São definidas configurações padrão, como:

Cores

Variáveis principais

- Volume

- Fontes

- Imagens

- Configurações de tela

- Loop Principal

Loop Principal

O código inicia no loop principal ao final, chamando a função main_menu().

No menu principal, objetos do tipo "Button" são criados, recebendo parâmetros como proporção, nome e posição.

O loop aguarda interações (colisões) com os botões, que retornam uma "action" para o loop principal.

Início do Jogo

Após selecionar as opções para jogar e nomear um jogador, a partida (current_match) é iniciada.

Propriedades do campo são definidas com base na quantidade de bombas e no tamanho do mapa.

Duas matrizes são criadas:

- Matriz de base: Contendo números, bombas e campos vazios.

- Matriz de jogo: Contendo caixas não reveladas e bandeiras.

Bandeiras e o contador de sorte são carregados na tela antes de chamar request_image_rendering_user().

Renderização do Jogo

Configurações para os botões são ajustadas conforme a dificuldade.

Um loop interno de renderização é iniciado:

Variáveis principais:

count: Conta as iterações do loop para calcular o tempo.

last_render: Analisa se o jogador venceu após o último clique.

O loop atualiza os botões apenas quando há cliques.

Gerenciamento de Cliques

A função click_manager gerencia as ações realizadas no jogo:

Recebe a matriz, o tamanho e as posições das caixas em jogo.

Verifica as duas ações principais:

- Botão direito: Define uma bandeira.

- Botão esquerdo: Pressiona e abre o mapa.

Requisitos

Python 3.x

Bibliotecas necessárias:

pygame

sqlite3 (padrão no Python)

Como Executar

Certifique-se de ter o Python 3.x instalado.

Instale as dependências com o seguinte comando:

```pip install pygame```

Execute o código principal:

```python main.py```

Contribuições

Este projeto é aberto para contribuições de qualquer usuário que deseja, mas recomenda-se refatorar o código para alinhar-se com as boas práticas de programação Python e melhorar a legibilidade e a manutenibilidade.
