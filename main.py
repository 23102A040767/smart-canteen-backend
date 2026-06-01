from fastapi import FastAPI
from pydantic import BaseModel

from database import engine
from models import Base
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User as UserModel

Base.metadata.create_all(bind=engine)   # ADD THIS LINE
 
app = FastAPI()

 
 

meals = [
    {
        "id": 1,
        "name": "Veg Biryani",
        "price": 60,
        "quantity": 10
    },
    {
        "id": 2,
        "name": "Fried Rice",
        "price": 50,
        "quantity": 8
    }
]

# Models
class User(BaseModel):
    username: str
    password: str


class Order(BaseModel):
    meal_id: int


# Register API
@app.post("/register")
def register(user: User, db: Session = Depends(get_db)):

    db_user = UserModel(
        username=user.username,
        password=user.password
    )

    db.add(db_user)
    db.commit()

    return {
        "message": "User Registered Successfully"
    }


# Login API
@app.post("/login")
def login(user: User, db: Session = Depends(get_db)):

    db_user = db.query(UserModel).filter(
        UserModel.username == user.username,
        UserModel.password == user.password
    ).first()

    if db_user:
        return {
            "message": "Login Successful"
        }

    return {
        "message": "Invalid Credentials"
    }

# Get Meals API
@app.get("/meals")
def get_meals():

    return meals


# Place Order API
@app.post("/order")
def place_order(order: Order):

    for meal in meals:

        if meal["id"] == order.meal_id:

            if meal["quantity"] > 0:

                meal["quantity"] -= 1

                return {
                    "message": "Order Placed",
                    "remaining_stock": meal["quantity"]
                }

            return {
                "message": "Out Of Stock"
            }

    return {
        "message": "Meal Not Found"
    }