import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Definindo as fases do framework
fases = [
    "Definição do Modelo de Negócio",
    "Construção do MVP",
    "Evolução para MMP",
    "Gestão da Backlog e Feedbacks",
    "Go-to-Market e Estratégia de Lançamento",
    "Monitoramento Contínuo e Otimização",
    "Revisão e Ajustes no Roadmap"
]

# Nível de maturidade para cada fase
maturidade = [1, 2, 3, 4, 5, 6, 7]

# Configurando o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(maturidade, fases, marker='o', linestyle='-', color='b')

# Adicionando rótulos e título
ax.set_xlabel("Nível de Maturidade")
ax.set_ylabel("Fases do Produto")
ax.set_title("Framework de Maturidade do Produto")
plt.yticks(maturidade, fases)

# Adicionando anotações para cada fase
for i, fase in enumerate(fases):
    ax.annotate(fase, (maturidade[i], i + 1), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

# Exibindo o gráfico
plt.grid(True)
plt.tight_layout()
plt.show()
