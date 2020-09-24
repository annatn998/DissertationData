import csv
from os import listdir
import sys
dataFiles = listdir('.')




averageAttractive = {}
averageWarm = {}
averageTrust = {}
averageDominant = {}
averageKind = {}
averageUnfaithful = {}
averageDatable = {}


for files in dataFiles:
    if '342405' in files:
        with open(files, newline='') as csvfile:
            temp_reader = csv.reader(csvfile, delimiter=',')
            data = list(temp_reader)
            attractiveRating = 0
            warmRating = 0
            trustworthyRating = 0
            dominantRating = 0
            kindRating = 0
            unfaithfulRating = 0
            datableRating = 0
            subjectGroup = int(data[1][0])
            profileGender = data[4][19].lower()
            relStatus = data[1][11].lower()
            gender = data[1][7].lower()
            profileGender = data[4][19].lower()
            for number in range(5,25):
                responseRow = data[number][19].split(';')
                F1andM1 = data[number][2].replace('','')
                if len(responseRow) < 2:
                    dateable = int(responseRow[0])
                    datableRating = datableRating + dateable
                    datableTotal = datableRating/10
                    averageDatable[data[1][3]] = [datableTotal,subjectGroup]
                elif len(responseRow) > 2:
                    attractive = int(responseRow[0])
                    attractiveRating = attractiveRating + attractive
                    attractiveTotal = attractiveRating/10
                    averageAttractive[data[1][3]] = [attractiveTotal,subjectGroup]
                    warm = int(responseRow[1])
                    warmRating = warmRating + warm
                    warmTotal = warmRating/10
                    averageWarm[data[1][3]] = [warmTotal,subjectGroup]
                    trustworthy = int(responseRow[2])
                    trustworthyRating = trustworthyRating + trustworthy
                    trustworthyTotal = trustworthyRating/10
                    averageTrust[data[1][3]] = [trustworthyTotal,subjectGroup]
                    dominant = int(responseRow[3])
                    dominantRating = dominantRating + dominant
                    dominantTotal = dominantRating/10
                    averageDominant[data[1][3]] = [dominantTotal,subjectGroup]
                    kind = int(responseRow[4])
                    kindRating = kindRating + kind
                    kindTotal = kindRating/10
                    averageKind[data[1][3]] = [kindTotal,subjectGroup]
                    possiblyUnfaithful = int(responseRow[5])
                    unfaithfulRating = unfaithfulRating + possiblyUnfaithful
                    unfaithfulTotal = unfaithfulRating/10
                    averageUnfaithful[data[1][3]] = [unfaithfulTotal,subjectGroup]


print(averageAttractive)
file = open('averageResponseTrustworthy.csv','w')
file.write(" TestableCode,Average,SubjectGroup + \n ")
columns = 'Particpant, Dimension'
csv_file = "AverageResponsesPerDimension.csv"
try:
    with open(csv_file, 'w') as csvfile:
        for data in averageDatable.keys():
            csvfile.write('Dateable,')
            csvfile.write("%s,%s\n"%(data,averageDatable[data]))
        for data in averageAttractive.keys():
            csvfile.write('Attractive,')
            csvfile.write("%s,%s\n"%(data,averageAttractive[data]))
        for data in averageDominant.keys():
            csvfile.write('Dominant,')
            csvfile.write("%s,%s\n" % (data, averageDominant[data]))
        for data in averageWarm.keys():
            csvfile.write('Warm,')
            csvfile.write("%s,%s\n" % (data, averageWarm[data]))
        for data in averageKind.keys():
            csvfile.write('Kind,')
            csvfile.write("%s,%s\n" % (data, averageKind[data]))
        for data in averageUnfaithful.keys():
            csvfile.write('Unfaithful,')
            csvfile.write("%s,%s\n" % (data, averageUnfaithful[data]))
        for data in averageTrust.keys():
            csvfile.write('Trust,')
            csvfile.write("%s,%s\n" % (data, averageTrust[data]))



except IOError:
    print("I/O error")
