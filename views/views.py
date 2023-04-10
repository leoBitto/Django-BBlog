from django.shortcuts import get_object_or_404, render
from ..models.article import Article


def articleListView(request):
    articles = Article.objects.filter(status="published")

    context = {
        'articles': articles,
    }     
    return render(request, 'BBlog/article_list.html', context)


def articleView(request, slug):
    
    article = get_object_or_404(Article, slug = slug) 
    
    context = {
        'article'  : article,       
         
        }

    return render(request, 'BBlog/article.html', context)
