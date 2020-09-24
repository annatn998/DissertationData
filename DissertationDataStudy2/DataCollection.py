import csv
import writingFileTitles

def DissertationDataCleaning(collectedDataFiles):

    subjectNumberFile = open(collectedDataFiles,'r')
    a = subjectNumberFile.readlines()
    subjectGroup = a[1][1]

    def writingSubjectGroup(fileName):
        subjectNumberFile2 = open(fileName,'a')
        subjectNumberFile2.write(subjectGroup + ',')
    writingSubjectGroup('profile1.csv')
    writingSubjectGroup('profile2.csv')
    writingSubjectGroup('profile3.csv')
    writingSubjectGroup('profile4.csv')
    writingSubjectGroup('profile5.csv')
    writingSubjectGroup('profile6.csv')
    writingSubjectGroup('profile7.csv')
    writingSubjectGroup('profile8.csv')
    writingSubjectGroup('profile9.csv')
    writingSubjectGroup('profile10.csv')


    def writeNewLine(file):
        profile = open(file,'a') #make sure to put after each written profile
        profile.write('\n')


    def profileNumber(profile,str,response,CSV):
        if profile == str:
            profileNumber = open(CSV, 'a')
            profileNumber.write(response + ',')

    def writingOtherData(file):
        profile = open(file,'a')
        profile.write(gender + ',' + profileGender + ',' + relStatus + ',' + testableCode)

############################################################################
    with open(collectedDataFiles, newline='') as csvfile:
        temp_reader = csv.reader(csvfile, delimiter=',')
        data = list(temp_reader)
    try:
        relStatus = data[1][10].lower()
        gender = data[1][7].lower()
        profileGender = data[4][17].lower()
        testableCode = data[1][3]

    except IndexError:
        print('No data found')

    with open(collectedDataFiles) as csvfile:
        CSVReader = csv.reader(csvfile, delimiter=',')
        for row in CSVReader:
            try:
                profile = row[2]
                print(row[19])
                if row[19] != 'Male' and row[19] != 'Female' and row[19] != 'response':
                    for number in row[19].split(';'):
                        response = number
                        profileNumber(profile, 'F1', response, 'profile1.csv')
                        profileNumber(profile, 'F2', response, 'profile2.csv')
                        profileNumber(profile, 'F3', response, 'profile3.csv')
                        profileNumber(profile, 'F4', response, 'profile4.csv')
                        profileNumber(profile, 'F5', response, 'profile5.csv')
                        profileNumber(profile, 'F6', response, 'profile6.csv')
                        profileNumber(profile, 'F7', response, 'profile7.csv')
                        profileNumber(profile, 'F8', response, 'profile8.csv')
                        profileNumber(profile, 'F9', response, 'profile9.csv')
                        profileNumber(profile, 'F10', response, 'profile10.csv')
                        profileNumber(profile, 'M1', response, 'profile1.csv')
                        profileNumber(profile, 'M2', response, 'profile2.csv')
                        profileNumber(profile, 'M3', response, 'profile3.csv')
                        profileNumber(profile, 'M4', response, 'profile4.csv')
                        profileNumber(profile, 'M5', response, 'profile5.csv')
                        profileNumber(profile, 'M6', response, 'profile6.csv')
                        profileNumber(profile, 'M7', response, 'profile7.csv')
                        profileNumber(profile, 'M8', response, 'profile8.csv')
                        profileNumber(profile, 'M9', response, 'profile9.csv')
                        profileNumber(profile, 'M10', response, 'profile10.csv')

            except IndexError:
                continue
###############################################################
    writingOtherData('profile1.csv')
    writingOtherData('profile2.csv')
    writingOtherData('profile3.csv')
    writingOtherData('profile4.csv')
    writingOtherData('profile5.csv')
    writingOtherData('profile6.csv')
    writingOtherData('profile7.csv')
    writingOtherData('profile8.csv')
    writingOtherData('profile9.csv')
    writingOtherData('profile10.csv')



##############################################################
    writeNewLine('profile1.csv')
    writeNewLine('profile2.csv')
    writeNewLine('profile3.csv')
    writeNewLine('profile4.csv')
    writeNewLine('profile5.csv')
    writeNewLine('profile6.csv')
    writeNewLine('profile7.csv')
    writeNewLine('profile8.csv')
    writeNewLine('profile9.csv')
    writeNewLine('profile10.csv')
#####################################################