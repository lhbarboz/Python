def calculo(t):
	lista = []
	inicio = 0
	for i in range(1000):
		lista.append(inicio)
		inicio+=1
		if inicio == t:
			inicio = 0
		print(f'N[{i}] = {lista[i]}')
		
def main():
	t = int(input())
	calculo(t)

main()