import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generar_graficos():
    print("Generando gráficos econométricos...")
    
    df = pd.read_csv('data/enemdu_mincer_clean.csv')
    sns.set_theme(style="whitegrid")
    os.makedirs('outputs', exist_ok=True)
    
    # -------------------------------------------------------------
    # GRÁFICO 1: Perfil Experiencia - Log(Ingreso)
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    sns.regplot(
        data=df.sample(1000, random_state=42), 
        x='experiencia', 
        y='log_ingreso', 
        order=2, 
        scatter_kws={'alpha': 0.3, 'color': '#4f46e5'}, 
        line_kws={'color': '#dc2626', 'linewidth': 2.5}
    )
    plt.title('Perfil Experiencia-Ingresos (Mincer U-Invertida)', fontsize=12, fontweight='bold')
    plt.xlabel('Años de Experiencia Potencial')
    plt.ylabel('Logaritmo del Ingreso Laboral')
    plt.tight_layout()
    plt.savefig('outputs/perfil_experiencia_ingreso.png', dpi=300)
    plt.close()
    
    # -------------------------------------------------------------
    # GRÁFICO 2: Retornos a la Escolaridad por Género
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    sns.lineplot(
        data=df, 
        x='escolaridad', 
        y='log_ingreso', 
        hue='mujer', 
        palette={0: '#2563eb', 1: '#ec4899'}, 
        marker='o'
    )
    plt.title('Brecha Salarial de Género según Nivel de Escolaridad', fontsize=12, fontweight='bold')
    plt.xlabel('Años de Escolaridad')
    plt.ylabel('Logaritmo del Ingreso Promedio')
    plt.legend(title='Género', labels=['Hombre', 'Mujer'])
    plt.tight_layout()
    plt.savefig('outputs/brecha_salarial_escolaridad.png', dpi=300)
    plt.close()
    
    print("Gráficos generados con éxito en la carpeta 'outputs/'.")

if __name__ == "__main__":
    generar_graficos()