from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of 3 posts.
    **For context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        No of posts per page.

    **Template:**

    :template:`blog/index.html`
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3


def post_detail(request, slug):
    """
    Displays individual :model:`blog.Post`.

    **For context**

    ``post``
        Instace of :model:`blog.Post`
    ``comments``
        All approved comments related to post.
    ``comment_count``
        Count of approved comments related to post.
    ``comment_form``
        Instance of :form:`blog.CommentForm`

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment is submitted and is waiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Displays individual comment for editing.

    **For context**

    ``post``
        Instance of :model:`blog.Post`.
    ``comment``
        Singular commment related to post.
    ``comment_form``
        Instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment successfully updated')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error. Something has gone wrong when updating comment')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Deletion of individual comment.

    **For context**

    ``post``
        Instance of :model:`blog.Post`.
    ``comment``
        Singular comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Comment has been deleted successfully')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can delete only comments you posted')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
