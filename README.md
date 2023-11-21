# Calculadora Simples em Python com Interface Gráfica

 Primeiramente, eu importei as bibliotecas PySimpleGUI e a biblioteca operadores com as funções desenvolvidas por mim, através da Documentação e alguns tutoriais consegui desenvolver minha própria lógica e pensei, porque não desenvolver uma simples calculadora?

É um projeto relativamente simples mas me desafiaria a aprender a desenvolver uma interface interativa que exibe as expressões e resultados em tempo real. Armazenando os valores em uma lista chamada 'expressao_atual', e ao mesmo tempo receber eventos como cliques em botões representados como números ou operações, também podendo interagir com o teclado. O que sinceramente foi uma parte a qual eu não fazia a menor ideia de como fazer inicialmente, mas estamos sempre aprendendo! 

Tem também algumas condicionais que possibilitam a comunicação de eventos e valores. Estou atualmente tentando diminuir o uso de condicionais tentando achar uma forma melhor de poder lidar com essa comunicação. E assim otimizar cada vez mais o projeto.

Pretendo atualizar esse projeto adicionando novas operações matemáticas, e novas funcionalidades como abas, créditos e algums outras informações.

A forma que usei para conseguir conectar o layout com os eventos foi, adicionar uma key aos textos. Por exemplo, o primeiro código: 

   [sg.Text('0', font='Arial', size=(30), justification='right', key='Zero')]   
   
A expressão começa com um o número 0 assim que o programa é iniciado, exibindo que ainda, nenhuma operação foi feita até o momento. a key='Zero' é atualizada quando operações são feitas pelo usuário imprimindo na interface com o código Janela['Zero'].update() sendo atualizada constantemente, exibindo também o número 0 assim que o valor é apagado. Sendo possivel apagar apenas um valor por vez, ou zerando tudo com o operador 'C', você pode ver isso nas funções em operadores.py
   O código Janela['Resultado'] Funciona exatamente da mesma forma. Tendo ['Resultado'] como uma key e um posição.

Liçença: esse código é livre para quem quiser fazer alterações, melhorias na interface ou no desempenho. Não se preocupe.
