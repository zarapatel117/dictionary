data={'hi':3,'what':6,'hihi':6,'bye':6}
print("orignal dictionary=",(str(data)))
h=6

res=0
for key in data:
    if data [key]==h:
        res=res+1
print("frecuency of h is",(str(res)))        

