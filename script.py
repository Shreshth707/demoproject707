import numpy as np;
import pandas as pd;
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommenderEngine():
	def __init__(self,title):
		self.title = title.lower();
		self.df = pd.read_csv('main_data.csv');

	def getRecommendations(self):
		similarity_score = self.create_similarity();
		most_simillar_movies = self.get_most_simillar_movies(similarity_score);
		most_simillar_movies_title = [];
		for movie_row in most_simillar_movies:
			most_simillar_movies_title.append(self.df.iloc[movie_row].movie_title);

		return most_simillar_movies_title;

	def get_movie_row(self):
		index = self.df[self.df.movie_title==self.title].index.values.astype(int);
		print(index);
		if index.size==0:
			self.found = False;
			return index;
		self.found = True;
		return index[0]; 

	def create_similarity(self):
		countVectorizer = CountVectorizer();
		count_matrix = countVectorizer.fit_transform(self.df['comb']);
		similarity_score = cosine_similarity(count_matrix);
		return similarity_score;


	def get_most_simillar_movies(self,similarity_score):
		final_sorted_movies = [];
		movie_row = self.get_movie_row();
		print(movie_row);
		if(self.found==False):
			return final_sorted_movies;
		similar_movies = list(enumerate(similarity_score[movie_row]));
		sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True);
		sorted_similar_movies =  sorted_similar_movies[:13];
		
		
		for movie in sorted_similar_movies:
			final_sorted_movies.append(movie[0]);

		return final_sorted_movies;



# searched_movie = 'The Avengers';
# searched_movie = searched_movie.lower();
# df = pd.read_csv('main_data.csv');

# similarity_score = create_similarity(df);
# most_simillar_movies = get_most_simillar_movies(similarity_score);

# for movie_row in most_simillar_movies:
# 	print(df.loc[[movie_row]].movie_title);


# obj = RecommenderEngine("The Avengers");
# print(obj.get_most_simillar_movies(obj.create_similarity()));