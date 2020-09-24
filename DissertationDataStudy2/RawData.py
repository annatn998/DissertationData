import csv
from os import listdir

data = listdir('.')
file = open('AllParticipantScoresRelStatus.csv','w')
file.write('Participant,Scores' + '\n')


for items in data:
    if '342405' in items:
        with open(items, newline='') as csvfile:
            temp_reader = csv.reader(csvfile, delimiter=',')
            data = list(temp_reader)
            relStatus = data[1][11].lower()
            gender = data[1][7].lower()
            profileGender = data[4][19].lower()
            testableCode = data[1][3]
            age = data[1][6]
            print(data[1][9])
        try:

            for x in range (5,26):
                relStatus = data[1][9]
                file = open('AllParticipantScoresRelStatus.csv','a')
                file.write(testableCode +','+ str(relStatus) + '\n')
        except IndexError:
            continue
        except IsADirectoryError:
            continue
