from numpy.lib.shape_base import tile
import pandas as pd
import numpy as np
from numpy.core.numeric import NaN
from numpy.lib.arraysetops import isin
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_movie(input):
	data  = pd.read_csv('archive3/movies_metadata.csv',low_memory=False)
	kw = pd.read_csv('archive3/keywords.csv')
	credits = pd.read_csv('archive3/credits.csv')

	

	kw['id'] = kw['id'].astype('int')
	credits['id'] = credits['id'].astype('int')
	data['id'] = data['id'].astype('int')

	data = data.merge(credits, on='id')
	data = data.merge(kw, on='id')

	


	features = ['cast', 'crew', 'keywords', 'genres']
	for feature in features:
		data[feature] = data[feature].apply(literal_eval)

	def get_director(x):
		for i in x:
			if i['job'] == 'Director':
				return i['name']
		return np.nan

	def get_list(x):
		if isinstance(x, list):
			names = [i['name'] for i in x]
			
			if len(names) > 3:
				names = names[:3]
			return names

		
		return []

	data['director'] = data['crew'].apply(get_director)

	features = ['cast', 'keywords', 'genres']

	for feature in features:
		data[feature] = data[feature].apply(get_list)

	def clean_data(x):
		if isinstance(x, list):
			return [str.lower(item.replace(" ", "")) for item in x]
		else:
			
			if isinstance(x, str):
				return str.lower(x.replace(" ", ""))
			else:
				return ''

	features = ['cast', 'keywords', 'director', 'genres']


	for feature in features:
		data[feature] = data[feature].apply(clean_data)

	def combine(x):
		return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])

	data['combine'] = data.apply(combine, axis=1)


	count = CountVectorizer()
	count_matrix = count.fit_transform(data['combine'])

	cosine_sim2 = cosine_similarity(count_matrix)

	data = data.reset_index()
	indices = pd.Series(data.index, index=data['title'])

	
	index = indices[input]

	sim_scores = list(enumerate(cosine_sim2[index]))

	sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

	sim_scores = sim_scores[1:21]

	movie_indices = [i[0] for i in sim_scores]

	movie_img = data['poster_path'].iloc[movie_indices]

	title = data['title'].iloc[movie_indices]

	return title, movie_img
#asd = get_movie('The Godfather')
#print(asd)