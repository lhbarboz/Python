def calculo(testes):
	ndivisores = 1
	contador = 2
	aux = 0
	# determinando os divisores
	while aux <=testes:
		if ndivisores <=2:
			primos = testes / contador
			if testes % contador == 0:
				ndivisores += 1
			contador += 1
		aux += 1

	# é primo ou não
	if ndivisores == 2:
		print(f'{testes} eh primo')
	else:
		print(f'{testes} nao eh primo')

def main():
	nt = int(input())
	for i in range (nt):
		testes = int(input())
		calculo(testes)
main()