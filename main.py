from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from auth.manager_auth import auth_backend
from auth.database_auth import User, create_db_and_tables
from auth.manager_auth import get_user_manager, current_active_user
from auth.schemas_auth import UserRead, UserCreate
from operation.router_oper import router_oper
from models.router import user_router
from models.db import Base, engine


app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user_router)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app.include_router(router_oper)
app.include_router(user_router)
###

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
@app.get("/authenticated-route",tags=['authenticated'])
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()