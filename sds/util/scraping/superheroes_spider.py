from bs4 import BeautifulSoup
import json, os, re, requests, sys, time
import pandas as pd
from tqdm import tqdm

for page in tqdm(range(1, 140)):  # 140
    if os.path.exists(f'heroes-{page}.csv'):
        print(f'heroes-{page}.csv exists: skipping')
        continue
    print(f'page {page}/140: retrieving heroes')
    r = requests.get(f'https://www.superherodb.com/characters/?page_nr={page}')
    c = BeautifulSoup(r.content, 'html.parser')

    heroes = []
    for a in c.body.main.div.contents[7]('a'):
        heroes.append({'name': a.contents[0], 'href': a['href']})
    
    time.sleep(0.2)

    print('processing heroes')
    for h in tqdm(heroes):
        try:

            r = requests.get('https://www.superherodb.com' + h['href'])
            c = BeautifulSoup(r.content, 'html.parser')
            if h['name'] != c.h1.string:
                h['name'] = c.h1.string
                print(f'WARNING: inconsistency {h["name"]}-->{c.h1.string}')

            h['identity'] = c.h2.string

            # stats_sect = c.find(lambda tag: tag.string=='Power Stats')
            # stats = stats_sect.parent.contents
            stats = c.find_all('div', class_='stat-holder')[0].next_sibling.string
            start = stats.find('bars')
            stats = stats[start+6:]
            end = stats.find('}')
            stats = stats[:end+1]
            stats = json.loads(stats)
            h['intelligence'] = stats['int']
            h['strength'] = stats['str']
            h['speed'] = stats['spe']
            h['durability'] = stats['dur']
            h['power'] = stats['pow']
            h['combat'] = stats['com']

            powers_sect = c.find(lambda tag: tag.string=='Super Powers')
            if powers_sect:
                powers = powers_sect.parent.contents
                h['powers'] = [t.i.next_sibling for t in powers if t.name=='a']
            else:
                h['powers'] = ''

            origin_sect = c.find(lambda tag: tag.string=='Origin')
            origin = origin_sect.next_sibling.next_sibling('tr')
            fields = [list(f.stripped_strings) for f in origin]
            field_names = ('Universe', 'Full name', 'Place of birth', 'Alignment', 'First appearance')
            for f in fields:
                if f[0] in field_names:
                    f[0] = f[0].lower()
                    if len(f) == 1:
                        f.append('')
                    h[f[0]] = f[1]
                
            # year = re.findall('\d{4}', h['first appearance'])
            # h['first appearance'] = year[0] if year else ''

            if 'universe' not in h:
                h['universe'] = ''
            
            appearance_sect = c.find(lambda tag: tag.string=='Appearance')
            appearance = appearance_sect.next_sibling.next_sibling('tr')
            fields = [list(f.stripped_strings) for f in appearance]
            field_names = ('Gender', 'Height', 'Weight', 'Eye color', 'Hair color')
            for f in fields:
                if f[0] in field_names:
                    f[0] = f[0].lower()
                    if len(f) == 1:
                        f.append('')
                    h[f[0]] = f[1]

            time.sleep(0.2)
        except Exception as e:
            print(f'Exception during page {page}, hero {h["name"]}')
            print(e)

    df = pd.DataFrame(heroes)
    df.to_csv(f'heroes-{page}.csv')

print('merging CSV files')
os.system('cat heroes-*.csv > heroes_all.csv')

# os.system('rm heroes-*.csv')
# os.system('mv heroes_all.csv heroes.csv')