import matplotlib.pyplot as plt

def mostrar_mapa(gdf):

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.set_facecolor("#26db2f")

    gdf.plot(ax=ax, edgecolor="black", linewidth=0.5)

    plt.title("Mapa de Barrios Legalizados")
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")

    plt.show()

    return True

