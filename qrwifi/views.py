from django.shortcuts import render
from django.http import HttpResponse
import qrcode


def inicio(request):
    return render(request,'index.html',context={})

def procesar_formulario(request):
    if request.method == 'GET':
        return render(request,'qr_generado.html',context={})
    
    elif request.method == 'POST':
        ssid = request.POST.get('ssid'),
        password = request.POST.get('password'),
        security = request.POST.get('secur'),# puede ser "WEP", "WPA" o "nopass"

        # Crear la cadena de texto para el código QR
        qr_data = "WIFI:S:{};T:{};P:{};;".format(ssid, security, password)

        # Crear el objeto QRCode
        qr = qrcode.QRCode(version=1, box_size=10, border=4)

        # Agregar los datos al objeto QRCode
        qr.add_data(qr_data)

        # Compilar el código QR
        qr.make(fit=True)

        # Crear una imagen del código QR
        img = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen en un archivo
        img.save("static/media/qr1.png")

        return render(request,'qr_generado.html',context={})
