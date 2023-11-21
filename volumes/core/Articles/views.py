from django.contrib import messages
from django.views.generic import ListView, DetailView

from Articles.forms import ArticleCommentModelForm
from Articles.models import Article
from doctors.models import Doctor


class ArticleListView(ListView):
    context_object_name = 'articles'
    paginate_by = 10
    template_name = 'blog/list_view.html'

    def get_queryset(self):
        q = self.kwargs.get('q')
        if q:
            return Article.custom_objects.get_by_search(query=q)
        else:
            return Article.custom_objects.get_active_list()


class ArticleDetailView(DetailView):
    queryset = Article.custom_objects.get_active_list()
    template_name = 'blog/detail_view.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['similar_articles'] = Article.custom_objects.get_active_list().filter(category=self.object.category)[:5]
        context['doctors'] = Doctor.objects.filter(doctor_expertise=self.object.doctor)

    # posts_comments = post_detail.comments.get_queryset().filter(active=True).order_by('id')
    # created_comment = ArticleCommentModelForm(request.POST or None)
    # if created_comment.is_valid():
    #     new_comment = created_comment.save(commit=False)
    #     new_comment.blog_post = post_detail
    #     new_comment.save()
    #     created_comment = ArticleCommentModelForm()
    #     messages.success(request,
    #                      '{}  لقد تم إرسال تعلیقک بنجاح و سیدرج علی الموقع بعد التأیید'.format(new_comment.name),
    #                      extra_tags='comment')


class ArticleCategoryListView(ListView):
    template_name = 'blog/list_view.html'
    paginate_by = 8
    context_object_name = 'articles'

    def get_queryset(self):
        category = self.kwargs.get('slug')
        return Article.custom_objects.get_active_list_by_category(category=category)
