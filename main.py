import uvicorn
from fastapi import FastAPI, Depends

from src.routes import user, blog, plant, greenhouse
from src.models.users import Profile, User
from src.handlers.users import get_password_hash, UserManager


app = FastAPI()


# Create Default User
def create_default_usee():

    user_data = {
        "email": "secretsoldier@gmail.com",
        "password": get_password_hash("gajni42564"),
        "profile": {
            "website": "pydatadev.net",
            "location": "Hyderabad, India"
        }
    }
    user = User(**user_data)
    u = UserManager()
    u.create_user(user)


app.include_router(user.router, prefix="/api/user", tags=["users"],)
app.include_router(blog.router, prefix="/api/blog", tags=["articles"])
app.include_router(plant.router, prefix="/api/plant", tags=["plants"])
app.include_router(greenhouse.router,
                   prefix="/api/greenhouse", tags=["greenhouses"])

if __name__ == "__main__":
    create_default_usee()
    uvicorn.run(app)
