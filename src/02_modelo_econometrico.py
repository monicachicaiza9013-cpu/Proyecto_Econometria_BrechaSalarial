import pandas as pd
import numpy as np
import statsmodels.api as sm
import json
import os

def estimar_modelos_mincer():
    print("Estimando modelos econométricos Mincerianos (OLS)...")
    
    df = pd.read_csv('data/enemdu_mincer_clean.csv')
    
    # -------------------------------------------------------------
    # MODELO 1: Minceriano Básico
    # -------------------------------------------------------------
    X1 = df[['escolaridad', 'experiencia', 'experiencia_sq']]
    X1 = sm.add_constant(X1)
    y = df['log_ingreso']
    
    model1 = sm.OLS(y, X1).fit()
    
    # -------------------------------------------------------------
    # MODELO 2: Minceriano Ampliado (Con Brecha de Género)
    # -------------------------------------------------------------
    df['interaccion_mujer_educ'] = df['mujer'] * df['escolaridad']
    X2 = df[['escolaridad', 'experiencia', 'experiencia_sq', 'mujer', 'interaccion_mujer_educ', 'urbano', 'horas_trabajo']]
    X2 = sm.add_constant(X2)
    
    model2 = sm.OLS(y, X2).fit()
    
    # Extraer métricas clave
    resultados = {
        "modelo_1_basico": {
            "r2": round(model1.rsquared, 4),
            "r2_adj": round(model1.rsquared_adj, 4),
            "f_stat": round(model1.fvalue, 2),
            "aic": round(model1.aic, 2),
            "coeficientes": {k: round(v, 4) for k, v in model1.params.to_dict().items()}
        },
        "modelo_2_ampliado": {
            "r2": round(model2.rsquared, 4),
            "r2_adj": round(model2.rsquared_adj, 4),
            "f_stat": round(model2.fvalue, 2),
            "aic": round(model2.aic, 2),
            "coeficientes": {k: round(v, 4) for k, v in model2.params.to_dict().items()}
        }
    }
    
    os.makedirs('outputs', exist_ok=True)
    with open('outputs/resultados_modelos.json', 'w') as f:
        json.dump(resultados, f, indent=4)
        
    print("Modelos OLS estimados con éxito.")
    print(f"-> Modelo 1 (R² Ajustado): {resultados['modelo_1_basico']['r2_adj']}")
    print(f"-> Modelo 2 (R² Ajustado): {resultados['modelo_2_ampliado']['r2_adj']}")

if __name__ == "__main__":
    estimar_modelos_mincer()