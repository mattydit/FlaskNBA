from flask import Flask
import urllib.request, json, datetime

app = Flask(__name__)

class Schedule:

    def __init__(self, gid, date, time, visitor, home):
        self.gid = gid
        self.date = date
        self.time = time
        self.visitor = visitor
        self.home = home

    def __str__(self):
        return str(self.__class__) + ': ' + str(self.__dict__)

@app.route('/')
def get_games():
    with urllib.request.urlopen("http://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2020/league/00_full_schedule.json") as url:
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
                visitor = j['v']['tn']
                home = j['h']['tn']

                if date == datenow:
                    game = Schedule(gid, date, time, visitor, home)
                    #print(game.gid, game.date, game.time, game.visitor, game.home)
                    gamesList.append(game)

    # for x in gamesList:
    #     print(x.__dict__)

if __name__ == '__main__':
    app.run()

