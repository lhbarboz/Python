n = int(input())

resto = 0
digito = 1
binario = 0

##separar os digitos
while n / 2 > 0:
	resto = n % 2
	n //= 2
	binario += resto * (10**(digito - 1))
	digito += 1

print(binario)