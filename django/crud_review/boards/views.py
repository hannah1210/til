from django.shortcuts import render,redirect
from .models import Board, Comment
from IPython import embed
# Create your views here.
def index(request):
    boards = Board.objects.all().order_by('-pk')
    context = {'boards':boards}
    return render(request,'boards/index.html',context)

def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        img_file = request.FILES.get('img_file')
        if img_file is not None:
            board = Board(title=title,content=content,image=img_file)
        else:
            board = Board(title=title, content=content)
        board.save()
        #return render(request, 'boards/form.html')
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/form.html')

def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)

    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else:
        comments = Comment.objects.filter(board=board)
        context = {'board':board, 'comments':comments}
        return render(request, 'boards/detail.html', context)

def delete(request,board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail',  board.pk)


def edit(request,board_pk):
    board= Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board = Board.objects.get(pk=board_pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()

        return redirect('boards:detail', board.pk)
    else:
        context = {'board': board}

        return render(request, 'boards/edit.html', context)


def comments_create(request, board_pk):
    board=Board.objects.get(pk=board_pk)
    if request.method == "POST":
        comment = Comment()
        comment.board_id = board.pk
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail',board.pk)
    else:
        return redirect('boards:detail',board.pk)

def comment_edit(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "POST":
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail',board_pk)
    else:
        context = {'comment':comment}
        return render(request, 'boards/comment_edit.html',context)

def comment_delete(request,board_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "POST":
        comment.delete()
        return redirect('boards:detail',board_pk)
    else:
        return redirect('boards:detail',board_pk)





