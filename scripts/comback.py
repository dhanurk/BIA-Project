import json
import time
			
json_data=open("full_dataset.json").read()
data=json.loads(json_data)
objectList = data['allmatches'] #one object = one season
comeback = 0
win = 0

teamList = set()
for i in range (0,len(objectList)):
	for key in objectList[i]['matches'].keys():
		homeTeam = objectList[i]['matches'][key]['score']['home']
		awayTeam = objectList[i]['matches'][key]['score']['away']
		teamList.add(homeTeam)
		teamList.add(awayTeam)
for team in teamList:
        comeback = 0
        win = 0
        for i in range(0,len(objectList)):
                comeback = 0
                win = 0
	        for key in objectList[i]['matches'].keys():
                        homeScoreTime = [999] * 10
                        awayScoreTime = [999] * 10
                        homeScoreCount = 0
                        awayScoreCount = 0
                        indexH = 0
                        indexA = 0
		        homeTeam = objectList[i]['matches'][key]['score']['home']
		        awayTeam = objectList[i]['matches'][key]['score']['away']
		        homeScore = int(objectList[i]['matches'][key]['score']['homeScore'])
		        awayScore = int(objectList[i]['matches'][key]['score']['awayScore'])
		        date = objectList[i]['matches'][key]['general']['date']
		        if(homeTeam == team):
                                if homeScore < awayScore:
                                        continue
                                win = win + 1
                                if awayScore == 0:
                                        continue
                                for keys in objectList[i]['matches'][key]['goalHome'].keys():
                                        homeScoreTime[indexH] = int(objectList[i]['matches'][key]['goalHome'][keys]['time'])
                                        indexH = indexH + 1
                                        if(indexH >= homeScore):
                                                break
                                for keys in objectList[i]['matches'][key]['goalAway'].keys():
                                        awayScoreTime[indexA] = int(objectList[i]['matches'][key]['goalAway'][keys]['time'])
                                        indexA = indexA + 1
                                        if(indexA >= awayScore):
                                                break
                                j = 0
                                homeScoreTime.sort()
                                awayScoreTime.sort()
                                while j < indexA:
                                        hTime = homeScoreTime[j]
                                        aTime = awayScoreTime[j]
                                        j = j + 1
                                        if aTime < hTime:
                                                comeback = comeback + 1
                                                break
		        elif(awayTeam == team):
                                if awayScore < homeScore:
                                        continue
                                win = win + 1
                                if homeScore == 0:
                                        continue
                                for keys in objectList[i]['matches'][key]['goalHome'].keys():
                                        homeScoreTime[indexH] = int(objectList[i]['matches'][key]['goalHome'][keys]['time'])
                                        indexH = indexH + 1
                                        if(indexH >= homeScore):
                                                break
                                for keys in objectList[i]['matches'][key]['goalAway'].keys():
                                        awayScoreTime[indexA] = int(objectList[i]['matches'][key]['goalAway'][keys]['time'])
                                        indexA = indexA + 1
                                        if(indexA >= awayScore):
                                                break;
                                j = 0
                                homeScoreTime.sort()
                                awayScoreTime.sort()
                                while j < indexH:
                                        hTime = homeScoreTime[j]
                                        aTime = awayScoreTime[j]
                                        j = j + 1
                                        if hTime < aTime:
                                                comeback = comeback + 1
                                                break
                print "insert into comebacks (season, team, wins, comebacks) values ( '" + str(i) + "', '" + str(team) + "', '" + str(win) + "', '" + str(comeback) + "');"
#homefactor,awayfactor,opponent team id,homefactor,awayfactor
# 24 12 6
# 27 11 4
# 26 10 6
# 25 7 6
#




