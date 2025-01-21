student_data={'id1':
        {'name':['zara'],
        'grade':['5'],
        'subject':['english, hindi, maths']
        },
        
        'id2':
        {'name':['zara'],
        'grade':['5'],
        'subject':['english, hindi, maths']
        },
         
         'id3':
        {'name':['umar'],
        'grade':['5'],
        'subject':['english, hindi, maths']
        },
        'id4':
        {'name':['mama'],
        'grade':['5'],
        'subject':['english, hindi, maths']
        },
        }

result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)        



         
         
            
        
        


       
                          