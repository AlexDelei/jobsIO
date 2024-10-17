from django.shortcuts import render


def get_landing_page(request):
    """
        GET/
    
        Returns the landing page template
    """
    return render(request, 'index.html')
