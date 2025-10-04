from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('food-types', FoodTypeViewSet)
router.register('foods', FoodsViewSet)
router.register('comments', CommentViewSet)

urlpattenrs = router.urls

