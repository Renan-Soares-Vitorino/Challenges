fib1 = 0
fib2 = 1
fibValor = 0
n = int(input("Qual Valor deseja saber se está na Sequencia? "))
sequenciaFib = [fib1, fib2]

while fibValor < n:
    fibValor = fib1 + fib2
    fib1 = fib2
    fib2 = fibValor
    sequenciaFib.append(fibValor)

if n in sequenciaFib:
    print(f"O valor {n} esta na sequencia de Fibonacci")
else:
    print(f"O valor {n} não esta na sequencia de Fibonacci")

print(sequenciaFib)