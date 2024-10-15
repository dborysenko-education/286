import pandas as pd

data = pd.read_csv("286/netflix_titles_1.csv")

# print(df)

# data = [
#     ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'],
#     ['s1', 'Movie', 'Dick Johnson Is Dead', 'Kirsten Johnson', '', 'United States', '25.09.2021', 2020, 'PG-13', '90 min', 'Documentaries', 'As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable.'],
#     ['s2', 'TV Show', 'Blood & Water', '', 'Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel, Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu, Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys, Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng', 'South Africa', '24.09.2021', 2021, 'TV-MA', '2 Seasons', 'International TV Shows, TV Dramas, TV Mysteries', 'After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth.'],
#     ['s3', 'TV Show', 'Ganglands', 'Julien Leclercq', 'Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabiha Akkari, Sofia Lesaffre, Salim Kechiouche, Noureddine Farihi, Geert Van Rampelberg, Bakary Diombera', '', '24.09.2021', 2021, 'TV-MA', '1 Season', 'Crime TV Shows, International TV Shows, TV Action & Adventure', 'To protect his family from a powerful drug lord, skilled thief Mehdi and his expert team of robbers are pulled into a violent and deadly turf war.'],
#     ['s4', 'TV Show', 'Jailbirds New Orleans', '', '', '', '24.09.2021', 2021, 'TV-MA', '1 Season', 'Docuseries, Reality TV', 'Feuds, flirtations and toilet talk go down among the incarcerated women at the Orleans Justice Center in New Orleans on this gritty reality series.'],

# ]

actors = ['Richard Gere', 'Bruce Willis', 'Dua Lipa']
for movie in data[1:]: 
    movie_actors = movie[4].split(",")
    for actor in movie_actors: 
        actors.append(actor)

print(actors)

# ['', 'Ama Qamata', ' Khosi Ngema', ' Gail Mabalane', ' Thabang Molaba', 
#  ' Dillon Windvogel', ' Natasha Thahane', ' Arno Greeff', ' Xolile Tshabalala', 
#  ' Getmore Sithole', ' Cindy Mahlangu', ' Ryle De Morny', ' Greteli Fincham', 
#  ' Sello Maake Ka-Ncube', ' Odwa Gwanya', ' Mekaila Mathys', ' Sandi Schultz', 
#  ' Duane Williams', ' Shamilla Miller', ' Patrick Mofokeng', 'Sami Bouajila', 
#  ' Tracy Gotoas', ' Samuel Jouy', ' Nabiha Akkari', ' Sofia Lesaffre', 
#  ' Salim Kechiouche', ' Noureddine Farihi', ' Geert Van Rampelberg', 
#  ' Bakary Diombera', '']

actors_movie_count = []
for actor in actors: 
    counter = 0
    for movie in data: 
        if actor in movie[4]:
            counter += 1
    actors_movie_count.append([actor, counter])

print(actors_movie_count)


[['', 5], 
 ['Ama Qamata', 1], [' Khosi Ngema', 1], [' Gail Mabalane', 1], 
 [' Thabang Molaba', 1], [' Dillon Windvogel', 1], [' Natasha Thahane', 1], 
 [' Arno Greeff', 1], ['Xolile Tshabalala', 1], [' Getmore Sithole', 1], 
 [' Cindy Mahlangu', 1], [' Ryle De Morny', 1], [' Greteli Fincham', 1], 
 [' Sello Maake Ka-Ncube', 1], [' Odwa Gwanya', 1], [' Mekaila Mathys', 1], 
 [' Sandi Schultz', 1], [' Duane Williams', 1], [' Shamilla Miller', 1], 
 [' Patrick Mofokeng', 1], ['Sami Bouajila', 1], [' Tracy Gotoas', 1], 
 [' Samuel Jouy', 1], [' Nabiha Akkari', 1], [' Sofia Lesaffre', 1], 
 [' Salim Kechiouche', 1], [' Noureddine Farihi', 1], 
 [' Geert Van Rampelberg', 1], [' Bakary Diombera', 1], ['', 5]]