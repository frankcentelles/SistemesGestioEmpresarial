'''
MEMOIZACIÓN

Con funciones internas se pueden hacer lógicas interesantes: crear
una minicaché interna para cálculos posteriores. Esta técnica se llama
memoization. Consiste en guardar en memoria de la función principal los
resultados de ejecuciones de la función interna.
Muy útil en situaciones en las que para llegar a un resultado se
necesitan los resultados anteriores.
'''
import timeit

def fibo(n):
    if n <= 1:
        return n # caso base
    else:
        return fibo(n-1) + fibo(n-2)
    
def memoize(f):
    '''Crea una caché del último resultado de f'''
    mem = {} # dict
    def mem_func(n):
        if n not in mem:
            mem[n] = f(n)
        return mem[n]
    return mem_func

mem_fibo = memoize(fibo) # versión memoized de fibo
nc = timeit.timeit('fibo(32)', globals = globals(), number = 1) # se ejecuta 1 vez
print(nc) # 0.3749675669996577
nc = timeit.timeit('fibo(32)', globals = globals(), number = 10) # se ejecuta 10 veces
print(nc) # 3.6652043369999774 (la anterior x 10)
c = timeit.timeit('mem_fibo(32)', globals = globals(), number = 1) # con caché 1 vez
print(c) # 0.3642976340001951 (similar a sin saché)
c = timeit.timeit('mem_fibo(32)', globals = globals(), number = 10) # con cache 10 veces
print(c) # 1.5429995983140543e-06 (rapidísimo)
c = timeit.timeit('mem_fibo(32)', globals = globals(), number = 1000) # con caché 1000 veces
print(c) # 6.248899990168866e-05 (rapidísimo)
# men_fibo(32) provoca la llamada de memoize(fibo(32)) que cachea fibo(32) en el diccionario
# (si no está) y retorna dicho # resultado. En el diccionario interno de memoize solo se
# pueden guardar objetos hasheables (método mágico __hash__)