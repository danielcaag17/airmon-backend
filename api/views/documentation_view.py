from django.http import HttpResponse
from django.template import loader
from django.conf import settings
import graphviz
import os

'''
Per a generar el diagrama python manage.py graph_models -a --dot -o my_models.dot
Per a passar de .dot a imatge python manage.py graph_models -a -o my_models.png 
'''

def veure_diagrama(request):
    template = loader.get_template('veure_diagrama.html')
    dot_path = os.path.join(settings.BASE_DIR, 'my_models.dot')
    if not os.path.exists(dot_path):
        raise FileNotFoundError(f"No such file or directory: '{dot_path}'")

    with open(dot_path, 'r') as file:
        dot_data = file.read()

    # Crear un objeto de Graphviz
    dot = graphviz.Source(dot_data)

    # Definir la ruta de salida del PNG
    output_path = os.path.join(settings.BASE_DIR, 'static', 'my_models')
    dot.format = 'png'
    try:
        dot.render(output_path, view=False)
    except PermissionError:
        raise PermissionError(f"Permission denied: '{output_path}.png'")

    return HttpResponse(template.render(context={'png_path': '/static/my_models.png'}, request=request))
