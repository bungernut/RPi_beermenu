from flask import Flask
from flask_table import Table, Col

app = Flask(__name__)

N_taps = 12

class BeerMenuTable(Table):
    tap  = Col('Tap #')
    name = Col('Beer Name')
    ibu  = Col('IBUs')
    abv  = Col('ABV')
    
items = [
dict(tap=1, name='Morning After', ibu=10, abv=6.7),
dict(tap=2, name='Akin Pump',     ibu=10, abv=5.5),
dict(tap=3, name='Dopulin Laizy', ibu=70, abv=6.0)
]

items2 = []
for i in items:
    items2.append({})
    for k in i.keys():
        if k == 'ibu':
            if i[k] < 20:
                items2[-1][k] = """<img src="images/0 Hops.png" width="20%">"""
            if i[k] >= 20:
                items2[-1][k] = """<img src="images/1 Hops.png" width="20%">"""
        else:
            items2[-1][k] = i[k]
        

BeerMenu = BeerMenuTable(items2, border=True)

print(BeerMenu.__html__())

@app.route('/')
def index():
    return BeerMenu.__html__()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')