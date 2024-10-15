import pandas as pd

netflix = pd.read_csv("286/netflix_titles_1.csv")

# print(netflix)

# print(netflix['cast'])

netflix_actors = []

for cast in netflix[:200]['cast']: 
    # print(cast)
    if isinstance(cast, str):
        movie_actors = cast.split(',')
        for movie_actor in movie_actors: 
            netflix_actors.append(movie_actor)

# print(len(netflix_actors))

actors = []
for actor in netflix_actors: 
    if actor[0] == " ": 
        actor = actor[1:]
    if actor not in actors: 
        actors.append(actor)

print(len(actors))

actors_and_movies = []

for actor in actors: 
    for cast in netflix['cast']: 
        counter = 0
    # print(cast)
        if isinstance(cast, str):
            movie_actors = cast.split(',')
            
            if actor in movie_actors: 
            # if actor in cast: 
                counter += 1
            else: 
                continue
                
    actors_and_movies.append([actor, counter])

print(actors_and_movies)