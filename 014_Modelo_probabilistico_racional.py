import numpy as np

# Datos de ejemplo: preferencias de usuario
# Cada fila representa un usuario y cada columna representa un artículo o ítem.
# Los valores son las calificaciones o preferencias del usuario por los ítems.
user_preferences = np.array([
    [4, 5, 0, 1, 0],
    [0, 0, 3, 4, 5],
    [1, 0, 5, 0, 2],
    [3, 4, 0, 5, 0],
])

# Calcular la probabilidad de que un usuario prefiera un ítem en particular
def calculate_item_probability(user_preferences, user_id, item_id):
    # Calcular la media de las calificaciones del usuario
    user_ratings = user_preferences[user_id]
    user_mean_rating = np.mean(user_ratings)

    # Calcular la desviación estándar de las calificaciones del usuario
    user_std_deviation = np.std(user_ratings)

    # Calcular la probabilidad de preferir el ítem basándose en una distribución normal
    item_rating = user_preferences[:, item_id]
    item_mean_rating = np.mean(item_rating)
    item_std_deviation = np.std(item_rating)

    # Calcular la probabilidad usando la función de densidad de probabilidad de la distribución normal
    probability = 1 / (user_std_deviation * np.sqrt(2 * np.pi)) * \
        np.exp(-0.5 * ((item_mean_rating - user_mean_rating) / user_std_deviation) ** 2)

    return probability

# Ejemplo de cálculo de probabilidad para un usuario e ítem específicos
user_id = 0
item_id = 2

probability = calculate_item_probability(user_preferences, user_id, item_id)
print(f"Probabilidad de que el usuario {user_id} prefiera el ítem {item_id}: {probability:.4f}")
