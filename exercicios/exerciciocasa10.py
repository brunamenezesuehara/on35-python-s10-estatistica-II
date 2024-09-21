import numpy as np
from scipy import stats

# Alturas das alunas
alturas_turma = [157, 160, 157, 163, 170, 167, 174, 160, 169, 158, 161, 168, 162, 167, 167, 165, 170, 170]

# Média populacional
mu_populacional = 161  

# Cálculos
media_amostra = np.mean(alturas_turma)
desvio_padrao_amostra = np.std(alturas_turma, ddof=1)
n = len(alturas_turma)

# Estatística Z
z = (media_amostra - mu_populacional) / (desvio_padrao_amostra / np.sqrt(n))

# Valor p
p_valor = 2 * (1 - stats.norm.cdf(abs(z)))

# Exibe os resultados
print(f"Média da amostra: {media_amostra}")
print(f"Desvio padrão da amostra: {desvio_padrao_amostra}")
print(f"Estatística Z: {z}")
print(f"Valor p: {p_valor}")
