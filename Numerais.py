from num2words import num2words

numero = int(input('Por favor, informe um número qualquer: '))

num_en = num2words(numero,lang='en')
print(f'The number {numero} that you typed, is written {num_en}, in English')

num_en_ord = num2words(numero,lang='en',to='ordinal')
print(f'The number {numero} that you typed, is written {num_en_ord}, in ordinal English')

num_pt = num2words(numero,lang='pt-br')
print(f'O número {numero} que você digitou, se escreve {num_pt}, em Português')

num_pt_ord = num2words(numero,lang='pt-br',to='ordinal')
print(f'O número {numero} que você digitou, se escreve {num_pt_ord}, em Português ordinal')

num_fr = num2words(numero,lang='fr')
print(f'Le nombre {numero} que vous avez tapé, s´écrit {num_fr}, en Français')

num_fr_ord = num2words(numero,lang='fr',to='ordinal')
print(f'Le nombre {numero} que vous avez tapé, s´écrit {num_fr_ord}, en Français ordinal')

num_es = num2words(numero,lang='es')
print(f'El número {numero} que escribió, se escribe {num_es}, en Español')

num_es_ord = num2words = num2words(numero,lang='es',to='ordinal')
print(f'El número {numero} que escribió, se escribe {num_es_ord}, en Español')



