# Task 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open("words.txt", "r") as fin:
# for line in fin:
# words = line.split()
# for word in words:
# if "абв" in word:
# words.remove(word)
# sentence = " ".join(words)
# print(sentence)


# Task 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# import datetime

# def ReadFileToList(fileName):
# with open(fileName, "r") as file:
# result = file.read()
# file.close
# return result

# def WriteListToFile(fileName,textData):
# todayDateTime=datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
# textData='The text was unzipped on '+ todayDateTime + ': ' + textData +'\n'
# with open(fileName, "a") as file:
# file.write(textData)
# file.close

# def StrToList(str):
# myList = [n for n in str]
# return myList

# def ZipFile(text):
# counter=1
# zipText=''
# for i in range (len(text)-1):
# if text[i]==text[i+1]:
# counter=counter+1
# else:
# zipText=zipText+text[i]+str(counter)
# counter=1
# if text[len(text)-2]!=text[len(text)-1]:
# zipText=zipText+text[len(text)-1]+str(counter)
# return zipText

# def UnzipFile(zipText):
# unzipText=''
# for i in range(0,len(zipText),2):
# unzipText=unzipText+(zipText[i]zipText[i+1)
# return unzipText

# def CheckOperation(text,unzipText):
# if text==unzipText:
# return True
# else:
# return False

# text=ReadFileToList('Text.txt')
# print(f"Entered text is: {text}")
# myList=StrToList(text)
# zipText=ZipFile(myList)
# print(f"Zipped text is: {zipText}")
# unzipText=UnzipFile(zipText)
# print(f"Unipped text is: {unzipText}")
# if CheckOperation(text,unzipText):
# print("The file was unzipped successfully!")
# WriteListToFile('OutputText.txt',unzipText)
# else:
# print("The file was unzipped with errors!")