a = input('Enter height(m): ')
b = input('Enter weaght(kg): ')
bmi = float(b) / float(a)**2

chart_bmi =  '========================'
count_list = round(bmi) - 17



if 16 > round(bmi):
  print('BMI is too small')

elif round(bmi) < 40:
  li = list(chart_bmi)
  li[count_list] = '|'

  print(f"BMI = {round(bmi)}")
  print(f"16{''.join(li)}40")

else:
  print('BMI is too big')