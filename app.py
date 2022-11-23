from flask import Flask, jsonify
import urllib.request, json, datetime

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

class Schedule:

    def __init__(self, gid, date, time, visitorName, visitorCity, visitorScore, homeName, homeCity, homeScore):
        self.gid = gid
        self.date = date
        self.time = time
        self.visitorName = visitorName
        self.visitorCity = visitorCity
        self.visitorScore = visitorScore
        self.homeName = homeName
        self.homeCity = homeCity
        self.homeScore = homeScore

    def __str__(self):
        return str(self.__class__) + ': ' + str(self.__dict__)

    # def get_dict(self, item):
    #     return self.__dict__[item]

@app.route('/')
def get_games():
    with urllib.request.urlopen("https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2022/league/00_full_schedule.json") as url:
        data = json.load(url)

        datenow = str(datetime.date.today())
        gamesList = []
        lscd = data['lscd']
        # print(lscd)

        for i in lscd:
            # print(i['mscd']['g'])
            for j in i['mscd']['g']:
                gid = j['gid']
                date = j['gdte']
                time = j['utctm']
                visitorName = j['v']['tn']
                visitorCity = j['v']['tc']
                visitorScore = j['v']['s']
                homeName = j['h']['tn']
                homeCity = j['h']['tc']
                homeScore = j['h']['s']

                if date == datenow:
                    game = Schedule(gid, date, time, visitorName, visitorCity, visitorScore, homeName, homeCity,
                    homeScore)
                    #print(game.gid, game.date, game.time, game.visitor, game.home)
                    gamesList.append(game.__dict__)

    return jsonify(gamesList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

