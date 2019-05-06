import json
import tkinter

import matplotlib
from numpy import save
from owlready import *
import pandas as pd
from scipy._lib.six import xrange
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle


# ----------------------Data loading------------------------------------------------------------------------------------
data = pd.read_csv('/Users/morteza/PycharmProjects/TestOnto/Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.csv')
dataFrame = pd.DataFrame(data)
# print(dataFrame)

dataUnclean = pd.read_csv('/Users/morteza/PycharmProjects/TestOnto/Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.csv')
dataFrameUnclean = pd.DataFrame(dataUnclean)
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------Ontology loading--------------------------------------------------------------------------------
onto = get_ontology("file:///Users/morteza/PycharmProjects/TestOnto/Olympic.owl").load()
# print(onto)
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------Ontology processing-----------------------------------------------------------------------------
# class Medal(Thing):
#     ontology = onto
#
# class Person(Thing):
#     ontology = onto
#
# class Country(Thing):
#     ontology = onto
#
# class Olympic(Thing):
#     ontology = onto
#
# class sport(Thing):
#     ontology = onto
class Discipline(Property):
    domain = [onto.Sport]
    range = [str]
class Event(Property):
    domain = [onto.Sport]
    range = [str]
class Event_Gender(Property):
    domain = [onto.Sport]
    range = [str]
class Has(Property):
    domain = [onto.Country]
    range = [onto.Person]
    inverse_property = onto.Blongs_To

# class Axiom(Thing):
#     ontology = onto
#     def genderCheck(self, tuple):
#         for i in range(0, len(tuple)):
#             if tuple.iloc[i]['Gender'] == 'Men' and tuple.iloc[i]['Event_gender'] == 'M':
#                 return 'Yes'
#             if tuple.iloc[i]['Gender'] == 'Women' and tuple.iloc[i]['Event_gender'] == 'M':
#                 return 'Yes'
#         return 'No'
#
#     def majorCheck(self, tuple, sport):
#         if sport == 'Wrestling':
#             Gre_RFlag = False
#             freeFlag = False
#             for i in range(0, len(tuple)):
#                 if tuple.iloc[i]['Sport'] == 'Wrestling':
#                     if tuple.iloc[i]['Discipline'] == 'Wrestling Gre-R':
#                         Gre_RFlag = True
#                     elif tuple.iloc[i]['Discipline'] == 'Wrestling Free.':
#                         freeFlag = True
#             if (Gre_RFlag == True) and (freeFlag == True):
#                 return 'Yes'
#             return 'No'
#         if sport == 'Equestrian':
#             Gre_RFlag = False
#             freeFlag = False
#             for i in range(0, len(tuple)):
#                 if tuple.iloc[i]['Sport'] == 'Equestrian':
#                     if tuple.iloc[i]['Discipline'] == 'Dressage':
#                         Gre_RFlag = True
#                     elif tuple.iloc[i]['Discipline'] == 'Eventing':
#                         freeFlag = True
#             if (Gre_RFlag == True) and (freeFlag == True):
#                 return 'Yes'
#             return 'No'
#
#         if sport == 'Cycling':
#             Gre_RFlag = False
#             freeFlag = False
#             for i in range(0, len(tuple)):
#                 if tuple.iloc[i]['Sport'] == 'Cycling':
#                     if tuple.iloc[i]['Discipline'] == 'Cycling Road':
#                         Gre_RFlag = True
#                     elif tuple.iloc[i]['Discipline'] == 'Cycling Track':
#                         freeFlag = True
#             if (Gre_RFlag == True) and (freeFlag == True):
#                 return 'Yes'
#             return 'No'
#         if sport == 'Aquatics':
#             SwFlag = False
#             DiFlag = False
#             WPFlag = False
#             for i in range(0, len(tuple)):
#                 if tuple.iloc[i]['Sport'] == 'Aquatics':
#                     if tuple.iloc[i]['Discipline'] == 'Swimming':
#                         SwFlag = True
#                     elif tuple.iloc[i]['Discipline'] == 'Diving':
#                         DiFlag = True
#                     elif tuple.iloc[i]['Discipline'] == 'Water polo':
#                         WPFlag = True
#             if (SwFlag == True) and (DiFlag == True):
#                 return 'Yes'
#             if (SwFlag == True) and (WPFlag == True):
#                 return 'Yes'
#             if (WPFlag == True) and (DiFlag == True):
#                 return 'Yes'
#             return 'No'
#
#     def monalityCheck(self, tuple):
#         name  = tuple.Athlete.unique()
#         date = tuple.Edition.unique()
#         if len(name) == 1 and len(date) == 1:
#             counter = 0
#             for i in range(0, len(tuple)):
#                 if tuple.iloc[i]['Athlete'] == name and tuple.iloc[i]['Edition'] == date:
#                     counter = counter + 1
#             if counter == 1:
#                 return 'Yes'
#         return 'No'
#
#     def genderModify(self, dFrame, Person):
#
#         personTuple = dataFrame[dataFrame['Athlete'] == Person]
#         mF = personTuple.loc[:, 'Gender'].value_counts().argmax()
#         for i in range(0, len(dFrame)):
#             if dFrame.iloc[i]['Athlete'] == Person:
#                 dFrame.iloc[i]['Gender'] = mF
#         return dFrame
#
#     def majorModify(self, dFrame, Person):
#
#         personTuple = dataFrame[dataFrame['Athlete'] == Person]
#         mF = personTuple.loc[:, 'Discipline'].value_counts().argmax()
#         for i in range(0, len(dFrame)):
#             if dFrame.iloc[i]['Athlete'] == Person:
#                 dFrame.iloc[i]['Discipline'] = mF
#         return dFrame
#     def monalityModify(self, dFrame, Person):
#         testDF = dFrame[dFrame['Athlete'] == Person]
#         if dFrame.empty == 'False' and testDF.empty == 'False':
#             if dFrame[dFrame['Athlete'] == Person].Sport.value_counts().argmax() == 'Football' :
#                 row = dFrame[dFrame['Athlete'] == Person]
#                 row = row.iloc[0]
#                 d1 = dFrame[dFrame['City'] == row['City']]
#                 d1 = d1[d1['Edition'] == row['Edition']]
#                 d1 = d1[d1['Sport'] == row['Sport']]
#                 d1 = d1[d1['Discipline'] == row['Discipline']]
#                 d1 = d1[d1['NOC'] == row['NOC']]
#                 d1 = d1[d1['Gender'] == row['Gender']]
#                 d1 = d1[d1['Event'] == row['Event']]
#                 d1 = d1[d1['Event_gender'] == row['Event_gender']]
#                 if len(d1.Edition.unique()) == 1:
#                     dFrame = dFrame[dFrame['Athlete'] != Person]
#                 # dFrame = dFrame.reset_index()
#                 d = {'City':[d1.City.value_counts().argmax()], 'Edition': [d1.Edition.value_counts().argmax()],
#                 'Sport': [d1.Sport.value_counts().argmax()], 'Discipline': [d1.Discipline.value_counts().argmax()],
#                 'Athlete': [Person], 'NOC': [d1.NOC.value_counts().argmax()], 'Gender':[d1.Gender.value_counts().argmax()],
#                 'Event': [d1.Event.value_counts().argmax()], 'Event_gender': [ d1.Event_gender.value_counts().argmax()],
#                 'Medal': [d1.Medal.value_counts().argmax()]}
#                 dForAdd = pd.DataFrame(data= d)
#                 dFrame = dFrame.append(dForAdd, ignore_index= True)
#         return dFrame
#     def cleanDup(self, dFrame):
#         dFrame = dFrame.drop_duplicates(keep= 'first')
#         return dFrame
# ////////////////////////////////////test Axiom///////////////////////////////////////////////////////////////////////
# testAxiom = onto.Axiom()
# testAxiom.genderCheck(dataFrame[dataFrame['Athlete'] == 'HAJOS, Alfred'])
# print(testAxiom.monalityCheck(dataFrame[dataFrame['Athlete']=='TOM, Logan']))
# testAxiom.monalityModify(dataFrame, 'TOM, Logan')
# print(testAxiom.majorCheck(dataFrame[dataFrame['Athlete'] == 'PALUSALU, Kristjan'], 'Wrestling'))
# cleaneeed = dataFrame.copy()
# cleaner = onto.Axiom()
# athletes = dataFrame.Athlete.unique()
# for p in athletes:
#     print(p)
#     if cleaner.genderCheck(cleaneeed[cleaneeed['Athlete'] == p]) == 'Yes':
#         cleaneeed = cleaner.genderModify(cleaneeed, p)
#     for e in ['Wrestling', 'Equestrian', 'Cycling', 'Aquatics']:
#         if cleaner.majorCheck(cleaneeed[cleaneeed['Athlete'] == p], e) == 'Yes':
#             cleaneeed = cleaner.majorModify(cleaneeed, p)
#     if cleaner.monalityCheck(cleaneeed[cleaneeed['Athlete']== p]) == 'No':
#             cleaneeed = cleaner.monalityModify(cleaneeed, p)
# print(cleaneeed)
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------Adding data to ontology-------------------------------------------------------------------------
# athleteSamples = []
# uniqueAthlete = dataFrame.Athlete.unique()
# for i in range(len(uniqueAthlete)):
#     athleteSamples.append(onto.Person(uniqueAthlete[i]))
#
# countrySamples = []
# uniqueCountry = dataFrame.NOC.unique()
# for i in range(len(uniqueCountry)):
#     countrySamples.append(onto.Country(uniqueCountry[i]))
#
# sportSamples = []
# uniqueSport = dataFrame.Sport.unique()
# for i in range(len(uniqueSport)):
#     sportSamples.append(onto.Sport(uniqueSport[i]))
#
# medalSamples = []
# medalSamples.append(onto.Medal('Gold'))
# medalSamples.append(onto.Medal('Silver'))
# medalSamples.append(onto.Medal('Bronze'))
#
#
# rawOlympicNames = []
# for i in range(len(dataFrame['City'])):
#     tem = str(dataFrame['City'][i]) + str(dataFrame['Edition'][i])
#     rawOlympicNames.append(tem)
# olympicSample = []
# uniqueOlympic = list(set(rawOlympicNames))
# for i in range(len(uniqueOlympic)):
#     olympicSample.append(onto.Olympic(uniqueOlympic[i]))

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------Data Pre-processing-----------------------------------------------------------------------------
# ////////////////////////////////////separate data for clustering//////////////////////////////////////////////////////
# X = dataFrame.iloc[0:20000][:]
# Y = dataFrame.iloc[20000:29215][:]

# XExternalUncleanData = dataFrameUnclean.iloc[0:20000][:]
# YExternalUncleanData = dataFrameUnclean.iloc[20000:29215][:]
# ////////////////////////////////////convert label data to numeric format for testing//////////////////////////////////
# YLabel = Y.copy()
# for clm in YLabel.columns:
#     if type(YLabel[clm]) is not(np.int64 or np.float):
#         YLabel[clm] = LabelEncoder().fit_transform(YLabel[clm])

# ////////////////////////////////////convert clean data to numeric format//////////////////////////////////////////////
# numericDataFrame = X.copy()
# for clm in numericDataFrame.columns:
#     if type(numericDataFrame[clm]) is not(np.int64 or np.float):
#         numericDataFrame[clm] = LabelEncoder().fit_transform(numericDataFrame[clm])
# numericDataFrame = shuffle(numericDataFrame)
# XC = numericDataFrame

# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
# numericDataFrame.to_csv("numericDataFrame.csv")

# ////////////////////////////////////generating unclean data///////////////////////////////////////////////////////////
# uncleanData = dataFrameUnclean.copy()
# uncleanData = uncleanData.sort_index()
# c = 1
# uncleanData = shuffle(uncleanData)
# print(uncleanData)
# for i in range(0, len(uncleanData) - 10):
#     print(c)
#     c = c + 1
#     newRow1Se = uncleanData.loc[i][:]
#     newRow1DF = uncleanData.loc[i][:].to_frame()
#     newRow2Se = uncleanData.loc[i + 1][:]
#     newRow2DF = uncleanData.loc[i + 1][:].to_frame()
#     newRow3Se = uncleanData.loc[i + 2][:]
#     newRow3DF = uncleanData.loc[i + 2][:].to_frame()
#     newRow4Se = uncleanData.loc[i + 3][:]
#     newRow4DF = uncleanData.loc[i + 3][:].to_frame()
#     newRow5Se = uncleanData.loc[i + 4][:]
#     newRow5DF = uncleanData.loc[i + 4][:].to_frame()
#     newRow6Se = uncleanData.loc[i + 5][:]
#     newRow6DF = uncleanData.loc[i + 5][:].to_frame()
#     newRow7Se = uncleanData.loc[i + 6][:]
#     newRow7DF = uncleanData.loc[i + 6][:].to_frame()
#     newRow8Se = uncleanData.loc[i + 7][:]
#     newRow8DF = uncleanData.loc[i + 7][:].to_frame()
#     newRow9Se = uncleanData.loc[i + 8][:]
#     newRow9DF = uncleanData.loc[i + 8][:].to_frame()
#     newRow10Se = uncleanData.loc[i + 9][:]
#     newRow10DF = uncleanData.loc[i + 9][:].to_frame()
#     newRow11Se = uncleanData.loc[i + 10][:]
#     newRow11DF = uncleanData.loc[i + 10][:].to_frame()
#     tempDF = pd.concat([newRow1DF, newRow2DF, newRow3DF, newRow4DF, newRow5DF, newRow6DF, newRow7DF,
#                         newRow8DF, newRow9DF, newRow10DF, newRow11DF])
#     if c % 13 == 0:
#         uncleanData.loc[-1] = newRow1Se
        # uncleanData.loc[-1] = newRow1Se
        # uncleanData.loc[-1] = newRow1Se
        # uncleanData.loc[-1] = newRow1Se
        # uncleanData.loc[-1] = newRow1Se
        # uncleanData.loc[-1] = newRow1Se
        # uncleanData.loc[-1] = newRow1Se
        # uncleanData.index = uncleanData.index + 1
    # for i in newRow1DF.columns:
    #     newRow11DF[i] = tempDF.loc[:, i].value_counts().argmax()
    # if c % 59 == 0:
    #     uncleanData.loc[-1] = newRow11Se
    #     uncleanData.loc[-1] = newRow11Se
        # uncleanData.loc[-1] = newRow11Se
        # uncleanData.loc[-1] = newRow11Se
        # uncleanData.loc[-1] = newRow11Se
        # uncleanData.loc[-1] = newRow11Se
        # uncleanData.loc[-1] = newRow11Se
        # uncleanData.index = uncleanData.index + 1
    # uncleanData = uncleanData.sort_index()
# print(uncleanData)

# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
# uncleanData.to_csv("uncleanData.csv")

# ////////////////////////////////////make clean data from unclean//////////////////////////////////////////////////////
# cleaneeed = uncleanData.copy()
# cleaner = onto.Axiom()
# athletes = dataFrame.Athlete.unique()
# for p in cleaneeed:
#     if cleaner.monalityCheck(cleaneeed[cleaneeed['Athlete']== p]) == 'No':
#         cleaneeed = cleaner.monalityModify(cleaneeed, p)
#     if cleaner.genderCheck(cleaneeed[cleaneeed['Athlete'] == p]) == 'Yes':
#         cleaneeed = cleaner.genderModify(cleaneeed, p)
#     for e in ['Wrestling', 'Equestrian', 'Cycling', 'Aquatics']:
#         if cleaner.majorCheck(cleaneeed[cleaneeed['Athlete'] == p], e) == 'Yes':
#             cleaneeed = cleaner.majorModify(cleaneeed, p)
#     # print(cleaneeed.empty)

# cleaneeed = cleaner.cleanDup(cleaneeed)
# print(cleaneeed)
# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
# cleaneeed.to_csv("cleaneeed.csv")
#
# ////////////////////////////////////convert unclean data to numeric format////////////////////////////////////////////
# numericDataFrameUnclean = uncleanData.copy()
# for clm in numericDataFrameUnclean.columns:
#     if type(numericDataFrameUnclean[clm]) is not(np.int64 or np.float):
#         numericDataFrameUnclean[clm] = LabelEncoder().fit_transform(numericDataFrameUnclean[clm])
# XUnC = numericDataFrameUnclean

# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
#
# numericDataFrameUnclean.to_csv("numericDataFrameUnclean.csv")
#
# ////////////////////////////////////convert again cleaned data to numeric format//////////////////////////////////////
# numericDataFramecleanAgain = cleaneeed.copy()
# for clm in numericDataFramecleanAgain.columns:
#     if type(numericDataFramecleanAgain[clm]) is not(np.int64 or np.float):
#         numericDataFramecleanAgain[clm] = LabelEncoder().fit_transform(numericDataFramecleanAgain[clm])
# XCAgain = numericDataFramecleanAgain

# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
# numericDataFramecleanAgain.to_csv("numericDataFramecleanAgain.csv")
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------Clustering--------------------------------------------------------------------------------------
# def rmse(predictions, targets):
#     return np.sqrt(((predictions - targets) ** 2).mean())
# def similarElement(list1, list2):
#     counter = 0
#     for i in list1:
#         for j in  list2:
#             if i == j:
#                 counter = counter + 1
#     return counter
# print(len(YLabel))
# print(len(XUnC))
# print(len(XCAgain))
# ////////////////////////////////////K_Means cluster model/////////////////////////////////////////////////////////////
# kmeans = KMeans(n_clusters= 201)
# kmeans.fit(XC)
#
#
# kmeansUnC = KMeans(n_clusters= 201)
# kmeansUnC.fit(XUnC)
#
#
# kmeansCAgain = KMeans(n_clusters= 201)
# kmeansCAgain.fit(XCAgain)


# for i,j,k in zip(kmeans.predict(YLabel), kmeansUnC.predict(YLabel), kmeansCAgain.predict(YLabel)):
#     print("%s\t%s\t%s" % (i, j, k))
#
# rmse_val_cleanAndUnclean = []
# rmse_val_cleanAndUnclean.append(rmse(np.array(kmeans.predict(YLabel)), np.array(kmeansUnC.predict(YLabel))))
# print("rms error for unclean data is: " + str(rmse_val_cleanAndUnclean))
#
# rmse_val2_cleanAndAgainClean = []
# rmse_val2_cleanAndAgainClean.append(rmse(np.array(kmeans.predict(YLabel)), np.array(kmeansCAgain.predict(YLabel))))
# print("rms error for cleaned data is: " + str(rmse_val2_cleanAndAgainClean))
#
# print(adjusted_rand_score(kmeans.predict(YLabel), kmeansUnC.predict(YLabel)))
# print(adjusted_rand_score(kmeans.predict(YLabel), kmeansCAgain.predict(YLabel)))
#
# print('///////////////')
#
# print(similarElement(kmeans.predict(YLabel), kmeansUnC.predict(YLabel)))
# print(similarElement(kmeans.predict(YLabel), kmeansCAgain.predict(YLabel)))
# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
# pdCandUNC = pd.DataFrame(rmse_val_cleanAndUnclean)
# pdCandUNC.to_csv("rmse_val_cleanAndUnclean.csv")
#
# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
# pdCandAC = pd.DataFrame(rmse_val2_cleanAndAgainClean)
# pdCandAC.to_csv("rmse_val2_cleanAndAgainClean.csv")

# ////////////////////////////////////K_Means classified model//////////////////////////////////////////////////////////
# trainClean = XC.drop(["Medal"], axis = 1)
# labelClean = XC["Medal"]
# SVMClean = svm.SVC(gamma='scale')
# SVMClean.fit(np.array(trainClean), np.array(labelClean))
#
# trainUnclean = XUnC.drop(["Medal"], axis = 1)
# labelUnclean = XUnC["Medal"]
# SVMUnclean = svm.SVC(gamma='scale')
# SVMUnclean.fit(np.array(trainUnclean), np.array(labelUnclean))
#
# trainAgainclean = XCAgain.drop(["Medal"], axis = 1)
# labelAgainclean = XCAgain["Medal"].ravel()
# SVMAgainclean = svm.SVC(gamma='scale')
# SVMAgainclean.fit(np.array(trainAgainclean), np.array(labelAgainclean))

# for i,j,k in zip(SVMClean.predict(np.array(YLabel.drop(["Medal"], axis = 1))),
#                  SVMUnclean.predict(np.array(YLabel.drop(["Medal"], axis = 1))),
#                  SVMAgainclean.predict(np.array(YLabel.drop(["Medal"], axis = 1)))):
#     print("%s\t%s\t%s" % (i, j, k))


# rmse_val_cleanAndUnclean = []
# rmse_val_cleanAndUnclean.append(rmse(SVMClean.predict(np.array(YLabel.drop(["Medal"], axis = 1))),
#                                      SVMUnclean.predict(np.array(YLabel.drop(["Medal"], axis=1)))))
# print("rms error for unclean data is: " + str(rmse_val_cleanAndUnclean))
#
# rmse_val2_cleanAndAgainClean = []
# rmse_val2_cleanAndAgainClean.append(rmse(SVMClean.predict(np.array(YLabel.drop(["Medal"], axis = 1))),
#                                          SVMAgainclean.predict(np.array(YLabel.drop(["Medal"], axis=1)))))
# print("rms error for cleaned data is: " + str(rmse_val2_cleanAndAgainClean))
# ////////////////////////////////////Plot raw data/////////////////////////////////////////////////////////////////////
# plt.scatter(numericDataFrame[:,0],numericDataFrame[:,1], label='True Position')
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------split data sets---------------------------------------------------------------------------------
bronzeData = dataFrame.copy()
bronzeData.columns = ['Holding Place','Year','Sport','Discipline','Athlete','NOC',
                      'Gender','Event','Event_gender','Medal']
silverData = dataFrame.copy()
silverData.columns = ['Holding City','Date','Sport','Major','Participant','Country',
                      'Gender','Event','Event_G','Medal']
goldData = dataFrame.copy()
goldData.columns = ['City','Edition','Sport','Discipline','Participant',
                    'Nation','Sex','Event','Event_gender','Medal']

bronzeData = bronzeData[bronzeData.Medal != 'Silver']
bronzeData = bronzeData[bronzeData.Medal != 'Gold']
# print(bronzeData)

# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
bronzeData.to_csv("bronzeData.csv")

silverData = silverData[silverData.Medal != 'Bronze']
silverData = silverData[silverData.Medal != 'Gold']
# print(silverData)

# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
silverData.to_csv("silverData.csv")

goldData = goldData[goldData.Medal != 'Silver']
goldData = goldData[goldData.Medal != 'Bronze']
# print(bronzeData)

# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
goldData.to_csv("goldData.csv")
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------add instances to ontology-----------------------------------------------------------------------
synCountry= []
country = onto.Country('Country', CName=['Country'])
NOC = onto.Country('NOC', CName= ['NOC'])
nation = onto.Country('Nation', CName= ['Nation'])
synCountry.append(country)
synCountry.append(NOC)
synCountry.append(nation)

synSport = []
sport1 = onto.Sport('Sport', SName= ['Sport'])
sport2 = onto.Sport('Sport', SName= ['Sport'])
sport3 = onto.Sport('Sport', SName= ['Sport'])
synCountry.append(sport1)
synSport.append(sport2)
synSport.append(sport3)

synOlympic = []
holding_Place = onto.Olympic('Holding Place', OName= ['Holding Place'], OYear= ['Year'])
holding_City = onto.Olympic('Holding City', OName= ['Holding City'], OYear= ['Date'])
city = onto.Olympic('City', OName= ['City'], OYear= ['Edition'])
synOlympic.append(holding_Place)
synOlympic.append(holding_City)
synOlympic.append(city)

synPerson = []
athlete = onto.Person('Athlete', PersonName= ['Athlete'])
participant = onto.Person('Participant', PersonName= ['Participant'])
synPerson.append(athlete)
synPerson.append(participant)


synMedal = []
medal = onto.Medal('Medal', MName=['Medal'])
synMedal.append(medal)

sport1.Discipline.append('Discipline')
sport1.Event.append('Event')
sport1.Event_Gender.append('Event_gender')

sport2.Discipline.append('Major')
sport2.Event.append('Event')
sport2.Event_Gender.append('Event_G')

sport3.Discipline.append('Major')
sport3.Event.append('Event')
sport3.Event_Gender.append('Event_gender')

athlete.Sex.append('Gender')
participant.Sex.append('Gender')
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------query on different data sets--------------------------------------------------------------------

queryForSearch = 'Aquatics'
type = ''
if(type == 'Person'):
    for person in onto.Person.instances():
        for clm in bronzeData.columns:
            if clm == person.PersonName[0]:
                q1 = bronzeData.loc[bronzeData[clm] == queryForSearch]
                if len(q1) != 0:
                    print(q1)

    for clm in silverData.columns:
        if clm == person.PersonName[0]:
            q2 = silverData.loc[silverData[clm] == queryForSearch]
            if len(q2) != 0:
                print(q2)

    for clm in goldData.columns:
        if clm == person.PersonName[0]:
            q3 = goldData.loc[goldData[clm] == queryForSearch]
            if len(q3) != 0:
                print(q3)

if(type == 'Country'):
    for country in onto.Country.instances():
        for clm in bronzeData.columns:
            if clm == country.CName[0]:
                q1 = bronzeData.loc[bronzeData[clm] == queryForSearch]
                if len(q1) != 0:
                    print(q1)

        for clm in silverData.columns:
            if clm == country.CName[0]:
                q2 = silverData.loc[silverData[clm] == queryForSearch]
                if len(q2) != 0:
                    print(q2)

        for clm in goldData.columns:
            if clm == country.CName[0]:
                q3 = goldData.loc[goldData[clm] == queryForSearch]
                if len(q3) != 0:
                    print(q3)

if(type == 'Olympic'):
    for olympic in onto.Country.instances():
        for clm in bronzeData.columns:
            if clm == olympic.OName[0]:
                q1 = bronzeData.loc[bronzeData[clm] == queryForSearch]
                if len(q1) != 0:
                    print(q1)

        for clm in silverData.columns:
            if clm == olympic.OName[0]:
                q2 = silverData.loc[silverData[clm] == queryForSearch]
                if len(q2) != 0:
                    print(q2)

        for clm in goldData.columns:
            if clm == olympic.OName[0]:
                q3 = goldData.loc[goldData[clm] == queryForSearch]
                if len(q3) != 0:
                    print(q3)

if(type == 'Sport'):
    for sport in onto.Sport.instances():
        for clm in bronzeData.columns:
            if clm == sport.SName[0]:
                q1 = bronzeData.loc[bronzeData[clm] == queryForSearch]
                if len(q1) != 0:
                    print(q1)

        for clm in silverData.columns:
            if clm == sport.SName[0]:
                q2 = silverData.loc[silverData[clm] == queryForSearch]
                if len(q2) != 0:
                    print(q2)

        for clm in goldData.columns:
            if clm == sport.SName[0]:
                q3 = goldData.loc[goldData[clm] == queryForSearch]
                if len(q3) != 0:
                    print(q3)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------clustering based on specific feature------------------------------------------------------------
personsSamples = []
uniquePersons = dataFrame.Athlete.unique()
q4 = pd.DataFrame(columns=['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC',
                           'Gender', 'Event', 'Event_gender', 'Medal'])
cleanedData = pd.DataFrame(columns=['City', 'Edition', 'Sport', 'Discipline', 'Athlete',
                                    'NOC', 'Gender', 'Event', 'Event_gender', 'Medal'])
sportList = []
disciplineList = []
athleteList = []
NOCList = []
genderList = []
eventList = []
event_genderList = []
cityList =[]
editionList =[]
medalTypeList =[]
medalCountList = []
list =[]
for personForSearch in uniquePersons:
    print('Person for search is: ' + str(personForSearch))
    for person in onto.Person.instances():
            for clm in bronzeData.columns:
                if clm == person.PersonName[0]:
                    q1 = bronzeData.loc[bronzeData[clm] == personForSearch]
                    if len(q1) != 0:
                        q1.columns = ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender', 'Event',
                                  'Event_gender', 'Medal']
                        # q4 = pd.merge(q1, q1)
                        # print(q4)
                        for i in q1.Sport.unique(): sportList.append(i)
                        for i in q1.Discipline.unique(): disciplineList.append(i)
                        athleteList.append(personForSearch)
                        for i in q1.NOC.unique(): NOCList.append(i)
                        for i in q1.Gender.unique(): genderList.append(i)
                        for i in q1.Event.unique(): eventList.append(i)
                        for i in q1.Event_gender.unique(): event_genderList.append(i)
                        for i in q1.City.unique(): cityList.append(i)
                        for i in q1.Edition.unique(): editionList.append(i)
                        medalTypeList.append('Bronze')
                        medalCountList.append(len(q1))


            for clm in silverData.columns:
                if clm == person.PersonName[0]:
                    q2 = silverData.loc[silverData[clm] == personForSearch]
                    if len(q2) != 0:
                        q2.columns = ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender', 'Event',
                                  'Event_gender', 'Medal']
                        # q4 = pd.merge(q4, q2)
                        # print(q2)
                        for i in q2.Sport.unique(): sportList.append(i)
                        for i in q2.Discipline.unique(): disciplineList.append(i)
                        athleteList.append(personForSearch)
                        for i in q2.NOC.unique(): NOCList.append(i)
                        for i in q2.Gender.unique(): genderList.append(i)
                        for i in q2.Event.unique(): eventList.append(i)
                        for i in q2.Event_gender.unique(): event_genderList.append(i)
                        for i in q2.City.unique(): cityList.append(i)
                        for i in q2.Edition.unique(): editionList.append(i)
                        medalTypeList.append('Silver')
                        medalCountList.append(len(q2))

            for clm in goldData.columns:
                if clm == person.PersonName[0]:
                    q3 = goldData.loc[goldData[clm] == personForSearch]
                    if len(q3) != 0:
                        q3.columns = ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender', 'Event',
                                  'Event_gender', 'Medal']
                        # q4 = pd.merge(q4, q3)
                        # print(q3)
                        for i in q3.Sport.unique(): sportList.append(i)
                        for i in q3.Discipline.unique(): disciplineList.append(i)
                        athleteList.append(personForSearch)
                        for i in q3.NOC.unique(): NOCList.append(i)
                        for i in q3.Gender.unique(): genderList.append(i)
                        for i in q3.Event.unique(): eventList.append(i)
                        for i in q3.Event_gender.unique(): event_genderList.append(i)
                        for i in q3.City.unique(): cityList.append(i)
                        for i in q3.Edition.unique(): editionList.append(i)
                        medalTypeList.append('Gold')
                        medalCountList.append(len(q3))
            d = {'Athlete':personForSearch, 'Sport': sportList, 'Country': NOCList, 'Olympic': [cityList, editionList],
                 'Medal': [medalTypeList, medalCountList]}
    sportList = []
    disciplineList = []
    athleteList = []
    NOCList = []
    genderList = []
    eventList = []
    event_genderList = []
    cityList = []
    editionList = []
    medalTypeList = []
    medalCountList = []
    list.append(d)
    # print(d)

# ////////////////////////////////////save data/////////////////////////////////////////////////////////////////////////
DFofList = pd.DataFrame(list)
DFofList.to_csv("list.csv")
# ----------------------------------------------------------------------------------------------------------------------
window = tkinter.Tk()
window.title("Phase2 Notification")
tkinter.Label(window, text = "Phase2 completed! find the result in the app directory", fg = "Black").pack()
window.mainloop()