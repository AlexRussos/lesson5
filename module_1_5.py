immutable_var=(4,5,6,'a','b','c',True)
print(immutable_var)
print(immutable_var[1])
#immutable_var[1]=15
print ("Комментарий к 3 заданию:\n"
       "Кортеж является объектом типа tuple и относится к неизменяемым типам данных.\n"
       "Но при этом кортеж может хранить изменяемые объекты.Например, может хранить список.\n"
       "А вот список в кортеже менять можно.")
mutable_list=[4,5,'a','b']
print(mutable_list)
mutable_list[2]=16
mutable_list[-4]='dog'
mutable_list[1]='cat'
mutable_list[3]=67
mutable_list.append("moon")
print(mutable_list)