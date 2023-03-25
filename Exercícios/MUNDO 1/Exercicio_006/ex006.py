from cores import branco
n = int(input('{}Digite um número: '.format(branco)))
d = n * 2
t = n * 3
r = n ** (1/2)
print('{}O dobro de {} é {}.\n O triplo vale {}.\n A raiz quadrada de {} é igual {:.2f}.'.format(branco, n, d, t, n, r),end='')