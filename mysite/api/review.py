from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from mysite.database.db import SessionLocal
from mysite.database.models import Review
from mysite.database.schema import ReviewOutSchema, ReviewInputSchema

review_router = APIRouter(prefix="/reviews")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@review_router.post("/", response_model=ReviewOutSchema)
def create_review(review: ReviewInputSchema, db: Session = Depends(get_db)):
    review_db = Review(**review.dict())
    db.add(review_db)
    db.commit()
    db.refresh(review_db)
    return review_db


# LIST
@review_router.get("/", response_model=List[ReviewOutSchema])
def list_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()


# DETAIL
@review_router.get("/{review_id}", response_model=ReviewOutSchema)
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return review


# UPDATE
@review_router.put("/{review_id}", response_model=ReviewOutSchema)
def update_review(review_id: int, review: ReviewInputSchema, db: Session = Depends(get_db)):
    review_db = db.query(Review).filter(Review.id == review_id).first()

    if not review_db:
        raise HTTPException(status_code=404, detail="Review not found")

    for key, value in review.dict().items():
        setattr(review_db, key, value)

    db.commit()
    db.refresh(review_db)
    return review_db


# DELETE
@review_router.delete("/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review_db = db.query(Review).filter(Review.id == review_id).first()

    if not review_db:
        raise HTTPException(status_code=404, detail="Review not found")

    db.delete(review_db)
    db.commit()
    return {"message": "Review deleted successfully"}
