from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Table,TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors



from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from unidorg.models import UnidOrg

from unidorg.api.serializers import UnidOrgSerializer


class UnidOrgApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = UnidOrgSerializer

    queryset = UnidOrg.objects.filter(uorgtdescrip__contains='OFICINA DE RECURSOS HUMANOS')

    #queryset = UnidOrg.objects.all()

    # Filtros
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields=['uorgtdescrip']


class ReporteView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UnidOrgSerializer


    def cabecera(self, pdf):

        # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        # Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"PYTHON PIURA")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE PERSONAS")


    def get(self, request,pk):


        idUnidOrg=str(pk).zfill(5)

        print("id: ",idUnidOrg)

        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 650
        self.tabla(pdf, y, idUnidOrg)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y,pk):
        # Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Codigo', 'Descripcion', 'Sigla', 'Fecha Registro')
        # Creamos una lista de tuplas que van a contener a las personas

        detalles = [(uorg.uorgccod, uorg.uorgtdescrip, uorg.uorgtsigla, uorg.uorgffechreg) for uorg in
                   UnidOrg.objects.filter(uorgccod=pk)]

        # Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
        # Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                # La primera fila(encabezados) va a estar centrada
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                # Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                # El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        # Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        # Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60, y)
