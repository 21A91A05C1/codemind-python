def check(n):  
   while True:  
       if '()' in n:  
           n=n.replace ( '()' , '' )  
       elif '{}' in n :
           
            n= n.replace ( '{}' , '' )  
       elif '[]' in n:  
           n= n.replace ( '[]' , '' )  
       else :  
           return not n
n=input()
print(check(n))