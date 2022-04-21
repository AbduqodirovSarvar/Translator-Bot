import requests
from pprint import pprint as pp

app_id = "49dd63a7"
app_key = "9c6f63862b5f860e0e454fdf4dd4e566"
language = "en-gb"

def getDefs(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False
    output={}
    senses=res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    diff=[]
    for sense in senses:
        diff.append(f" {sense['definitions'][0]}")
    output['diff']=''.join(diff)
    audio=res['results'][0]['lexicalEntries'][0]["entries"][0]['pronunciations'][0]
    if audio.get('audioFile'):
        output['audio']=audio['audioFile']
    return output

if __name__ == '__main__':
    pp(getDefs('Great'))
