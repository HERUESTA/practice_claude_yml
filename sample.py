import json
import datetime

def process(f, out):
    d = open(f).read()
    x = json.loads(d)
    res = []
    for u in x:
        if u['age'] > 20 and u['active'] == True:
            score = 0
            if u['score'] >= 80:
                score = 3
            elif u['score'] >= 60:
                score = 2
            elif u['score'] >= 40:
                score = 1
            u['rank'] = score
            res.append(u)
    total = 0
    for r in res:
        total = total + r['score']
    avg = total / len(res)
    summary = {
        'date': str(datetime.datetime.now()),
        'count': len(res),
        'average': avg,
        'users': res
    }
    open(out, 'w').write(json.dumps(summary))
    print('done', len(res), avg)

process('users.json', 'output.json')
