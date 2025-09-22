import numpy as np
class Perceptron:
    """
    Implementação do algoritmo Perceptron para classificação binária.
    
    Parâmetros:
    -----------
    learning_rate : float
        Taxa de aprendizado (entre 0.0 e 1.0)
        - Valores menores: aprendizado mais lento, mas mais estável
        - Valores maiores: convergência mais rápida, mas pode oscilar
    
    n_epochs : int
        Número de passadas pelo dataset de treino
    """
    
    def __init__(self, learning_rate=0.01, n_epochs=100):
        self.learning_rate = learning_rate
        self.n_epochs = n_epochs
        self.weights = None
        self.bias = None
        self.errors_history = []  # Para acompanhar o progresso