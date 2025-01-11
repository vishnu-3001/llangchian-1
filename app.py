from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os



app=FastAPI(
    title= "Langchain server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model=ChatOpenAI()
prompt1=ChatPromptTemplate.from_template("Write me a poem on {topic}")

add_routes(
    app,
    prompt1|model,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)

