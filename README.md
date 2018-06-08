US-EN


==========================================================================================
PT-BR

# CC-PDI-DominioDaFrequencia
Projeto que substituirá a prova3 de PDI UFPB: Identificar o domínio da frequência de uma imagem

## O que deve ser feito
Dada uma imagem I (RGB ou monocromática), de dimensões R x C, desenvolver uma aplicação para calcular e exibir, no domínio do espaço, uma aproximação de I obtida preservando-se o coeficiente DC e os n coeficientes AC mais importantes da DCT de I, em que n é um inteiro no intervalo [0, R x C - 1], a ser informado pelo usuário em tempo de execução. Todos os demais coeficientes devem ser zerados. A DCT-2D deve ser calculada utilizando-se a propriedade da separabilidade, aplicando-se diretamente a fórmula da DCT-1D, sem recorrer a bibliotecas prontas. Para imagens RGB, o processamento deve ser efetuado separadamente em cada banda. 

## Dependencias
[OpenCV](https://docs.opencv.org/3.0-beta/index.html)
```
sudo apt-get install python-opencv
```

numpy

## Como usar


## Grupo
- Alisson Galiza
- Aline Araujo
- Luiz Henrique
- Wesnydy