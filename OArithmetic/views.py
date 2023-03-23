from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def suma(request, num1, num2):
    suma = num1 + num2
    text = '<h1 style="color: #5f6062;">' + "La suma de " + str(num1) + " + " + str(num2) + " = %s" + '</h1>'
    return HttpResponse(text % suma)

def resta(request, num1, num2):
    resta = num1 - num2
    text = '<h1 style="color: #5f6062;">' + "La resta de " + str(num1) + " - " + str(num2) + " = %s" + '</h1>'
    return HttpResponse(text % resta)

def multiplicacion(request, num1, num2):
    producto = num1 * num2
    text = '<h1 style="color: #5f6062;">' + "La multiplicacion de " + str(num1) + " x " + str(num2) + " = %s" + '</h1>'
    return HttpResponse(text % producto)


