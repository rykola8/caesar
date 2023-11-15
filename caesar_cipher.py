a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Symbol encryption function
def e(t, o):   
#Эта переменная используется для хранения результата процесса шифрования
  r = ""
  #из текста вытягиваются буквы, Он позволяет программе выполнять операции над каждым отдельным символом в строке "t".
  for c in t:
    #ищет в переменной а буквы из слова
    #если символ "c" отсутствует в строке "a", то сам символ "c" просто добавляется к результату "r".
    if (a.find(c) == -1):
      #Это эквивалентно записи r = r + c.
      r += c
    #в остальных случаях
    else:
      # шифрования символа путем сдвига его на определенное количество позиций в алфавите:
      #a.find(c) находит позицию символа c в строке а
      #Мы добавляем к этой позиции значение o (сдвиг)
      # мы используем оператор остатка от деления (%) на len(a), чтобы убедиться, что результат остается в пределах допустимых позиций в алфавите.
      r += (a[(a.find(c) + o) % len(a)])
  # В данном контексте этот оператор возвращает окончательный результат процесса шифрования, который хранится в переменной "r".
  return r

#Функция расшифрования символов
def d(t, o):
  r = ""
  for c in t:
    if (a.find(c) == -1):
      r += c
    else:
      r += (a[(a.find(c) - o) % len(a)])
  return r

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + e(text, rotation))
elif mode == 2:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + d(text, rotation))
elif mode == 3:
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
