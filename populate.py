import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'proyecto.settings')

import django
django.setup()
from aplicacion.models import *
def populate():

    medico1= medico.objects.get_or_create(id=1001, nombreM="medico1")[0]
    medico1.save()
    medico2 = medico.objects.get_or_create(id=1002, nombreM="medico2")[0]
    medico2.save()
    medico3 = medico.objects.get_or_create(id=1003, nombreM="medico3")[0]
    medico3.save()
    medico4 = medico.objects.get_or_create(id=1004, nombreM="medico4")[0]
    medico4.save()


    paciente1 = paciente.objects.get_or_create(id=1001, nombreP="paciente1")[0]
    paciente1.save()
    paciente2 = paciente.objects.get_or_create(id=1002, nombreP="paciente2")[0]
    paciente2.save()

    receta1 = receta.objects.get_or_create(id=1001, idMedico=medico1, idPaciente=paciente1)[0]

    receta1 = receta.objects.get_or_create(id=1002, idMedico=medico2, idPaciente=paciente1)[0]

    receta1 = receta.objects.get_or_create(id=1003, idMedico=medico1, idPaciente=paciente2)[0]

    receta1 = receta.objects.get_or_create(id=1004, idMedico=medico2, idPaciente=paciente2)[0]

    receta1 = receta.objects.get_or_create(id=1005, idMedico=medico3, idPaciente=paciente2)[0]

if __name__ == '__main__':
    print('Starting app')
    populate()
