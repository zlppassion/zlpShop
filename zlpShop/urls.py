"""zlpShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from zlpShop.settings import MEDIA_ROOT
from django.views.static import serve #用于寻找静态文件
# from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewset,HotSearchsViewset, BannerViewset, IndexCategoryViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset,OrderViewset
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
#配置goods 的url
router.register('goods', GoodsListViewSet, basename='goods')
router.register('codes', SmsCodeViewset, basename='codes')
router.register('hotsearchs', HotSearchsViewset, basename="hotsearchs")
router.register('users', UserViewset, basename='users')
#配置 category的url
router.register('categorys', CategoryViewset, basename='categorys')
#收藏
router.register('userfavs', UserFavViewset, basename='userfavs')
# 留言
router.register('messages', LeavingMessageViewset, basename="messages")
# 收货地址
router.register('address', AddressViewset, basename="address")
#购物车
router.register('shopcarts', ShoppingCartViewset, basename="shopcarts")
#订单相关
router.register('orders', OrderViewset, basename="orders")
#轮播图url
router.register('banners', BannerViewset, basename="banners")
# 首页商品系列数据
router.register('indexgoods', IndexCategoryViewset, basename="indexgoods")
# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^xadmin/', xadmin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #drf 自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    #jwt 的认证接口
    # path('jwt-auth/', obtain_jwt_token),
    path('login/', obtain_jwt_token),
    # media 这个不设置的话，图片显示不出来
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    # 这句代码意思是，与media相关的通通当作静态文件来处理，根据指定好的MEDIA_ROOT路径找寻静态文件
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    # 商品列表页
    # path('goods/', goods_list, name="goods-list"),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="生鲜采购平台")),
]
