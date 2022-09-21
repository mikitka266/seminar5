#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
str1 = input("Введите данные для преобразования в RLE алгоритм: ")
current_digit1, count1 = None, 0
for digit in str1:
   if current_digit1 != digit:
       if count1 > 0:
           print(count1, current_digit1)
       current_digit1, count1 = digit, 1
   else:
       count1 += 1
print(count1, current_digit1)

str2 = input("Введите данные для восстановления из RLE алгоритма: ")
count2= ''
decode= ''
for char in str2:
  if char.isdigit():
    count2==char
  else: 
    decode=count2*int(char)
print(decode)
  




#def decoding_rle(str2):
    #count = ''
    #str_decode = ''
    #for char in str2:
      #  if char.isdigit():
      #      count == char 
       # else:
       #     str_decode = char * int(count)
       #     count = ''
   # print(str_decode)    
