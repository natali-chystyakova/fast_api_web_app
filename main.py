from fastapi import FastAPI
from routers.items import router as items_router
from routers.users import router as users_router


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
