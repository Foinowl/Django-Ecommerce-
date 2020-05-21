from django.urls import path
from .views import (CheckoutView,
                    HomeView,
                    ItemDetailView,
                    add_to_cart,
                    remove_from_cart,
                    OrderSummaryView,
                    remove_single_item_from_cart,
                    PaymentView,
                    AddCouponView,
                    RequestRefundView,
                    ContentDetailView,
                    SearchResultsView,
                    ViewPage,
                    FeturedHomeView
                    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('fetured/', FeturedHomeView.as_view(), name='fetured'),
    path('view', ViewPage.as_view(), name='view_page'),
    path('results/', SearchResultsView.as_view(), name='search_results'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('<category>/', ContentDetailView.as_view(), name='content'),
]
