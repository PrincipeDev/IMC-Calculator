altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

IMC = peso / (altura / 100) ** 2

if IMC < 18.5:
  print(f'seu IMC é de {IMC}, e é classificado como Baixo Peso')
elif IMC >= 18.5 and IMC < 24.9:
  print(f'seu IMC é de {IMC}, e é classificado como Peso Normal')
elif IMC >= 25 and IMC < 29.9:
  print(f'seu IMC é de {IMC}, e é classificado como Excesso de Peso')
elif IMC >= 30 and IMC < 34.9:
  print(f'seu IMC é de {IMC}, e é classificado como Obesidade')
else:
  print(f'sue IMC é de {IMC}, e é classificado como Obesidade Extrema')