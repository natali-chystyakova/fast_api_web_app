from fastapi import FastAPI
from routers.items import router as items_router
from routers.users import router as users_router
from routers.tokens import router as tokens_router
import uvicorn

# #(зразок з документацii)
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None, a: Union[str, None] = None):
#     return {"item_id": item_id, "q": q, "a": a}

# core.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=items_router, prefix="/items")

app.include_router(router=users_router, prefix="/users")

app.include_router(router=tokens_router, prefix="/tokens")


if __name__ == "__main__":
    # asyncio.run(main())
    uvicorn.run(
        app="main:app",
        reload=True,
    )

# "email": "nata2@mail.com",
# "password": "nata2nata2"
# 8eaaf5df-df56-40d9-8046-044d57d1716c
