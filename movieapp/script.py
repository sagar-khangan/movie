import json
import sqlite3

data = []
with open('../imdb.json') as f:
    data = json.loads(f.read())

directors=set([i['director'] for i in data])
genres=[]

for i in data:
    for j in i['genre']:
        genres.append(j.lstrip())
genres=set(genres)

try:
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    """insert directors and genre"""
    for i in directors:
        c.execute("INSERT OR REPLACE INTO movieapp_director(name) VALUES(?)", (str(i),))
    conn.commit()
    for i in genres:
        c.execute("INSERT OR REPLACE INTO movieapp_genere(name) VALUES(?)", (str(i),))
    conn.commit()
    c.execute("SELECT  id,name from movieapp_director")
    directors_db = {str(i[1]):i[0] for i in c.fetchall()}
    c.execute("SELECT  id,name from movieapp_genere")
    genre_db = {str(i[1]):i[0] for i in c.fetchall()}

    for i in data:
        """insert movies"""
        c.execute("INSERT OR REPLACE INTO movieapp_movie(imdb_score,name,director_id,popularity) VALUES (?,?,?,?);", (i['imdb_score'],i['name'],directors_db[i['director']],i['99popularity']))

        """insert movie genre relation"""
        c.execute("SELECT id from movieapp_movie where name ='{0}'".format(i['name']))
        for x in c.fetchone():
            m = x
            break
        for j in  i['genre']:
            t = j.lstrip()
            c.execute("INSERT OR IGNORE  INTO movieapp_movie_genere(movie_id,genere_id) VALUES (?,?);",(int(m),int(genre_db[t])))
    conn.commit()
    conn.close()

except Exception as e:
    pass

