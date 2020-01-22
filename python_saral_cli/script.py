import requests
from pprint import pprint

saral_url = "http://saral.navgurukul.org/api"


def course(link):
    respon = requests.get(link)
    request = respon.json()
    # pprint (request)
    return request


courses_url = saral_url+"/"+"courses"
full_courses = course(courses_url)
# pprint (full_courses)


course_id_list = []
def courses_fun():
    index = 0
    while index < len(full_courses["availableCourses"]):
        courses_ex = full_courses["availableCourses"][index]
        course_name = courses_ex["name"]
        courses_id = courses_ex["id"]
        course_id_list.append(courses_id)
        print str(index)+" ", course_name, courses_id
        index = index + 1
courses_fun()


user_input = int(input("enter your exercise:-"))
user_id = course_id_list[user_input]
print(user_id)

print("All exerise")
saral_url1 = courses_url + "/"+str(user_id)+"/"+'exercises'
saral_url2 = courses_url + "/"+str(user_id)+"/"+'exercise'
exercise = course(saral_url1)
# pprint (exercise)

sub_exercises = []
slug_list = []


def exercise_fun():
    index1 = 0
    while index1 < len(exercise["data"]):
        data_exercise = exercise["data"][index1]
        all_exercise = data_exercise["parentExerciseId"]
        child_exercise = data_exercise["childExercises"]
        exercise_id = data_exercise["id"]
        sub_exercises.append(child_exercise)
        if all_exercise != []:
            exercise_name = data_exercise["name"]
            exercise_slug = data_exercise["slug"]
            slug_list.append(exercise_slug)
            print str(index1) + "*", exercise_name
        index1 = index1+1
exercise_fun()

user_input1 = int(input("enter your lesson?:-"))
use_exerise = slug_list[user_input1]
all_exercise = slug_list[user_input1]
print(use_exerise)

saral_url3 = saral_url2+"/"+"getBySlug?slug="+str(use_exerise)
saral_url4 = saral_url2+"/"+"getBySlug?slug="
print(saral_url3)

content = course(saral_url3)
content_name = content["content"]
print(content_name)

slug_list1 = []
sub_name = []


def child_func():
    if all_exercise != None:
        if sub_exercises[user_input1] != []:
            index2 = 0
            while index2 < len(sub_exercises[user_input1]):
                child_sub_ex = sub_exercises[user_input1][index2]
                sub_ex_name = child_sub_ex["name"]
                sub_name.append(sub_ex_name)
                sub_ex_slug = child_sub_ex["slug"]
                slug_list1.append(sub_ex_slug)
                print str(index2) + "%", sub_ex_name
                index2 = index2+1

            user_input2 = int(input("enter your topics:-"))
            sub_content = slug_list1[user_input2]
            saral_url5 = saral_url4 + str(sub_content)
            print(saral_url5)

            print_cont = course(saral_url5)
            cont_name = print_cont["content"]
            print(cont_name)
        return user_input2
child_func()



def contentNext():    
    user_input6 = int(input("enter your num question"))
    slug_list2 = slug_list1[user_input6+1] 
    url =  saral_url2+"/"+"getBySlug?slug="+ slug_list2
    urlCall = course(url)
    nextContent = urlCall['content']
    print (nextContent)
   

def contentPrevious():
    user_input7 = int(input("enter your num question"))
    slugList = slug_list1[user_input-1] 
    url1 = saral_url2+"/"+"getBySlug?slug="+ slugList
    urlCall = course(url1)
    previousContent = urlCall['content']
    print (previousContent)
   

while True:
    choose= raw_input("Enter 'n' to go to next exercise or 'p' to go to previous exercise or to exit enter e key :- ")
    if choose == 'n':
        contentNext() 
    elif choose == 'p':
        contentPrevious() 
    elif choose == 'e':
        print("\n\n----You choose exit from current COURSE.-------\n\n")
        break    
 