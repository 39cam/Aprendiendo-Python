print('*** Bienvenidos a la casa de los espejos ***')

edad = int(input('\nCuál es tu edad?: '))
miedo_oscuridad = input('\nTienes miedo a la oscuridad? (Si / No): ').strip().lower() == 'si'

if not miedo_oscuridad and edad > 10:
    print('Puedes entrar a la casa de los espejos, Bienvenido(a) ☻')
elif miedo_oscuridad and edad > 10:
    print(f'Puedes entrar a la casa de los espejos bajo tu responsabilidad: esta podría ocasionarte mucho miedo')
else:
    print(f'No puedes entrar a la casa de los espejos, eres menor de 10 años: {edad}')