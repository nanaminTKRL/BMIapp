def bmi_calc(weight, height):
   # BMI測定プログラム
   weight = float(weight)
   height = float(height) / 100
   bmi = round(weight / (height ** 2))
   if bmi < 18.5:
       result = "痩せ型"
   elif (bmi >= 18.5) and (bmi < 25):
       result = "標準体型"
   elif (bmi >= 25) and (bmi < 30):
       result = "肥満(軽)"
   else:
       result = "肥満(重)"
   print("BMI: " + str(bmi))
   print("判定: " + result)
   return bmi , result
 
if __name__ == '__main__':
   bmi_calc()