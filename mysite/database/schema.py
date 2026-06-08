from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, datetime
from .models import StatusChoices



class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str
    age: Optional[int] = None
    phone_number: Optional[str] = None
    avatar: Optional[str] = None

class UserLoginSchema(BaseModel):
     username: str
     password: str

class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int]
    phone_number: Optional[str]
    status: StatusChoices
    date_registered: date

    model_config = {"from_attributes": True}

class CategoryInputSchema(BaseModel):
    category_image: str
    category_name: str



class CategoryOutSchema(BaseModel):
    id: int
    category_image: str
    category_name: str


    model_config = {"from_attributes": True}
class SubCategoryInputSchema(BaseModel):
    subcategory_name: str
    category_id: int


class SubCategoryOutSchema(BaseModel):
    id: int
    subcategory_name: str
    category_id: int

    model_config = {"from_attributes": True}
class ProductImageInputSchema(BaseModel):
    image: str
    product_id: int


class ProductImageOutSchema(BaseModel):
    id: int
    image: str
    product_id: int

    model_config = {"from_attributes": True}
class ReviewInputSchema(BaseModel):
    user_id: int
    product_id: int
    text: str
    stars: int


class ReviewOutSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    text: str
    stars: int
    created_date: date

    model_config = {"from_attributes": True}
class ProductInputSchema(BaseModel):
    subcategory_id: int
    product_name: str
    price: int
    article_number: int
    description: str
    video: Optional[str] = None
    product_type: bool


class ProductOutSchema(BaseModel):
    id: int
    subcategory_id: int
    product_name: str
    price: int
    article_number: int
    description: str
    video: Optional[str]
    product_type: bool
    created_date: datetime

    model_config = {"from_attributes": True}


