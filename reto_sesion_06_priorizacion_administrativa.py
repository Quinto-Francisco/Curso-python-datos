# Reto sesión 6 - Priorizador de solicitudes administrativas

##1. Datos de la solicitud (registro de prueba)
solicitud = {
    "codigo": "ADM-004",
    "tipo": "Actualización de datos",
    "area_solicitante": "Talento Humano",
    "dias_pendiente": 8,
    "afecta_operacion": True,
    "estado": "Cerrada",
}

##2. Consultar los datos que se van a evaluar
estado = solicitud["estado"]
dias_pendiente = solicitud["dias_pendiente"]
afecta_operacion = solicitud["afecta_operacion"]

##3. Evaluar la clasificación de prioridad según los criterios establecidos
if estado == "Cerrada":
    clasificacion = "CERRADA"
    accion = "registrar que no requiere nueva gestión"
elif afecta_operacion and dias_pendiente >= 2:
    clasificacion = "URGENTE"
    accion = "escalar al responsable para atención prioritaria"
elif afecta_operacion or dias_pendiente >= 5:
    clasificacion = "PRIORITARIA"
    accion = "Programar atención preferente."
else:
    clasificacion = "NORMAL"
    accion = "Mantener en el flujo habitual de atención."

##4. resumen de la solicitud
print("Resumen de la solicitud:")
print("Código:", solicitud["codigo"])
print("Tipo:", solicitud["tipo"])
print("Estado:", estado)
print("Clasificacion de atención:", clasificacion)
print("Acción recomendada:", accion)



# =====================================================
# PREGUNTAS DE REFLEXIÓN
# =====================================================

# 1. ¿Por qué la solicitud cerrada debe evaluarse antes que las demás condiciones?
# Porque una solicitud cerrada ya no requiere nueva gestión, sin importar sus días
# pendientes ni si afecta la operación.

# 2. ¿Qué diferencia hay entre utilizar and y utilizar or en las reglas de prioridad?
# Con "and" deben cumplirse las dos condiciones a la vez (afecta la operación Y
# lleva 2 días o más), por eso es más estricta y se usa para URGENTE. Con "or"
# basta con que se cumpla una (afecta la operación O lleva 5 días o más), por eso
# es más amplia: una solicitud que no afecta la operación pero lleva 5 días
# también es PRIORITARIA.

# 3. ¿Qué podría ocurrir si cambiamos el orden de las condiciones?
# Python se detiene en la primera condición verdadera, así que el resultado
# cambiaría. Por ejemplo, si PRIORITARIA (con "or") va antes que URGENTE, una
# solicitud pendiente que afecta la operación con 2 días se clasificaría como
# PRIORITARIA y nunca llegaría a URGENTE.