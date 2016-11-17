import json
import time


def getPastMatchesResults(objectList,team,idDict,dateb4,homeOrAway):
	result={}
	result['homewin']=result['awaywin']=result['homematches']=result['awaymatches']=result['wld']=0
	for i in range(0,len(objectList)-1):
		for key in objectList[i]['matches'].keys():
			homeTeam = objectList[i]['matches'][key]['score']['home']
			awayTeam = objectList[i]['matches'][key]['score']['away']
			date = time.strptime(objectList[i]['matches'][key]['general']['date'], "%d %b %Y")
			if(((homeOrAway == 'home' and homeTeam == team) or (homeOrAway == 'away' and awayTeam == team))  and date<=dateb4):
  				homeScore = objectList[i]['matches'][key]['score']['homeScore']
				awayScore = objectList[i]['matches'][key]['score']['awayScore']
				if(homeTeam==team and homeOrAway == 'home'):
						result['homematches']+=1  
						if(homeScore>awayScore):
							result['homewin']+=1 
				elif (awayTeam==team and homeOrAway == 'away'):
						result['awaymatches']+=1  
						if(awayScore>homeScore):
							result['awaywin']+=1 
	return result 
									
def generateIds(objectList):
	idno=0
	idDict={}
	for i in range(0,len(objectList)-1):
		for key in objectList[i]['matches'].keys():
			objMatch = objectList[i]['matches'][key]
			homeTeam=objMatch['score']['home']
			team=idDict.get(homeTeam,'invalid')   #see if it exists already in dictionary
			if(team == 'invalid'):
				idDict[homeTeam]=idno
				idno+=1
			awayTeam=objMatch['score']['away']
			team=idDict.get(awayTeam,'invalid')
			if(team == 'invalid'):
				idDict[awayTeam]=idno
				idno+=1
				
	idDictNew={}
	for key, value in idDict.iteritems():
		string=""
		for i in range(0,len(idDict)):						
			string+="0,"
		string = string[:2*value] + '1' + string[2*value + 1:]
		idDictNew[key]=string
		
	return idDictNew


print "Enter team name\n"
input_team = raw_input()			
json_data=open("full_dataset.json").read()
data=json.loads(json_data)
objectList = data['allmatches'] #one object = one season
idDict=generateIds(objectList)
result_input_team={}
result_other_team={}
for i in range(0,len(objectList)-1):
		for key in objectList[i]['matches'].keys():
			homeTeam = objectList[i]['matches'][key]['score']['home']
			awayTeam = objectList[i]['matches'][key]['score']['away']
			homeScore = objectList[i]['matches'][key]['score']['homeScore']
			awayScore = objectList[i]['matches'][key]['score']['awayScore']
			date = time.strptime(objectList[i]['matches'][key]['general']['date'], "%d %b %Y")
			if(homeTeam == input_team):
				result_input_team=getPastMatchesResults(objectList,input_team,idDict,date,'home') #consider only home matches
				result_other_team=getPastMatchesResults(objectList,awayTeam,idDict,date,'away') 
				homeFactor=0.0
				awayFactor=0.0				
				if(result_input_team['homematches']!=0):
					homeFactor = float(result_input_team['homewin'])/result_input_team['homematches']
				if(result_other_team['awaymatches']!=0):
					awayFactor = float(result_other_team['awaywin'])/result_other_team['awaymatches']
				if(homeScore>awayScore):	
					result_input_team['wld']=1
				elif(awayScore>homeScore):
					result_input_team['wld']=2
				else:
					result_input_team['wld']=3
				print "{0},0,{1}0,{2},{3}".format(homeFactor,idDict[awayTeam],awayFactor,result_input_team['wld'])
			elif(awayTeam == input_team):
				result_input_team=getPastMatchesResults(objectList,input_team,idDict,date,'away') 
				result_other_team=getPastMatchesResults(objectList,homeTeam,idDict,date,'home')
				homeFactor=0.0
				awayFactor=0.0
				if(result_other_team['homematches']!=0):
					homeFactor = float(result_other_team['homewin'])/result_other_team['homematches']
				if(result_input_team['awaymatches']!=0):
					awayFactor = float(result_input_team['awaywin'])/result_input_team['awaymatches'] 
				if(awayScore>homeScore):
					result_input_team['wld']=1
				elif(homeScore>awayScore):
					result_input_team['wld']=2
				else:
					result_input_team['wld']=3
				print "0,{0},{1}{2},0,{3}".format(awayFactor,idDict[homeTeam],homeFactor,result_input_team['wld'])

#homefactor,awayfactor,opponent team id,homefactor,awayfactor
# 24 12 6
# 27 11 4
# 26 10 6
# 25 7 6
#




