import csv

gastos_por_categoria = {}
total_gasto = 0

with open('extrato.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        valor = float(linha['Valor'])

        if valor < 0:
            categoria = linha['Categoria']
            valor_gasto = abs(valor)

            if categoria in gastos_por_categoria:
                gastos_por_categoria[categoria] += valor_gasto

            else:
                gastos_por_categoria[categoria] = valor_gasto

            total_gasto += valor_gasto

print("\n RELATÓRIO DE GASTOS")
print("-" * 30)
for categoria, valor in gastos_por_categoria.items():
    print(f"{categoria}: R$ {valor:.2f}")
print("-" * 30)
print(f"TOTAL GASTO: R$ {total_gasto:.2f}\n")