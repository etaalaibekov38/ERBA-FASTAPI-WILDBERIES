from fastapi import FastAPI
import uvicorn


from mysite.api.users import user_router
from mysite.api.category import category_router

from mysite.api.subcategory import subcategory_router
from mysite.api.product import product_router
from mysite.api.product_images import product_image_router
from mysite.api.review import review_router

from mysite.admin.setup import setup_admin
shop_app = FastAPI(title="erbaaaaaaa")


shop_app.include_router(user_router, prefix="/users",  )
shop_app.include_router(category_router, prefix="/categories", )
shop_app.include_router(subcategory_router, prefix="/subcategories",  )
shop_app.include_router(product_router, prefix="/products", )
shop_app.include_router(product_image_router, prefix="/product-images",  )
shop_app.include_router(review_router, prefix="/reviews",  )
from mysite.api.auth import auth_router
setup_admin(shop_app)

shop_app.include_router(auth_router)
if __name__ == '__main__':
    uvicorn.run(shop_app, host="127.0.0.1", port=8000)
