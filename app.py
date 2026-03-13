# Calculadora de Consumo de Energia

print("=== Calculadora de Consumo Elétrico ===")

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (horas): "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado
valor_kwh = 0.75
custo = consumo_mensal * valor_kwh

# Saída formatada usando %
print("\n===== Resultado =====")
print("Aparelho: %s" % aparelho)
print("Consumo estimado: %.2f kWh/mês" % consumo_mensal)
print("Custo estimado: R$ %.2f por mês" % custo)
