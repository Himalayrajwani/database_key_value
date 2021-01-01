
# importing the main2 file("code" is the name of the file I have used) as a library
import main2 as obj
import time as t
from threading import Thread



# it is only used only for the better representation  Purpose -->

print(end="\n\n\n")
print("_".center(70,"_"))
A=4
for i in range(10):
    if  A==i:
        print("___Hello Freshworks___".center(70))
    print("||",end="                                                                    ")
    print("||")

print("Welcome Program is Going to  Start".center(70,"_"))

#main things are started here -->

#Creation of the key : value database-----
obj.create("Himachalpradesh",20,20)
obj.create("gujarat",80,50)
obj.create("jaisalmer",75)
obj.create("Jaipur",80)

#Reading of the key value database
print(end="\n\n\n")
print("Reading the key[gujarat] value ".center(70,"_"))
obj.read("gujarat")


print(end="\n\n\n")
print("Reading the key[ahemadabad] value which doesn't exists".center(70,"_"))
obj.read("ahemadabad")


print(end="\n\n\n")
print("Reading the key[Uttar_pradesh] value which doesn't exists and it also contain underscore".center(70,"_"))
obj.read("Uttar_pradesh")



print(end="\n\n\n")
print("Reading the key[Jaipur] value whose scope is expired".center(70,"_"))
obj.read("Jaipur")



#delete of the key value database
print(end="\n\n\n")

print("Deleting  the key[gujarat] value".center(70,"_"))
obj.delete("gujarat")


print(end="\n\n\n")
print("Deleting the key[Ahemdabad] value which doesn't exists".center(70,"_"))
obj.delete("Ahemdabad")


print(end="\n\n\n")
print("Deleting the key[Uttar_pradesh] value which doesn't exists and contain underscore".center(70,"_"))
obj.delete("Uttar_pradesh")

print(end="\n\n\n")
print("Deleting the key[Jaipur] value whose scope is expired".center(70,"_"))
obj.delete("Jaipur")


print(end="\n\n\n")
print("Deleting the key[gujarat] value which doesn't exists".center(70,"_"))
obj.delete("gujarat")



#modify the existing key value database------------>>>
print(end="\n\n\n")
print("Modifying the key[Jaipur] value  whose scope is expired".center(70,"_"))
obj.modify("Jaipur",85)

print(end="\n\n\n")
print("Modifying the key[Ahemdabad] value which doesn't exists".center(70,"_"))
obj.modify("Ahemdabad",69)


print(end="\n\n\n")
print("Modifying the key[Uttar_pradesh] value which doesn't exists and contain underscore".center(70,"_"))
obj.modify("Uttar_pradesh",75)

print(end="\n\n\n")
print("Modifying the key[gujarat] value whose scope is expired".center(70,"_"))
obj.modify("gujarat",83)

print(end="\n\n\n")



#try and execpt block started-->

print("__".center(100,"_"))
print("__".center(100,"_"))
try:
    t1=Thread(target=(obj.create or obj.read or obj.delete),args=("Jaipur",80,10)) #as per the operation
    t1.start()
    t.sleep(10)

    t2=Thread(target=(obj.create or obj.read or obj.delete),args=("Jaipur",85,20)) #as per the operation
    t2.start()
    t.sleep(15)
except Exception as e:
    print(end="\n\n")
    print("Error occur due to that reason".center(70,"_"),e,)
else:
    print("Original database".center(70,"_"),obj.dic)
finally:
    print("Program dies....!!!".center(70,"_"))



#the code also returns other errors like
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
