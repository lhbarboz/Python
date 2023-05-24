def calculo(x):
	n = [0]
	n[0]=x
	print(f'N[0] = {x:.4f}')
	for i in range(1,100):
		n.append(x/2)
		x /= 2
		print(f'N[{i}] = {x:.4f}')
def main():
	x = float(input())
	calculo(x)

main()