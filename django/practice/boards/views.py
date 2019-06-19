from django.shortcuts import render, redirect
from .models import Board,Comment

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk').all()
    context= {'boards':boards}
    return render(request, 'boards/index.html',context)

def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/form.html')


def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    context= {'board':board}

    return render(request, 'boards/detail.html',context)

def edit(request, board_pk):
    board= Board.objects.get(pk=board_pk)
    if request.method == "POST":
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        context= {'board':board}
        return render(request, 'boards/edit.html',context)


def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    board.delete()

    return redirect('boards:index')

def comment_create(request, board_pk):
    content = request.POST.get('content')
    comment = Comment(content=content, board_id=board_pk)
    comment.save()

    return redirect('boards:detail', board_pk)

def comment_edit(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method=='POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board_pk)
    else:
        context={'comment':comment}
        return render(request,'boards/comment_edit.html',context)

def comment_delete(request, board_pk, comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect('boards:detail', board_pk)