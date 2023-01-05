from django.shortcuts import render


def menu(request):
    title = 'tree_menu'
    template = 'tree_menu/draw_menu.html'
    context = {
        'title': title,
    }
    return render(request, template, context)
