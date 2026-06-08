from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import SessionLocal
from mysite.database.models import ProductImage
from mysite.database.schema import (
    ProductImageOutSchema,
    ProductImageInputSchema
)

product_image_router = APIRouter(prefix="/product-images")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@product_image_router.post("/", response_model=ProductImageOutSchema)
def create_image(image: ProductImageInputSchema, db: Session = Depends(get_db)):
    image_db = ProductImage(**image.dict())
    db.add(image_db)
    db.commit()
    db.refresh(image_db)
    return image_db


# LIST
@product_image_router.get("/", response_model=List[ProductImageOutSchema])
def list_images(db: Session = Depends(get_db)):
    return db.query(ProductImage).all()


# DETAIL
@product_image_router.get("/{image_id}", response_model=ProductImageOutSchema)
def get_product_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(ProductImage).filter(ProductImage.id == image_id).first()

    if not image:
        raise HTTPException(status_code=404, detail="Product image not found")

    return image


# UPDATE
@product_image_router.put("/{image_id}", response_model=ProductImageOutSchema)
def update_product_image(image_id: int, image: ProductImageInputSchema, db: Session = Depends(get_db)):
    image_db = db.query(ProductImage).filter(ProductImage.id == image_id).first()

    if not image_db:
        raise HTTPException(status_code=404, detail="Product image not found")

    for key, value in image.dict().items():
        setattr(image_db, key, value)

    db.commit()
    db.refresh(image_db)
    return image_db


# DELETE
@product_image_router.delete("/{image_id}")
def delete_product_image(image_id: int, db: Session = Depends(get_db)):
    image_db = db.query(ProductImage).filter(ProductImage.id == image_id).first()

    if not image_db:
        raise HTTPException(status_code=404, detail="Product image not found")

    db.delete(image_db)
    db.commit()
    return {"message": "Product image deleted successfully"}
