file = ('dictionary.txt')

def fileread (file_name):
   file_name = open('dictionary.txt', 'r',encoding='UTF-8')
   print(file_name.read())
   file_name.close()
   return file_name
def filewrite(file_name):
   name = input("Ведите имя: ")
   file_name = open('dictionary.txt', 'a',encoding='UTF-8')
   file_name.write(name + '\n')
def filesarch(file_name):
   name = input('Введите имя для поиска: ')
   R = []
   f= open('dictionary.txt',encoding='UTF-8') 
   for i in f.readlines():
      R.append(i.split(' '))
   
   for i in R:
      if i[0] == name:
         str_i=' '.join(i)
         print(str_i)

def filechange(file_name):
   name = input('Ведите имя абонента, номер которого нужно изменить: ')
 
   R =[]
   f=open('dictionary.txt',encoding='UTF-8')
   for i in f.readlines():
      R.append(i.split(' '))
  
   print (R)  
   name1= input("Введите новый номер: ")
   for i in R:
      if i[0] == name:
         i[-1]=name1+"\n"
   print(R)  
   R_new=[]
   Str = ''
   for i in R:
      i_new=' '.join(i)
      R_new.append(i_new)
   
   for el in R_new:
      Str += el
   print(Str)
   f=open('dictionary.txt','w',encoding='UTF-8')
   f.write(Str)
   f.close()
   
def filedelete(file_name):
   name = input('Ведите имя, которое нужно удалить ')
   R =[]
   f=open('dictionary.txt',encoding='UTF-8')
   for i in f.readlines():
         R.append(i.split(' '))
   for i in R:
      if i[0] == name:
         R.remove(i)  
   print(R)
   R_new=[]
   Str = ''
   for i in R:
      i_new=' '.join(i)
      R_new.append(i_new)
   
   for el in R_new:
      Str += el
   print(Str)
   f=open('dictionary.txt','w',encoding='UTF-8')
   f.write(Str)
   f.close()
 

while True:
    print("1. Вывести на экран список всех абонентов")
    print("2. Добавить абонента")
    print("3. Найти номер по имени абонента")
    print("4. Изменить номер абонента")
    print("5. Удалить номер абонента")
    print("0. Выйти из меню")
    n = input("Выберите пункт: ")
    
    if n == "1":
      print(fileread(file))
    elif n == "2":
      fileread(file)
    elif n == "3":
      filesarch(file)
    elif n == "4":
      filechange(file)
    elif n == "5":
       filedelete(file)
       
    elif n == "0":
      break
    else:
      print("Вы ввели не правильное значение")


#filewrite(file)
#fileread(file)
#filesarch(file)
#filedelete(file)



#file.close()