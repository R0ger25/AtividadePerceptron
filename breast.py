import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from perceptron import *
from util import *
import time

# PASSO 1: Gerar o Dataset
print("=" * 50)
print("EXEMPLO: Breast Dataset")
print("=" * 50)

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
print(f"Features: {cancer.feature_names}")
print(f"Classes: {cancer.target_names}")  # ['malignant' 'benign']

# Versão B
# X = X[:, [0, 2]]

print(f"Dataset gerado:")
print(f"- Amostras: {X.shape[0]}")
print(f"- Features: {X.shape[1]}")
print(f"- Classes: {np.unique(y)}")

# PASSO 2: Dividir em Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(
	X, y,
	test_size=0.3,        # 30% para teste
	random_state=42,
	stratify=y            # Mantém proporção das classes
)

print(f"\nDivisão treino/teste:")
print(f"- Treino: {len(X_train)} amostras")
print(f"- Teste: {len(X_test)} amostras")

# PASSO 3: Normalização
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)   # Fit no treino
X_test_std = scaler.transform(X_test)         # Apenas transform no teste


# PASSO 4: Treinar o Perceptron
ppn = Perceptron(learning_rate=0.01, n_epochs=50)

start_time = time.perf_counter() # Começa contar o tempo

ppn.fit(X_train_std, y_train)

end_time = time.perf_counter() # Para de contar o tempo

training_time = end_time - start_time # Calcula o tempo de treinamento

# PASSO 5: Avaliar o Modelo
y_pred = ppn.predict(X_test_std)
accuracy_train = accuracy_score(y_train, ppn.predict(X_train_std))
accuracy_test = accuracy_score(y_test, y_pred)

print(f"\nResultados:")
print(f"- Acurácia Train: {accuracy_train:.2%}")
print(f"- Acurácia Teste: {accuracy_test:.2%}")
print(f"- Tempo de Treinamento: {training_time:.8f} segundos")
print(f"- Erros finais no treino: {ppn.errors_history[-1]}")
print(classification_report(y_test, y_pred, target_names=cancer.target_names))

# Verificar convergência
if 0 in ppn.errors_history:
	conv_epoch = ppn.errors_history.index(0)
	print(f"- Convergiu na época: {conv_epoch + 1}")
else:
	print("- Não convergiu completamente")


# # PASSO 6: Visualizar Resultados
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# # Subplot 1: Regiões de Decisão
# axes[0].set_title('Regiões de Decisão - Breast')
# plot_decision_regions(X_train_std, y_train, classifier=ppn)
# axes[0].set_xlabel('Feature 1 (normalizada)')
# axes[0].set_ylabel('Feature 2 (normalizada)')

# # Subplot 2: Curva de Convergência
# axes[1].plot(range(1, len(ppn.errors_history) + 1), ppn.errors_history, marker='o')
# axes[1].set_xlabel('Épocas')
# axes[1].set_ylabel('Número de erros')
# axes[1].set_title('Convergência do Treinamento')
# axes[1].grid(True, alpha=0.3)

# plt.tight_layout()
# plt.show()

# PASSO 7: Análise dos Pesos Aprendidos
print(f"\nPesos aprendidos:")
print(f"- w1: {ppn.weights[0]:.4f}")
print(f"- w2: {ppn.weights[1]:.4f}")
print(f"- bias: {ppn.bias:.4f}")

# A equação da fronteira de decisão é:
# w1*x1 + w2*x2 + bias = 0
# ou seja: x2 = -(w1/w2)*x1 - (bias/w2)
if ppn.weights[1] != 0:
	slope = -ppn.weights[0]/ppn.weights[1]
	intercept = -ppn.bias/ppn.weights[1]
	print(f"\nEquação da fronteira de decisão:")
	print(f"x2 = {slope:.2f} * x1 + {intercept:.2f}")
 
# PASSO 8: Visualizar a Matriz de Confusão
print("\n" + "="*50)
print("Matriz de Confusão")
print("="*50)

cm = confusion_matrix(y_test, y_pred) # Gera a matriz de confusão

# Printa a matriz de confusão
print("Linhas: Valor Real | Colunas: Valor Previsto\n")
print(f"Classes: {np.unique(y)}") # Para te lembrar a ordem (ex: [0 1])
print(cm)
print("="*50)