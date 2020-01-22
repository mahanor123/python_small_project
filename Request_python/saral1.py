import requests 
import json
import os
import pprint
saral_url="http://saral.navgurukul.org/api/courses"  
saral= requests.get(saral_url)
with open("./course.json","w") as f:
        f.write(saral.content)
response = saral.json()

if os.path.exists("./course.json"):
        print("welcome to saral")
        file=open("course.json","r")
        f= file.read()
else:
        with open("course.json","w") as f:
                f.write(saral.content)
        file=open("course.json","r")
        f= file.read()

id_list=[]
def cou():
    i = 0
    while(i < len(response['availableCourses'])):
        courses=response['availableCourses'][i]
        print(str(i + 1)+" "+ courses["name"])
        course_id=courses["id"]
        id_list.append(course_id)
        i +=1
    course=id_list 
    return(course)
demo = cou() 

a=int(raw_input("enter your exercise:-"))
print(demo[a-1])   
id=id_list[a-1]

saral_url1= "http://saral.navgurukul.org/api/courses/"+ str(id) +"/exercises"
print(saral_url1)
slug=[] 
saral1= requests.get(saral_url1)
with open("./exercise.json","w") as f:
        f.write(saral1.content)

response1 = saral1.json()
if os.path.exists("./exercise.json"):
          
        file=open("exercise.json","r")
        f= file.read()

else:
        with open("exercise.json","w") as f:
                f.write(saral1.content)
        file=open("exercise.json","r")
        f= file.read()


id_list1=[]

slug1=[]
def course1():
    i=0
    while(i < len(response1['data'])):
            courses=response1['data'][i]
            print(str(i + 1)+" "+ courses["name"])
            course_id=courses["childExercises"]
            id_list1.append(course_id)
            store_slug=courses["slug"]
            slug1.append(store_slug)
            i=i+1       
            
course1()
user=str(raw_input("enter anything and up:-"))
course=id_list1[a-1]
if((user)=="up"):
        cou()
        a=int(raw_input("enter your id:-"))
        id=id_list[a-1]
        
        saral_url1= "http://saral.navgurukul.org/api/courses/"+ str(id) +"/exercises"
        saral1= requests.get(saral_url1)
        response1 = saral1.json()
       
        course1()
else:
        int1=int(user)
        course=id_list1[int1-1]
        print course

j=0 
i=0   
while(i < len(response1['data'])):
        courses=response1['data'][i]
        print(str(i + 1)+" "+ courses["name"])
        course_id=courses["childExercises"]
        id_list1.append(course_id)
        store_slug=courses["slug"]
        slug1.append(store_slug)
        i=i+1       
        

while(j< len(course)):   
        
        course_id=course["childExercises"]
        
        course_name=course_id[j]["name"]
        print course_name

        print str(j+1)+" "+ course_name
        
        j=j+1
     
     
user_input=int(raw_input("enter childExercises:-"))

course=id_list1[user_input-1]


slug_s=[]
id_s=[]

k=0
while(k<len(course)):
        course_name=course[k]["name"]
        
        print str(k+1)+" "+ course_name
        slug_store=course[k]["slug"]
                
        slug_s.append(slug_store)
        id_store=course[k]["id"]
                        
        id_s.append(id_store)
        k=k+1

       
user_input=int (raw_input("enter your  slug:-"))
SLUG=slug_s[user_input-1]
ID=id_s[user_input-1] 


url="http://saral.navgurukul.org/api/courses/"+str(ID)+"/exercise/getBySlug?slug="+str(SLUG)
       
slug_url=requests.get(url)
res=slug_url.json()
content1=res["content"]
print content1
        
while True:
        user_input1=str(raw_input("enter p,n"))

        if(user_input1=="n" and user_input<len( slug_s)):
                #user_input+1
                
                if( user_input<len( slug_s)):
                        u=user_input+1

                        SLUG=slug_s[u-1]
                        ID=id_s[user_input] 


                        url="http://saral.navgurukul.org/api/courses/"+str(ID)+"/exercise/getBySlug?slug="+str(SLUG)
                
                        slug_url=requests.get(url)
                        res=slug_url.json()

                        
                        content1=res["content"]
                        print content1
                        user_input=user_input+1
                        #if(user_input==len( slug_s)):
                               # break

        elif(user_input1=="p" and user_input<len( slug_s)):
                if( user_input<len( slug_s)):
                        u=user_input

                        SLUG=slug_s[u-2]
                        ID=id_s[user_input] 


                        url="http://saral.navgurukul.org/api/courses/"+str(ID)+"/exercise/getBySlug?slug="+str(SLUG)
                
                        slug_url=requests.get(url)
                        res=slug_url.json()

                        
                        content1=res["content"]
                        print content1
                        user_input=user_input-1
                        if(user_input==1):
                                break
                
                #user_input+1


                

        

 
     