from .views import (
    RefreshTokenAdmin,
    UserProfileAdmin,
    CategoryAdmin,
    SubCategoryAdmin,
    ProductAdmin,
    ProductImageAdmin, 
    ReviewAdmin,
)

from fastapi import FastAPI
from sqladmin import Admin
from mysite.database.db import engine


def setup_admin(app: FastAPI):
    admin = Admin(app, engine)

    admin.add_view(RefreshTokenAdmin)
    admin.add_view(UserProfileAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(SubCategoryAdmin)
    admin.add_view(ProductAdmin)
    admin.add_view(ProductImageAdmin)
    admin.add_view(ReviewAdmin)