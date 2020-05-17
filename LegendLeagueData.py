#--------------------------------------------------
#--------------------------------------------------
#----------------IMPORTANT-------------------------
#-----PLACE THIS FILE INSIDE OF A NEW FOLDER-------
#--------------------------------------------------
#--------------------------------------------------

#      PYTHON 2.6 or higher required

#Requests used to retrieve api
#Json used to parse the json into a string
import requests
import json

#Get an api token from https://developer.clashofclans.com/#/
api = "token"

#Stuff to authorize your api token
headers = {'authorization': 'Bearer ' +(api),'Accept': 'application/json' }

def get_legendleagueseasondata():
    #First Legend League Season
    year = 2015
    month = 7
    while True:

        season = str(year)+'-'+ '{0:02d}'.format(month)
        print('Downloading legend league data for '+ season)
        response = requests.get('https://api.clashofclans.com/v1/leagues/29000022/seasons/'+season, headers=headers)
        season_json = response.json()
        data=open((season)+'.txt',"w", encoding = 'utf-8')
        data.write(json.dumps(season_json))
        data.close()
        month = month + 1
        if month > 12:
            month = 1
            year = year + 1
        #Change if needed. Exits program once all data is retrieved.
        #Say if you want to retrieve data up to June 2025 input if month > 6 and year > 2024:
        if month > 4 and year > 2019:
            exit()
        print('Download complete onto next season')



get_legendleagueseasondata()
