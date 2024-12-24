from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - fastapi-coll-756b8bf8629240c2a68163b2c8941f8a',debug=False,docs_url='/vibrant-bohr-01a3c4bac1ce11ef89340242ac12000546/docs',openapi_url='/vibrant-bohr-01a3c4bac1ce11ef89340242ac12000546/openapi.json')

app.include_router(router, prefix='/vibrant-bohr-01a3c4bac1ce11ef89340242ac12000546/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()