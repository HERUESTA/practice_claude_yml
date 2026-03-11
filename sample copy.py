import json
import datetime

# Constants
MIN_AGE = 20
SCORE_THRESHOLD_HIGH = 80
SCORE_THRESHOLD_MEDIUM = 60
SCORE_THRESHOLD_LOW = 40
RANK_HIGH = 3
RANK_MEDIUM = 2
RANK_LOW = 1

def process(f, out):
    d = open(f).read()
    x = json.loads(d)
    res = []
    for u in x:
        if u['age'] > MIN_AGE and u['active'] == True:
            score = 0
            if u['score'] >= SCORE_THRESHOLD_HIGH:
                score = RANK_HIGH
            elif u['score'] >= SCORE_THRESHOLD_MEDIUM:
                score = RANK_MEDIUM
            elif u['score'] >= SCORE_THRESHOLD_LOW:
                score = RANK_LOW
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
