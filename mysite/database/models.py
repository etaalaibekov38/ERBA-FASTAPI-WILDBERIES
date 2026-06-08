from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, Date, ForeignKey, Text, Boolean, DateTime
from typing import Optional, List
from enum import Enum as PyEnum
from datetime import date, datetime

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    token: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=False)
    user_id: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


class StatusChoices(str, PyEnum):
    gold = "Gold"
    silver = "Silver"
    bronze = "Bronze"
    simple = "Simple"

class UserProfile(Base):
    __tablename__ = "profile"
    id: Mapped[int] = mapped_column( Integer,primary_key=True, autoincrement=True)
    first_name:  Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    avatar: Mapped[Optional[str]] = mapped_column(String)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), default=StatusChoices.simple)
    date_registered: Mapped[Optional[date]] = mapped_column(Date, default=date.today())
    user_review: Mapped[List['Review']] = relationship(back_populates="user", cascade="all, delete-orphan")


class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_image: Mapped[str] = mapped_column(String)
    category_name: Mapped[str] = mapped_column(String(20))
    sub_categories: Mapped[List['SubCategory']] = relationship(back_populates="category",
                                                               cascade="all, delete-orphan")


class SubCategory(Base):
    __tablename__ = "sub_category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subcategory_name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped[Category] = relationship(Category, back_populates="sub_categories")
    sub_products: Mapped[List['Product']] = relationship(back_populates="subcategory",
                                                         cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("sub_category.id"))
    subcategory: Mapped[SubCategory] = relationship(back_populates="sub_products")
    product_name: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column(Integer)
    article_number: Mapped[int] = mapped_column(Integer, unique=True)
    description: Mapped[str] = mapped_column(Text)
    video: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    product_type: Mapped[bool] = mapped_column(Boolean)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    images: Mapped[List['ProductImage']] = relationship(back_populates="product",
                                                        cascade="all, delete-orphan")
    product_review: Mapped[List['Review']] = relationship(back_populates="products",
                                                                 cascade="all, delete-orphan")

class ProductImage(Base):
    __tablename__ = "product_image"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(String)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped[Product] = relationship(back_populates="images")



class  Review(Base):
    __tablename__ = "review"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("profile.id"))
    user: Mapped[UserProfile] = relationship( back_populates="user_review")
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    products: Mapped[Product] = relationship(back_populates="product_review")
    text: Mapped[Text] = mapped_column(Text)
    stars: Mapped[int] = mapped_column(Integer)
    created_date: Mapped[date] = mapped_column(Date, default=date.today)
