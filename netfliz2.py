netflix = [
    ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
    ['s1', 'Movie', 'Dick Johnson Is Dead', 'Kirsten Johnson', '', 'United States', '25.09.2021', 2020, 'PG-13', '90 min', 'Documentaries', 'As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable.'],
    ['s2', 'TV Show', 'Blood & Water', '', 'Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel, Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu, Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys, Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng', 'South Africa', '24.09.2021', 2021, 'TV-MA', '2 Seasons', 'International TV Shows, TV Dramas, TV Mysteries', 'After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth.'],
    ['s3', 'TV Show', 'Ganglands', 'Julien Leclercq', 'Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabiha Akkari, Sofia Lesaffre, Salim Kechiouche, Noureddine Farihi, Geert Van Rampelberg, Bakary Diombera', '', '24.09.2021', 2021, 'TV-MA', '1 Season', 'Crime TV Shows, International TV Shows, TV Action & Adventure', 'To protect his family from a powerful drug lord, skilled thief Mehdi and his expert team of robbers are pulled into a violent and deadly turf war.'],
    ['s4', 'TV Show', 'Jailbirds New Orleans', '', '', '', '24.09.2021', 2021, 'TV-MA', '1 Season', 'Docuseries, Reality TV', 'Feuds, flirtations and toilet talk go down among the incarcerated women at the Orleans Justice Center in New Orleans on this gritty reality series.'],
]

# for movie in netflix: 
#     if movie[4] != '': 
#         actors = movie[4].split(",")
#         actors_count = len(actors)
#     else:
#         actors_count = 0
#     print(f"Movie: {movie[2]}, Actors: {actors_count}")

all_actors = []
for movie in netflix[1:]: 
    if movie[4] != '': 
        actors = movie[4].split(",")
        for actor in actors: 
            all_actors.append(actor)

print(all_actors)

actors_films = []
for d in all_actors: 
    counter = 0
    for movie in netflix: 
        if netflix_actor in movie[4].split(","): 
            counter += 1
    actors_films.append([actor, counter])

print(actors_films)

# ['Ama Qamata', ' Khosi Ngema', ' Gail Mabalane', ' Thabang Molaba', 
#  ' Dillon Windvogel', ' Natasha Thahane', ' Arno Greeff', ' Xolile Tshabalala', 
#  ' Getmore Sithole', ' Cindy Mahlangu', ' Ryle De Morny', ' Greteli Fincham', 
#  ' Sello Maake Ka-Ncube', ' Odwa Gwanya', ' Mekaila Mathys', ' Sandi Schultz', 
#  ' Duane Williams', ' Shamilla Miller', ' Patrick Mofokeng', 'Sami Bouajila', 
#  ' Tracy Gotoas', ' Samuel Jouy', ' Nabiha Akkari', ' Sofia Lesaffre', 
#  ' Salim Kechiouche', ' Noureddine Farihi', ' Geert Van Rampelberg', 
# ' Bakary Diombera']
        
