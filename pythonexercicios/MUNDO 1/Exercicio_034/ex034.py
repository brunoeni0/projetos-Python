from cores import verde, branco,amarelo
s =float(input('{}Quanto e teu salário '.format(branco)))
a1=s+s*10/100
a2=s+s*15/100
if s > 1250.00:
    print('{}Seu aumento e de 10% que da {}{}'.format(amarelo, branco, int(a1)))
else:
    print('{}Seu aumento é de 15% que da {}{}'.format(verde, branco, int(a2)))
