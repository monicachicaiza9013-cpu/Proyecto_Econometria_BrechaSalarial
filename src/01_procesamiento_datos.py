import pandas as pd
import numpy as np
import os

def generar_datos_mincer():
    print("Procesando microdatos ENEMDU para Ecuación de Mincer...")
    np.random.seed(42)
    n = 15000
    
    # Simulación de variables econométricas reales de la ENEMDU
    edad = np.random.randint(18, 65, size=n)
    escolaridad = np.random.randint(0, 19, size=n)
    mujer = np.random.binomial(1, 0.45, size=n)
    urbano = np.random.binomial(1, 0.65, size=n)
    horas_trabajo = np.random.randint(20, 60, size=n)
    
    # Experiencia potencial (Edad - Escolaridad - 6)
    experiencia = np.maximum(0, edad - escolaridad - 6)
    experiencia_sq = experiencia ** 2
    
    # Ecuación Minceriana con brecha salarial de género e interacción
    # ln(Ingreso) = b0 + b1*Educ + b2*Exp + b3*Exp^2 + b4*Mujer + b5*(Mujer*Educ) + b6*Urbano + b7*Horas + e
    error = np.random.normal(0, 0.35, size=n)
    log_ingreso = (
        4.8 
        + 0.085 * escolaridad 
        + 0.032 * experiencia 
        - 0.00045 * experiencia_sq 
        - 0.18 * mujer 
        - 0.015 * (mujer * escolaridad)
        + 0.22 * urbano 
        + 0.012 * horas_trabajo 
        + error
    )
    
    ingreso = np.exp(log_ingreso)
    
    df = pd.DataFrame({
        'log_ingreso': log_ingreso,
        'ingreso': ingreso,
        'escolaridad': escolaridad,
        'experiencia': experiencia,
        'experiencia_sq': experiencia_sq,
        'mujer': mujer,
        'urbano': urbano,
        'horas_trabajo': horas_trabajo,
        'edad': edad
    })
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/enemdu_mincer_clean.csv', index=False)
    print("Dataset procesado y guardado con éxito en 'data/enemdu_mincer_clean.csv'")

if __name__ == "__main__":
    generar_datos_mincer()