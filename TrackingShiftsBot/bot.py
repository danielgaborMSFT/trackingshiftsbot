from importlib.resources import path
import random

def printWeek(week):
    #shuffle the days between them
    random.shuffle(week)
    print('Monday    | morning: ',  week[0][0], ' | afternoon: ',  week[0][1])
    print('Tuesday   | morning: ',  week[1][0], ' | afternoon: ',  week[1][1])
    print('Wednesday | morning: ',  week[2][0], ' | afternoon: ',  week[2][1])
    print('Thursday  | morning: ',  week[3][0], ' | afternoon: ',  week[3][1])
    print('Friday    | morning: ',  week[4][0], ' | afternoon: ',  week[4][1],"\n")

def saveNewWeek(currentWeek):
    with open('lastWeek.txt', 'w') as file:
        for engineer in currentWeek:
            file.write(engineer[0]+ ', ' + str(engineer[3])+'\n')
    file.close()


def readLastWeek():
    file = open('lastWeek.txt', 'r')
    engineers = file.readlines()
    file.close()
    engineersLastWeek=[]
    
    for engineer in engineers:
        engineersLastWeek.append(engineer.split(', '))
        
    engineersLastWeek = [[x[0], int(x[1])] for x in engineersLastWeek]
    
    lastWeek={}
    for engineer in engineersLastWeek:
        key, value = engineer[0], engineer[1]
        lastWeek[key] = value

    return lastWeek

def main(currentWeek):
    days= [['morning','afternoon'] for x in range(5)]

    lastWeek=readLastWeek()
    print('\n\nlast week number of shifts: ', lastWeek, '\n')

    for day in days:
        random.shuffle(currentWeek)
        currentWeek=sorted(currentWeek, key=lambda x: (x[3], random.random()))
        morningFound=False
        afternoonFound=False
        
        for engineer in currentWeek:
            if(morningFound is False or afternoonFound is False):
                dayCompleted=False
                #morning search
                if(morningFound== False and engineer[1]==1 and lastWeek[engineer[0]]<3):
                    day[0]=engineer[0]
                    engineer[3]+=1
                    morningFound=True
                    dayCompleted=True
                    lastWeek[engineer[0]]+=1

                #afternoon search
                
                if(afternoonFound==False and dayCompleted==False and engineer[2]==1 and lastWeek[engineer[0]]<3):
                    day[1]=engineer[0]
                    engineer[3]+=1
                    afternoonFound=True
                    lastWeek[engineer[0]]+=1

   
   
    printWeek(days)
    print("number of shifts from the last 2 weeks:  ", lastWeek)
    saveNewWeek(currentWeek)


#engineer will be stored as a list
#[engineer Name, morning shifts available, afternoon shifts available, number of shifts]
engineersList=[["Daniel", 0, 0, 0], ["Hugo", 1, 1, 0], ["Manuel", 1, 0, 0],  ["Pedro", 1, 1, 0],
 ["Michael", 1, 1, 0], ["Eric", 1, 1, 0], ["Andreea", 1, 1, 0],
 ["Klaus", 1, 0, 0], ["Claudiu", 0, 0, 0], ["Martin", 0, 0, 0]]

random.shuffle(engineersList)
main(engineersList)