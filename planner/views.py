from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def generate_plan(request):

    idea = request.data.get('idea', '').strip()

    if not idea:
        return Response(
            {'error': 'La idea es obligatoria.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    plan = {
        'title': 'Sistema de gestión de inventario',
        'summary': 'Aplicación web para gestionar productos, stock y movimientos.',
        'complexity': 'Media',
        'totalTime': '5 semanas',
        'technologies': [
            'Angular',
            'Django',
            'PostgreSQL'
        ],
        'steps': [
            {
                'step': 'Análisis',
                'description': 'Definir los requerimientos del proyecto.',
                'time': '2 días'
            },
            {
                'step': 'Diseño',
                'description': 'Diseñar la estructura y arquitectura de la aplicación.',
                'time': '3 días'
            },
            {
                'step': 'Backend',
                'description': 'Desarrollar la API y la lógica del sistema.',
                'time': '2 semanas'
            },
            {
                'step': 'Frontend',
                'description': 'Construir la interfaz de usuario.',
                'time': '2 semanas'
            },
            {
                'step': 'Pruebas',
                'description': 'Realizar pruebas y corregir errores.',
                'time': '1 semana'
            }
        ]
    }

    return Response(plan)