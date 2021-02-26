from flask import Flask
import urllib.request, json

app = Flask(__name__)


@app.route('/')
def get_games():
    with urllib.request.urlopen("http://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2020/league/00_full_schedule.json") as url:
        data = json.load(url)

        # print(data)
        # print(data['lscd'])

        lscd = data['lscd']
        # print(lscd)

        for i in lscd:
            # print(i['mscd']['g'])
            for j in i['mscd']['g']:
                # print(j)
                gid = j['gid']
                print(gid)
                date = j['gdte']
                print(date)
                time = j['utctm']
                print(time)
                # print(j['v'])
                visitor = j['v']['tn']
                print(visitor)
                home = j['h']['tn']
                print(home)
                print('')


if __name__ == '__main__':
    app.run()

