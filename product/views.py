import csv, io
from django.contrib import messages
#from django.contrib.auth.decorater import permission_required
from .models import Product
from django.shortcuts import render

from .forms import ProductForm

def product(request):
    template = "product.html"

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save

    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, template, context)

#@permission_required('admin.can_add_log_entry')
def product_upload(request):
    template = "product_upload.html"

    prompt = {
        'order': 'order of CSV file should be product_name, product_sku, product_description'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is not csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Product.objects.update_or_create(
        product_name=column[0],
        product_sku=column[1],
        product_description=column[2]
        )

    context = {}
    return render(request, template, context)
