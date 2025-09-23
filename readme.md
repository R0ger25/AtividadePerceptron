# Atividade Perceptron

# Dupla

- Roger de Asiss Tedesco
- 

# Iris

1.  Descrição do Dataset
    - Número de amostras e features   
        - Amostras: 100, Features: 2.

    - Distribuição das classes
        - Classes: 2, [0 e 1].

    - É linearmente separável?
        - Sim.

2.  Resultados
    - Acurácia no treino e teste
        - 100% em ambos.

    - Número de épocas até convergência
        - 2 épocas.

    - Tempo de treinamento
        - Tempo de Treinamento: 0.00046840 segundos.

3.  Visualizações
    - Gráfico de convergência

    - Regiões de decisão (quando possível)

    - Matriz de confusão
        - [15 0]
        - [0 15]
4.  Análise
    - O perceptron foi adequado para este problema?
        - Sim. pois o problema era linearmente separável.

    - Que melhorias você sugeriria?
        - Nenhuma.

    - Comparação com suas expectativas
        - Ele atendeu as todas as expectativas.

# Moons

1.  Descrição do Dataset
    - Número de amostras e features   
        - Amostras: 200, Features: 2.

    - Distribuição das classes
        - Classes: 2, [0 e 1].

    - É linearmente separável?
        - Não.

2.  Resultados
    - Acurácia no treino e teste
        - Treino: 82,86% e Teste: 81,67%.

    - Número de épocas até convergência
        - Não houve convergência.

    - Tempo de treinamento
        - Tempo de Treinamento: 0.04311140 segundos

3.  Visualizações
    - Gráfico de convergência

    - Regiões de decisão (quando possível)

    - Matriz de confusão
        - [24 6]
        - [5 25]
4.  Análise
    - O perceptron foi adequado para este problema?
        - Não pois o problema não era linearmente separável.

    - Que melhorias você sugeriria?
        - 

    - Comparação com suas expectativas
        - Houve uma acurácia acima do esperado, em torno de 20% maior.

# Breast Cancer

1.  Descrição do Dataset
    - Número de amostras e features
        - Amostras: 569, Features: 30 -> ['mean radius' 'mean texture' 'mean perimeter' 'mean area' 'mean smoothness' 'mean compactness' 'mean concavity' 'mean concave points' 'mean symmetry' 'mean fractal dimension' 'radius error' 'texture error' 'perimeter error' 'area error' 'smoothness error' 'compactness error' 'concavity error' 'concave points error' 'symmetry error' 'fractal dimension error''worst radius' 'worst texture' 'worst perimeter' 'worst area' 'worst smoothness' 'worst compactness' 'worst concavity' 'worst concave points' 'worst symmetry' 'worst fractal dimension'].

    - Distribuição das classes
        - Classes: ['malignant' 'benign']

    - É linearmente separável?
        - Não.

2.  Resultados
    - Acurácia no treino e teste
        Versão A
        - Treino: 91,21% e Teste: 89,47%.
        Versão B
        - Treino: 98,24% e Teste: 97,08%.

    - Número de épocas até convergência
        - Não convergiu completamente em ambas versões.

    - Tempo de treinamento
        Versão A
        - Tempo de Treinamento: 0.11492060 segundos

        Versão B
        - Tempo de Treinamento: 0.11900340 segundos

3.  Visualizações
    - Gráfico de convergência

    - Regiões de decisão (quando possível)

    - Matriz de confusão
        Versão A
        - [59 5]
        - [13 94]

        Versão B
        - [ 61   3]
        - [  2 105]
4.  Análise
    - O perceptron foi adequado para este problema?
        - Não pois o problema não era linearmente separável. Pois os pontos estavam muitos juntos e dificilmente seria separavel pelo perceptron.

    - Que melhorias você sugeriria?
        - 

    - Comparação com suas expectativas
        - A versão com apenas 2 features me surpreendeu, pois ficou menos preciso do que a versão com todas as features.

# Ruído

1.  Descrição do Dataset
    - Número de amostras e features   
        - Amostras: 200, Features: 2.

    - Distribuição das classes
        - Classes: 2, [0 e 1].

    - É linearmente separável?
        - 100% não, mas chega bastante perto de ser separavel.

2.  Resultados
    - Acurácia no treino e teste
        - Treino: 97,14% e Teste: 96,67%.

    - Número de épocas até convergência
        - Não houve convergência.

    - Tempo de treinamento
        - Tempo de Treinamento: 0.04285330 segundos

3.  Visualizações
    - Gráfico de convergência

    - Regiões de decisão (quando possível)

    - Matriz de confusão
        - [29 0]
        - [ 2 29]
4.  Análise
    - O perceptron foi adequado para este problema?
        - Dependendo de como usar as configurações de métrica sim.

    - Que melhorias você sugeriria?
        - Ajeitar as métricas.

    - Comparação com suas expectativas
        - Depois que alterei as métricas houve um resultado até consideravelmente ótimo em relação ao esperado.

# Dataset Linearmente Separável Personalizado
