# Tasas y límites del INSS y del IRRF en Brasil

# Tasas y límites del INSS
# Límites de salario para cada tasa
limite_inss = [1212.00, 2427.35, 3641.03, 7087.22]
tasa_inss = [0.075, 0.09, 0.12, 0.14]  # Tasas correspondientes

# Tasas y límites del IRRF
# Límites de salario para cada tasa
limite_irrf = [1903.98, 2826.65, 3751.05, 4664.68]
tasa_irrf = [0.075, 0.15, 0.225, 0.275]  # Tasas correspondientes
# Deducciones fijas para cada tramo
deduccion_irrf = [142.80, 354.80, 636.13, 869.36]

# Salario neto deseado
salario_neto_deseado = 3313.18

# Función para calcular el INSS corregida


def calcular_inss_corregido(salario_bruto):
    inss = 0
    for i in range(len(limite_inss)):
        if salario_bruto > limite_inss[i]:
            if i == 0:
                inss += limite_inss[i] * tasa_inss[i]
            else:
                inss += (limite_inss[i] - limite_inss[i-1]) * tasa_inss[i]
        else:
            if i == 0:
                inss += salario_bruto * tasa_inss[i]
            else:
                inss += (salario_bruto - limite_inss[i-1]) * tasa_inss[i]
            break
    return inss

# Función para calcular el IRRF


def calcular_irrf(salario_bruto, inss):
    base_irrf = salario_bruto - inss
    irrf = 0
    for i in range(len(limite_irrf)):
        if base_irrf > limite_irrf[i]:
            if i == len(limite_irrf) - 1 or base_irrf <= limite_irrf[i + 1]:
                irrf = base_irrf * tasa_irrf[i] - deduccion_irrf[i]
        else:
            break
    return irrf if irrf > 0 else 0

# Función para estimar el salario bruto a partir del neto corregida


def estimar_salario_bruto_corregido(salario_neto):
    salario_bruto = salario_neto
    while True:
        inss = calcular_inss_corregido(salario_bruto)
        irrf = calcular_irrf(salario_bruto, inss)
        neto_calculado = salario_bruto - inss - irrf
        if neto_calculado >= salario_neto:
            break
        salario_bruto += 10  # Ajuste incremental
    return salario_bruto


# Calcular el salario bruto estimado
salario_bruto_estimado_corregido = estimar_salario_bruto_corregido(
    salario_neto_deseado)
print(salario_bruto_estimado_corregido)
