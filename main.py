from fastapi import FastAPI
from script import RecommenderEngine

app = FastAPI()

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
