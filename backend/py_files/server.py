import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers.main_router import router

app = FastAPI()
app.include_router(router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

if __name__ == '__main__':
    uvicorn.run(app, port=8080)