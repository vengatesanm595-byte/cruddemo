from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import productForm
from django.core.paginator import Paginator


def Product_list(request):
    products=Product.objects.all()
    return render(request,'product_list.html',{'products':products})
    
def add_product(request):
    form=productForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'product_form.html',{'form':form})

def update_product(request,id):
    product=get_object_or_404(Product,id=id)
    form=productForm(request.POST or None,request.FILES or None,instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'product_form.html',{'form':form})

def delete_product(request,id):
     product=get_object_or_404(Product,id=id)
     product.delete()
     return redirect('product_list')

def product_home(request):
    search=request.GET.get('search')
    if search:
        product_list=Product.objects.filter(name__icontains=search)
    else:
        product_list=Product.objects.all()

    paginator=Paginator(product_list,8)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render (request,'home.html',{'page_obj':page_obj,'search':search})
    


# Create your views here.
