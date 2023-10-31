import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear variables difusas
calidad_comida = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_comida')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de membresía para las variables difusas
calidad_comida['mala'] = fuzz.trimf(calidad_comida.universe, [0, 0, 5])
calidad_comida['buena'] = fuzz.trimf(calidad_comida.universe, [0, 5, 10])
servicio['malo'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['bueno'] = fuzz.trimf(servicio.universe, [0, 5, 10])
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Definir reglas difusas
regla1 = ctrl.Rule(calidad_comida['mala'] | servicio['malo'], propina['baja'])
regla2 = ctrl.Rule(servicio['bueno'], propina['alta'])
regla3 = ctrl.Rule(calidad_comida['buena'] | servicio['bueno'], propina['media'])

# Crear sistema de control difuso
sistema_propina = ctrl.ControlSystem([regla1, regla2, regla3])

# Simular el sistema con valores de entrada
propina_ctrl = ctrl.ControlSystemSimulation(sistema_propina)

# Definir valores de entrada
propina_ctrl.input['calidad_comida'] = 6.5
propina_ctrl.input['servicio'] = 9.8

# Realizar la inferencia difusa
propina_ctrl.compute()

# Obtener el valor de salida
print("Valor de propina:", propina_ctrl.output['propina'])
propina.view(sim=propina_ctrl)
