# src/generate_figures.py
import pandas as pd
import matplotlib.pyplot as plt
import helpers.DataLoader as Dtl


def plot_histogram(df, column, output_path):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column])
    plt.title(f"Distribución de {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")

    plt.savefig(output_path)
    plt.close()


def main():
    path = "./data/processed/RH_procesado.csv"
    reader = Dtl.DataLoader(path)
    df = reader.load_data()
    
    # print(df.head()) ## Para comprobar que funciona imprimimos en pantalla (opcional)

    # Asegúrate de que los datos estén correctamente procesados antes de intentar trazarlos
    plot_histogram(df, "Desercion", "./reports/figures/histograma_desercion_POO.png")


if __name__ == "__main__":
    main()
