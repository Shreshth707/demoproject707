from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from script import RecommenderEngine

origins = [
    "https://recommender-script.herokuapp.com",
    "https://shreshth707.github.io/"
    "https://shreshth707.github.io/"
]

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
async def root():
  return {"message": "Hello World"}



@app.get('/recommendation')
async def recommendation(title:str):
	app.model = RecommenderEngine(title.lower());
	recommendations = app.model.getRecommendations();
	return recommendations;



if __name__ == "__main__" :
  app.run(debug=True)
