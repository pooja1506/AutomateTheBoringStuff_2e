import random

list1 = []


def HeadTailFunc():
    experiment = 0
    numberOfStreaks = 0
    while experiment < 1000:
        for i in range(1, 101):
            HeadTail = random.randint(0, 1)
            if HeadTail == 0:
                # print("H")
                list1.append("H")

            elif HeadTail == 1:
                # print("T")
                list1.append("T")
        #print(list1)
        # print("Length of List1", len(list1))
        for f in range(len(list1)-6):
            if list1[f] == list1[f+1] == list1[f+2] == list1[f+3] == list1[f+4] == list1[f+5] != list1[f+6]:
                numberOfStreaks = numberOfStreaks + 1
                # print(numberOfStreaks)
        experiment = experiment+1
        # print("Experiment: ",experiment)
    print("Number of Streaks",numberOfStreaks)
    print("percentage:" , numberOfStreaks/(100*1000)) 


HeadTailFunc()  # headtail function for list of randomly generated values
# myList = list1
# print(len(myList))


# def streak():
#     for f in range(len(myList)-6):
#         if myList[f] == myList[f+1] == myList[f+2] == myList[f+3] == myList[f+4] == myList[f+5] != myList[f+6]:
#             numberOfstreaks = numberOfStreaks + 1
#             print(numberOfStreaks)


# streak()
