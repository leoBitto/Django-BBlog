from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from ..models.article import Article


# class articleListView(ListView):
#     model = Article
#     pagination = 20
#     template_name = 'article_list.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['navbar'] = Navbar.objects.first()
#         return context
def articleListView(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }     
    return render(request, 'article_list.html', context)


def articleView(request, slug):
    
    article = get_object_or_404(Article, slug = slug) 
    
    context = {
        'article'  : article,       
         
        }

    return render(request, 'article.html', context)
