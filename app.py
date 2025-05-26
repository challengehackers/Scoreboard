# Optixal

import requests, time
from flask import Flask, url_for, redirect, render_template
from pprint import pprint

app = Flask(__name__)
BASEURL = 'https://ctf.firstseclounge.org/api/v1'

@app.route('/')
def index():
    return redirect(url_for('scoreboard'))

class Latest():
    def __init__(self, teamname, challname, challcat, challpoints, date):
        self.teamname = teamname
        self.challname = challname
        self.challcat = challcat
        self.challpoints = challpoints
        self.time = time.strftime('%H:%M', time.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ'))

def getLatest():
    data = getData()
    teamMap = {team.id : team.name for team in data}
    latestSolves = []
    for team in data:
        for solve in team.solves:
            latestSolves.append(solve)
    latestSolves = list(sorted(latestSolves, key=lambda x: x['date'], reverse=True))[:10]
    finalData = []
    downloadedTeams = {}

    # [{'challenge_id': 310, 'account_id': 382, 'team_id': 382, 'user_id': 966, 'value': 100, 'date': '2025-05-26T19:11:16.903453Z'}]
    for chall in latestSolves:
        try:
            teamName = teamMap[chall['team_id']]
            if chall['team_id'] not in downloadedTeams:
                print('[*] Downloading team {} info for chall {}...'.format(chall['team_id'], chall['challenge_id']))
                raw = requests.get('{}/teams/{}/solves'.format(BASEURL, chall['team_id']), timeout=3)
                parsed = raw.json()["data"]
                downloadedTeams[chall['team_id']] = parsed
            else:
                print('[*] Re-using team {} info for chall {}...'.format(chall['team_id'], chall['challenge_id'])) #DEBUG
                parsed = downloadedTeams[chall['team_id']]
    
            # Find the challenge name and category
            challName = [x for x in parsed if x["challenge_id"] == chall['challenge_id']][0]['challenge']['name']
            challCat = [x for x in parsed if x["challenge_id"] == chall['challenge_id']][0]['challenge']['category']            
            teamName = [x for x in parsed if x["team"]['id'] == chall['team_id']][0]["team"]["name"]

            print(f'[*] Found solve for team {teamName} on challenge {challName} in category {challCat} worth {chall["value"]} points at {chall["date"]}') #DEBUG

            l = Latest(teamName, challName, challCat, chall['value'], chall['date'])
            finalData.append(l)
        except Exception as e:
            print(f"FATAL ERROR: {e}")
            continue
    return finalData

@app.route('/latest')
def latest():
    data = getLatest()
    return render_template('latest.html', data=data)

class Team():
    def __init__(self, teamPosition, teamDict):
        self.position = int(teamPosition)
        self.name = teamDict['name']
        self.id = teamDict['id']
        self.solves = [solve for solve in teamDict['solves'] if solve['challenge_id']]
        self.solved = len(self.solves)
        self.score = teamDict['score']


def getData():
    data = []
    while True:
        try:
            print('[*] Downloading scoreboard data...')
            raw = requests.get('{}/scoreboard/top/20'.format(BASEURL), timeout=4)
            print('[+] Smexy...')
            parsed = raw.json()['data']
            for teamPosition, teamDict in parsed.items():
                t = Team(teamPosition, teamDict)
                data.append(t)
            break
        except Exception as e:
            print(e)
            continue
    data = sorted(data, key=lambda x: x.position)
    return data

@app.route('/data')
def data():
    data = getData()
    return render_template('data.html', teams=data)

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/timer')
def timer():
    return render_template('timer.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

