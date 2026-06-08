from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import SessionLocal
from mysite.database.models import SubCategory
from mysite.database.schema import SubCategoryOutSchema, SubCategoryInputSchema

subcategory_router = APIRouter(prefix="/subcategories")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@subcategory_router.post("/", response_model=SubCategoryOutSchema)
def create_subcategory(subcategory: SubCategoryInputSchema, db: Session = Depends(get_db)):
    sub_db = SubCategory(**subcategory.dict())
    db.add(sub_db)
    db.commit()
    db.refresh(sub_db)
    return sub_db


# LIST
@subcategory_router.get("/", response_model=List[SubCategoryOutSchema])
def list_subcategories(db: Session = Depends(get_db)):
    return db.query(SubCategory).all()


# DETAIL
@subcategory_router.get("/{subcategory_id}", response_model=SubCategoryOutSchema)
def get_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    sub = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="SubCategory not found")
    return sub


# UPDATE
@subcategory_router.put("/{subcategory_id}", response_model=SubCategoryOutSchema)
def update_subcategory(subcategory_id: int, subcategory: SubCategoryInputSchema, db: Session = Depends(get_db)):
    sub_db = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()

    if not sub_db:
        raise HTTPException(status_code=404, detail="SubCategory not found")

    for key, value in subcategory.dict().items():
        setattr(sub_db, key, value)

    db.commit()
    db.refresh(sub_db)
    return sub_db


# DELETE
@subcategory_router.delete("/{subcategory_id}")
def delete_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    sub_db = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()

    if not sub_db:
        raise HTTPException(status_code=404, detail="SubCategory not found")

    db.delete(sub_db)
    db.commit()
    return {"message": "SubCategory deleted successfully"}
