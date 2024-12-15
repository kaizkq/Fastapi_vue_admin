from fastapi import FastAPI
from book.router import books
from user.router import user
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


register_tortoise(
    app,
    # MySQL configuration (commented)
    # db_url="mysql://root:root123@127.0.0.1:3306/fastapibook",
    
    # PostgreSQL configuration
    db_url="postgres://root:root123@127.0.0.1:5432/fastapi_vue_admin",
    modules={"models": ["user.model", "book.model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(books)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True, port=5000)
