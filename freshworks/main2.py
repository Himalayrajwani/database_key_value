import time

#'dic' is the dictionary in which we store data
dic={}


#create block :--> that create the new key value in the database
#use syntax "create(key_name,value,timing_value)"


def create(key1,value1,timing=0):

    if key1 in dic:
        print(" Error! This key is already thier so you are not able to insert the key ") #error message1
    else:
        if (key1.lower().isalpha()):
            if len(dic)<=(1024*1024*1024) and value1<=(16*1024*1024):  #constraints for file size less than 1GB and Jasonobject value less than 16KB
                if timing==0:
                    l=[value1,timing]
                    dic[key1]=l
                    return dic
                else:
                    l=[value1,time.time()+timing]
                    if len(key1)<=32:  #constraints for input key_name capped at 32chars

                        dic[key1]=l
                        return dic
            else:
                print("Error ! Due Memory limit exceed ") #error message2
        else:
            print("The key is Invalid--->",key1) #error message3



#Read block:--> that reads the key and find out that key is in their or not
#for read operation
#use syntax "read(key_name)"
def read(key1):


    if key1 not in dic:
        print("This key  doesn't exists for Read operation .Please enter a valid key--->",key1) #error message4
    else:
        a=dic[key1]
        if a[1]!=0:
            if time.time()<=a[1]:  #comparing the present time with expiry time
                data=key1+":"+str(a[0])   #to return the value in the format of JasonObject i.e.,"key_name:value"
                return data
            else:
                print("Error !!!  Time to live  Property of a key is expired !!!")  #error message5
        else:
            data=key1+":"+str(a[0])
            return data



#delete block:--> In this block first they find the key and delete the key
def delete(key1):


    if key1 not in dic:
         print("This key  doesn't  exist for Delete operation .Please enter a valid key--->",key1)  #error message4
    else:
        a=dic[key1]
        if a[1]!=0:
            if time.time()<=a[1]: #comparing the current time with expiry time
                del dic[key1]
                print(f"{key1} is successfullly deleted ")
                return dic
            else:
                print("Error !!!  Time to live  Property of a key is expired !!!") #error message5
        else:
            del dic[key1]
            print(f"{key1} is succesfully deleted ")  # this shows that key is sucessfully deleted

            return dic


#Modify block :--> In this block updation process occurs

def modify(key1,value1):

    if key1 not in dic:
        print("This key  doesn't  exist for modify operation .Please enter a valid key--->",key1)   #error message6
    else:

        a=dic[key1]
        if a[1]!=0:
            if time.time()<=a[1]:
                l=[]
                l.append(value1)
                l.append(a[1])
                dic[key1]=l
                print("Successfully modified the key ")  #this shows that the key is sucessfully modified
                return dic
            else:
                print("Error !!!  Time to live  Property of a key is expired !!! ")  #error message5
        else:
            l1=[]
            l1.append(value1)
            l1.append(a[1])
            dic[key1]=l1

            print("Successfully modified the key")
            return dic





