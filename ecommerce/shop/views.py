from django.shortcuts import render
from .models import Campaign, Category, Product

# Create your views here.


def home(request):
    slide_campaigns = Campaign.objects.filter(is_slide=True)[:3]
    nonslide_campaigns = Campaign.objects.filter(is_slide=False)[:4]
    featured_products = Product.objects.filter(featured=True)[:8]
    recent_products = Product.objects.all().order_by('-created')[:8]
    return render(request, 'home.html', {
        'slide_campaigns': slide_campaigns,
        'nonslide_campaigns': nonslide_campaigns,
        'featured_products': featured_products,
        'recent_products': recent_products
    })



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    has_review = False

    if request.user.is_authenticated and hasattr(request.user, 'customer'):
        has_review = Review.objects.filter(customer=request.user.customer, product=product).exists()

    other_products = Product.objects.exclude(pk=product.pk).order_by('?')[:5]

    return render(request, 'product-detail.html', {
        'product': product,
        'other_products': other_products,
        'has_review': has_review
    })



