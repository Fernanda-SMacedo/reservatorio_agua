# 🚰 Monitor de Reservatório de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

## Sobre o Projeto
O **Monitor de Reservatório de Água** é um script em Python desenvolvido para monitorar e classificar o nível atual de água em um reservatório. O sistema utiliza cores dinâmicas no terminal (através da biblioteca `colorama`) para alertar visualmente o operador sobre o estado crítico ou normal do nível de água.

---

## Regras de Negócio e Níveis

O programa tem a variável nivel_escolhido com o valor do nível para teste, exibindo cada situação correspondente com uma cor específica:

- **Nível 1:** Muito baixo (Crítico) — 🔴Vermelho
- **Nível 2:** Baixo — 🟡Amarelo
- **Nível 3:** Médio — 🟢Verde
- **Nível 4:** Alto — 🔵Ciano
- **Nível 5:** Muito alto — 🔵Azul
- **Inválido:** Caso seja digitado um valor fora do intervalo de 1 a 5, um alerta de erro é exibido.

---

## Tecnologias e Bibliotecas Utilizadas

- **Linguagem:** [Python 3](https://www.python.org/)
- **Biblioteca Externa:** [Colorama](https://pypi.org/project/colorama/) (para colorir as saídas no terminal)
- **Estruturas de Controle:** Cadeia de condicionais encadeadas (`if`, `elif`, `else`)
