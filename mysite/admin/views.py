from sqladmin import ModelView
from mysite.database.models import (
    RefreshToken,
    UserProfile,
    Category,
    SubCategory,
    Product,
    ProductImage,
    Review
)

class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = [RefreshToken.id, RefreshToken.token, RefreshToken.user_id]
class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.id, UserProfile.first_name, UserProfile.last_name, UserProfile.email]
class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.category_name]
class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [SubCategory.id, SubCategory.subcategory_name, SubCategory.category_id]
class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.product_name, Product.price, Product.article_number]
class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [ProductImage.id, ProductImage.image, ProductImage.product_id]
class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.user_id, Review.product_id, Review.stars]