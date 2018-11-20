from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from categories.forms import CategoryForm
from categories.models import Category


class CategoryListView(ListView):

    model = Category
    template_name = 'categories/category_list.html'
    paginate_by = 10


class CategoryDetailView(DetailView):

    model = Category
    template_name = 'categories/category_detail.html'


class NewCategoryView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = CategoryForm()
        return render(request, 'categories/new_category.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = CategoryForm(request.POST)

        if form.is_valid():
            new_category = form.save()
            messages.success(request, 'Category {0} created successfully!'.format(new_category.name))
            form = CategoryForm()

        return render(request, 'categories/new_category.html', {'form': form})
