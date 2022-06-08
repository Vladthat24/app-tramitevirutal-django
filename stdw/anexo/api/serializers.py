from rest_framework.serializers import ModelSerializer
from anexo.models import Anexo


class AnexoSerializers(ModelSerializer):
    class Meta:
        model = Anexo
        fields = ['idanexo'
                  'num_anexo'
                  'direc_ip'
                  'marctelf'
                  'model'
                  'estado'
                  'fechinstal'
                  'fechcambio'
                  'observ'
                  'fechreg']
