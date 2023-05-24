def fibonacci(n, testes):
#-----------------------------------------------------
	fibonacci = [0,1,1]
	for i in range (2,60):
		fibonacci.append(fibonacci[i-1]+fibonacci[i])
#-----------------------------------------------------
	print(f'Fib({testes}) = {fibonacci[testes]}')
	

def main():
	n = int(input())
	for i in range(n):
		testes = int(input())
		fibonacci(n,testes)

main()