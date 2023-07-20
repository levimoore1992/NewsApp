from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView

from news.models import Category, Article
from user.forms import UserCreationForm


# Create your views here.
class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = UserCreationForm()  # Adding here because the form should be on all pages
        context['login_form'] = AuthenticationForm()  # Adding here because the form should be on all pages
        context['categories'] = Category.objects.all()
        return context


class HomeView(BaseView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(status='published')
        return context


class ArticleView(BaseView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.get(id=self.kwargs['id'])

        return context

class CategoryView(BaseView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(category_id=self.kwargs['id'], status='published')
        return context