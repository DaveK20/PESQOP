import matplotlib as plt
import numpy as np

def plot_graph(x,y):
    # Plotando o gráfico
    x_vals = np.linspace(0, 1600, 400)
    y_restr_3 = (25000 - 10 * x_vals) / 8
    y_restr_4 = 4500 - x_vals
    y_restr_2 = np.full_like(x_vals, 6000)

    # Aplicar x <= 1500 na região viável
    x_limit = 1500
    viable_x = x_vals[x_vals <= x_limit]
    viable_y = np.minimum(np.minimum(y_restr_3[x_vals <= x_limit], y_restr_4[x_vals <= x_limit]), 6000)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_restr_3, label='10x + 8y ≤ 25000', color='blue')
    plt.plot(x_vals, y_restr_4, label='x + y ≤ 4500', color='green')
    plt.axhline(6000, color='red', linestyle='--', label='y ≤ 6000')
    plt.axvline(1500, color='orange', linestyle='--', label='x ≤ 1500')

    # Região viável
    plt.fill_between(viable_x, 0, viable_y, color='gray', alpha=0.3, label='Região Viável')

    # Solução ótima
    plt.plot(x.value(), y.value(), 'ko', label=f'Solução ótima: ({x.value()}, {y.value()})\nLucro = R${lucro_opt:.2f}')

    plt.xlabel("model de Luxo (x)")
    plt.ylabel("model Básico (y)")
    plt.title("Região Viável e Solução Ótima para Produção de Geladeiras")
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 1600)
    plt.ylim(0, 6500)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    solve('geladeiras', LpMaximize, 100*x+50*y, [
        x<=1500,
        y<=6000,
        10*x+8*y<=25000,
        x+y<=4500
    ])