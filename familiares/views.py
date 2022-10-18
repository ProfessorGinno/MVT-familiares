from django.shortcuts import render
from .models import Familiares


def mostrar_familiares(request):
    familiar_1 = Familiares(nombre='Estefa',
                            edad=22,
                            fecha="2000-10-1",
                            correo='prueba@prueba.com'
                        )
    familiar_2 = Familiares(nombre='Sara',
                            edad=18,
                            fecha="2004-11-23",
                            correo='prueba1@prueba.com'
                        )
    familiar_3 = Familiares(nombre='Luisa',
                            edad=25,
                            fecha="1997-11-12",
                            correo='prueba2@prueba.com'
                        )
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()

    # familiares = {'familiar 1':familiar_1,
    #                 'familiar 2': familiar_2,
    #                 'familiar 3': familiar_3,
    # }
    familiares = Familiares.objects.all()

    return render(request, 'familiares/mostrar_familiares.html', {'familiares':familiares})