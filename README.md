# Las Formas - Desenhando com Robôs no ROS

![Turtlesim](https://raw.githubusercontent.com/ros/ros_tutorials/noetic-devel/turtlesim/images/turtlesim.png)

Este projeto utiliza o **ROS (Robot Operating System)** para controlar um robô simulado, o `turtlesim`, e fazê-lo desenhar diferentes formas geométricas na tela. É um ótimo exemplo prático para aprender sobre a manipulação de tópicos (topics) e o controle de movimento de robôs com ROS e Python.

## Formas Implementadas

O robô é capaz de desenhar as seguintes formas:

* Quadrado
* Triângulo
* Estrela
* Círculo

## Pré-requisitos

Antes de executar, certifique-se de que você tem o seguinte ambiente configurado:

* **ROS Noetic Ninjemys**: O projeto foi desenvolvido e testado nesta versão do ROS.
* **Pacote `turtlesim`**: Geralmente incluído na instalação padrão do ROS (`ros-noetic-desktop-full`).

## Como Executar o Projeto

Siga os passos abaixo para ver o robô em ação.

1.  **Inicie o ROS Master:**
    Abra um novo terminal e execute o comando:
    ```bash
    roscore
    ```

2.  **Inicie o Simulador Turtlesim:**
    Abra um segundo terminal e execute o nó do `turtlesim`:
    ```bash
    rosrun turtlesim turtlesim_node
    ```
    Uma janela com o robô (uma tartaruga) no centro deverá aparecer.

3.  **Execute o Script `las_formas.py`:**
    Abra um terceiro terminal, navegue até a pasta onde o arquivo `las_formas.py` está salvo e execute-o com Python 3:
    ```bash
    python3 las_formas.py
    ```

4.  **Escolha uma Forma:**
    No terminal onde você executou o script, um menu aparecerá. Digite o número correspondente à forma que você deseja desenhar e pressione Enter. A tartaruga começará a se mover e a desenhar a forma escolhida.

## Como Funciona

O script `las_formas.py` funciona da seguinte maneira:

1.  **Inicializa um Nó ROS**: Cria um nó chamado `las_formas` para se comunicar com o restante do sistema ROS.
2.  **Cria um Publisher**: O script publica mensagens do tipo `Twist` no tópico `/turtle1/cmd_vel`. O simulador `turtlesim` "escuta" este tópico para receber comandos de velocidade linear e angular, que controlam o movimento do robô.
3.  **Funções de Desenho**: Para cada forma geométrica, existe uma função específica (`desenha_quadrado`, `desenha_triangulo`, etc.) que calcula e publica as velocidades necessárias para mover o robô em trajetórias retas ou curvas, formando o desenho desejado.
4.  **Menu Interativo**: Um menu simples no terminal permite que o usuário escolha qual função de desenho será executada.

## Contribuição

Sinta-se à vontade para contribuir com o projeto! Você pode adicionar novas formas, melhorar a interface ou otimizar o código. Basta fazer um *fork* do repositório e abrir um *pull request*.
