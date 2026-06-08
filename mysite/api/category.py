from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from mysite.database.db import SessionLocal
from mysite.database.models import Category
from mysite.database.schema import CategoryInputSchema, CategoryOutSchema

category_router = APIRouter(prefix="/categories")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@category_router.post("/", response_model=CategoryOutSchema)
def create_category(category: CategoryInputSchema, db: Session = Depends(get_db)):
    category_db = Category(**category.dict())
    db.add(category_db)
    db.commit()
    db.refresh(category_db)
    return category_db


# LIST
@category_router.get("/", response_model=List[CategoryOutSchema])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()


# DETAIL
@category_router.get("/{category_id}", response_model=CategoryOutSchema)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


# UPDATE
@category_router.put("/{category_id}", response_model=CategoryOutSchema)
def update_category(category_id: int, category: CategoryInputSchema, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(status_code=404, detail="Category not found")

    for key, value in category.dict().items():
        setattr(category_db, key, value)

    db.commit()
    db.refresh(category_db)
    return category_db


# DELETE
@category_router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category_db)
    db.commit()
    return {"message": "Category deleted"}
