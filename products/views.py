from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q, Sum, Count
from .models import Product, Category, Rating
from .forms import ProductForm, CommentForm
from django.db.models.functions import Lower

# Create your views here.

def all_products(request):

    """
    A view to return all products in the database
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    rating = Rating.objects.all()

    products = products.annotate(avg = Sum('rating__rating') / Count('rating__rating', distinct=True))

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'rating':
                sortkey = 'rating__rating'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    products = products.order_by(F(sortkey).desc(nulls_last=True))
                else:
                    products = products.order_by(sortkey)
            

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)            

        if 'deals' in request.GET:
            products = products.filter(on_sale = True)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'rating': rating,
    }
    
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    already_rated = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = Product.objects.get(id=product_id)
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect(reverse('product_detail', args=[product_id]))
    
    product = get_object_or_404(Product, pk=product_id)
    rating = Rating.objects.filter(product=product_id)
    if rating.__len__() > 0:
        avg = rating.aggregate(avg=Sum('rating') / Count('rating', distinct=True))
        for rate in rating:
            if rate.author_id == request.user.id:
                already_rated = True
                break

    form = CommentForm()
    if rating.__len__() > 0:
        context = {
            'product': product,
            'rating': rating,
            'ingredients': product.ingredients.all(),
            'form': form,
            'avg': (round(avg['avg'],2)),
            'already_rated': already_rated,
        }
    else:
        context = {
            'product': product,
            'rating': rating,
            'ingredients': product.ingredients.all(),
            'form': form,
        }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the correct permissions to do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have the correct permissions to do that.")
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

@login_required
def delete_comment(request, comment_id):
    """ Delete a product from the store """
    rating = get_object_or_404(Rating, id=comment_id)
    if not request.user.id == rating.author_id:
        messages.error(request, "Sorry, you don't have the correct permissions to do that.")
        return redirect(reverse('home'))
    rating.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('product_detail', args=[rating.product_id]))