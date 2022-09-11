from django.shortcuts import render


def error_view_404(request, exception):
   return render(request, 'handler_errors/404.html', status=404)

def error_view_500(request):
   return render(request, 'handler_errors/500.html', status=500)