import pandas as pd 

netflix = pd.read_csv("286/netflix_titles_1.csv")

# print(netflix["listed_in"])


# netflix_categories = netflix["listed_in"]
# categories = []
# for cat_list in netflix_categories: 
#     if isinstance(cat_list, str): 
#         # cat_list = cat_list.split(",")
#         for cat in cat_list.split(","): 
#             categories.append(cat)

# # print(categories)

# show_categories = []

# for category in categories: 
#     if category[0] == " ": 
#         category = category[1:]
    
#     if category not in show_categories: 
#         show_categories.append(category)

# print(show_categories)

categories = ['Documentaries', 'International TV Shows', 'TV Dramas', 'TV Mysteries', 
 'Crime TV Shows', 'TV Action & Adventure', 'Docuseries', 'Reality TV', 
 'Romantic TV Shows', 'TV Comedies', 'TV Horror', 'Children & Family Movies', 
 'Dramas', 'Independent Movies', 'International Movies', 'British TV Shows', 
 'Comedies', 'Spanish-Language TV Shows', 'Thrillers', 'Romantic Movies', 
 'Music & Musicals', 'Horror Movies', 'Sci-Fi & Fantasy', 'TV Thrillers', 
 "Kids' TV", 'Action & Adventure', 'TV Sci-Fi & Fantasy', 'Classic Movies', 
 'Anime Features', 'Sports Movies', 'Anime Series', 'Korean TV Shows', 
 'Science & Nature TV', 'Teen TV Shows', 'Cult Movies', 'TV Shows', 
 'Faith & Spirituality', 'LGBTQ Movies', 'Stand-Up Comedy', 'Movies', 
 'Stand-Up Comedy & Talk Shows', 'Classic & Cult TV']


netflix_categories = []
for category in categories: 
    counter = 0 
    for movie in netflix["listed_in"]: 
        if category in movie: 
            counter += 1
        
    netflix_categories.append([category, counter])
print(netflix_categories)






    
