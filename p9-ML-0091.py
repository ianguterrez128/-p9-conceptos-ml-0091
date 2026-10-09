import pandas as pd
# ian gutierrez NC = 0091

datos26 = {
    'distancia_km': [3.0, 1.1, 6.5, 2.8, 4.7],
    'trafico_nivel': [1, 3, 2, 1, 3],
    'edad_repartidor': [27, 34, 44, 21, 39],
    'tiempo_entrega_min': [21, 10, 55, 19, 44]
}

df = pd.DataFrame(datos26)

X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']]
y = df['tiempo_entrega_min']

print("--- DATOS DE ENTRADA (X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (y) ---")
print(y.head(2))


# programa realizado por ian gutierrez NC = 0091
print("programa realizado por ian gutierrez NC = 0091")