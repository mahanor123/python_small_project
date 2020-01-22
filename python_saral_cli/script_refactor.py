import requests
from pprint import pprint

saralUrl = "http://saral.navgurukul.org/api"

def requestSaral(url):
    return requests.get(url).json()
coursesUrl = saralUrl+"/"+"courses"
coursesUrlCall = requestSaral(coursesUrl) 



def displayCourse():
    courseIdList = [] 
    index = 0
    while index < len(coursesUrlCall["availableCourses"]):
        courseIndex = coursesUrlCall["availableCourses"][index]
        courseName = courseIndex["name"]
        courseId = courseIndex["id"]
        courseIdList.append(courseId)
        print str(index+1)+" ", courseName
        index = index + 1
    return courseIdList

def selectCoures(id):
    select = int(input("choose one coures"))
    selectId = courseIdList[select+1]
    return selectId


def start():
    courseIdList = displayCourse()
    selectCoures(courseIdList)
if __name__ == "__main__":
        start()