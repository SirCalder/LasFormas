# 🐢 Las Formas - Desenhando com Robôs no ROS

> Este projeto utiliza o **ROS (Robot Operating System)** para controlar um robô simulado, o `turtlesim`, e fazê-lo desenhar diferentes formas geométricas na tela. É um ótimo exemplo prático para aprender sobre a manipulação de tópicos (topics) e o controle de movimento de robôs com Python.

---

### ✨ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ROS](https://img.shields.io/badge/ROS-Noetic-22314E?style=for-the-badge&logo=ros&logoColor=white)

---

### 🎨 Demonstração

A imagem abaixo mostra a tartaruga do `turtlesim` após desenhar algumas formas.

*Dica: Para um efeito ainda melhor, você pode usar um programa de captura de tela para gravar um GIF do seu robô desenhando e substituir a imagem abaixo!*

![Turtlesim](http://wiki.ros.org/turtlesim?action=AttachFile&do=get&target=turtlesim_screenshot.png)

---

### 🚀 Funcionalidades

O robô é capaz de desenhar as seguintes formas:
- Quadrado:white_medium_square:
- Triângulo :small_red_triangle:
- Estrela :star:
- Círculo :black_circle:
- Pentágono (⬟)
- Hexágono (⬣)
- Coração (❤️)

---

### 🔧 Pré-requisitos

Antes de executar, certifique-se de que você tem o seguinte ambiente configurado:

- **ROS Noetic Ninjemys**: O projeto foi desenvolvido e testado nesta versão do ROS.
- **Pacote `turtlesim`**: Geralmente incluído na instalação padrão do ROS (`ros-noetic-desktop-full`).

---

### ▶️ Como Executar o Projeto

Siga os passos abaixo para ver o robô em ação.

1.  **Inicie o ROS Master:**
    Abra um novo terminal e execute o comando:
    ```bash
    roscore
    ```

2.  **Inicie o Simulador Turtlesim:**
    Abra um **segundo terminal** e execute o nó do `turtlesim`:
    ```bash
    rosrun turtlesim turtlesim_node
    ```
    *Uma janela com a tartaruga no centro deverá aparecer.*

3.  **Execute o Script `las_formas.py`:**
    Abra um **terceiro terminal**, navegue até a pasta onde o arquivo `las_formas.py` está salvo e execute-o:
    ```bash
    python3 las_formas.py
    ```

4.  **Escolha uma Forma:**
    No terminal onde você executou o script, um menu aparecerá. Digite o nome da forma que você deseja desenhar (ex: `quadrado`) e pressione Enter. A tartaruga começará a se mover e a desenhar!
