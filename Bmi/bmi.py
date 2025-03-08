height = float(input('Height: '))
weight = float(input('Weight: '))

bmi = weight / height ** 2
print(f'Your BMI: {bmi:.2f}')

if bmi < 16:
    print('Severe Thinness')
elif 16 <= bmi < 17:
    print('Moderate Thinness')
elif 17 <= bmi < 18.5:
    print('Mild Thinness')
elif 18.5 <= bmi < 25:
    print('Normal')
elif 25 <= bmi < 30:
    print('Overweight')
elif 30 <= bmi < 35:
    print('Obese Class I')
elif 35 <= bmi < 40:
    print('Obese Class II')
else:
    print('Obese Class III')
