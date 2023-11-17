from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator

from blog.forms import BlogComment
from blog.models import Post, PostCategory
from django.contrib import messages
from doctors.models import DoctorExpertise, Doctor
# from forms.models import BlogForm


# --------------------------------------------------- blog ListView --------------------------------------------------------


def blog_list(request):
    posts: Post = Post.object.get_queryset().filter(active=True)
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'paginator': paginator,
    }

    return render(request, 'Blog/list_view.html', context)


# --------------------------------------------------- blog Detail funcion base --------------------------------------------------------


def blog_detail(request, pk, slug):
    post_detail: Post = get_object_or_404(Post.object, id=pk, slug=slug, active=True)
    related_posts: Post = Post.object.get_queryset().filter(b_category__blog_category=post_detail).order_by('-id')[:5]

    # ----------------------Doctors------------------------

    doctor: DoctorExpertise = DoctorExpertise.objects.get_queryset().filter(Doctor_Expertiseee__slug=slug).first()
    doctor_in: Doctor = Doctor.objects.get_queryset().filter(doctor_expertise__exact=doctor, active=True)[:10]

    # ----------------------page view------------------------

    post_detail.blog_views += 1
    post_detail.save()

    # ---------------------- comment ------------------------
    posts_comments = post_detail.comments.get_queryset().filter(active=True).order_by('id')
    created_comment: BlogComment = BlogComment(request.POST or None)
    if created_comment.is_valid():
        new_comment = created_comment.save(commit=False)
        new_comment.blog_post = post_detail
        new_comment.save()
        created_comment: BlogComment = BlogComment()
        messages.success(request,
                         '{}  لقد تم إرسال تعلیقک بنجاح و سیدرج علی الموقع بعد التأیید'.format(new_comment.name),
                         extra_tags='comment')

    context = {
        "blog_ditail": post_detail,
        'releted_blog': related_posts,
        'Doctors': doctor_in,
        'comments': posts_comments,
        'created_comment': created_comment,
    }
    return render(request, "Blog/detail_view.html", context)


# --------------------------------------------------- blog search  --------------------------------------------------------


class Search(ListView):
    template_name = "Blog/list_view.html"
    paginate_by = 8

    def get_queryset(self):
        request = self.request
        qoury = request.GET.get('q')
        if qoury is not None:
            return Post.object.search(qoury)

        return Post.object.get_queryset().filter(active=True)


# --------------------------------------------------- blog category  --------------------------------------------------------

def blog_category(request, slug):
    category: PostCategory = get_object_or_404(PostCategory, slug=slug)
    get_posts_by_category = category.blog_category.filter(active=True)
    paginator = Paginator(get_posts_by_category, 8)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        "page_obj": page_obj,
        'paginator': paginator,
    }
    return render(request, 'Blog/list_view.html', context)

