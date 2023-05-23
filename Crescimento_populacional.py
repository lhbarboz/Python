#quanto anos para que o crescimento da cidade A passe a cidade B em numero de habitantes
def calculo(PA,PB,G1,G2):
	crescimentoA = 0
	crescimentoB = 0
	tempo = 0
	while PA <= PB:
		if tempo > 100:
			break
		crescimentoA = (int(PA * G1/100))
		PA += crescimentoA
		crescimentoB = (int(PB * G2/100))
		PB += crescimentoB
		tempo += 1

	if tempo <= 100:
		print(f'{tempo} anos.')
	
	elif tempo > 100:
		print('Mais de 1 seculo.')

def main():
	#numero de testes
	t = int(input())
	for i in range(t):
		PA, PB, G1, G2 = map(float,input().split())
		calculo(PA,PB,G1,G2)
main()