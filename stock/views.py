from django.shortcuts import redirect, render
import datetime
from .models import  ArticuloFarmacia, ArticuloFarmaciaLiquido
from .forms import FormularioFarmacia, FormularioCreacion

def farmacia(request):
    if request.user.username == "alejandro":
        articulos=ArticuloFarmacia.objects.order_by("nombreArticulo")

        fechaActual=datetime.date.today()

        return render(request, 'stock/stock.html', {"articulos" : articulos,  "fecha" : fechaActual})
    
    else:
        return redirect("/login/login")

def farmaciaLiquido(request):
    if request.user.username == "alejandro":
        
        articulosLiq=ArticuloFarmaciaLiquido.objects.order_by("nombreArticulo")

        fechaActualLiq=datetime.date.today()

        return render(request, 'stock/stockLiquido.html', {"articulos" : articulosLiq,  "fecha" : fechaActualLiq})
    
    else:
        return redirect("/login/login")

def editLiquido(request, id):
    if request.user.username == "alejandro":
        articulosLiq = ArticuloFarmaciaLiquido.objects.get(id=id)
    
        form = FormularioFarmacia(request.POST or None)
        if form.is_valid():
        #el modelo

            ArticuloFarmaciaLiquido.objects.filter(id=id).update(fecharda=form.cleaned_data['fecha'], cantidad=form.cleaned_data['cantidad'])
        

            return redirect('/stock/liquidos/')

        return render(request, 'stock/edit.html', {'articulos' : articulosLiq, 'form' : form})

    else:
        return redirect("/login/login")

def edit(request, id):
    if request.user.username == "alejandro":
        articulos = ArticuloFarmacia.objects.get(id=id)
    
        form = FormularioFarmacia(request.POST or None)
        if form.is_valid():
            #el modelo

            ArticuloFarmacia.objects.filter(id=id).update(fecharda=form.cleaned_data['fecha'], cantidad=form.cleaned_data['cantidad'])
        

            return redirect('/stock/')

        return render(request, 'stock/edit.html', {'articulos' : articulos, 'form' : form})

    else:
        return redirect('/login/login')

def create(request):
    if request.user.username == "alejandro":
        if request.method=='POST':

            form=FormularioCreacion(request.POST)

            if form.is_valid():
            
                nuevoArticulo= ArticuloFarmacia()#el modelo

                nuevoArticulo.nombreArticulo=form.cleaned_data['nombreArticulo']
                nuevoArticulo.cantidad=form.cleaned_data['cantidad']
                nuevoArticulo.fecharda=form.cleaned_data['fecharda']
                nuevoArticulo.save()
            
            
            
                return redirect('/stock/')
            
        
        else:
            form = FormularioCreacion()

        return render(request, 'stock/create.html', {'form' : form})

    else:
        return redirect("/login/login")

def createLiquido(request):
    if request.user.username == "alejandro":
        if request.method=='POST':

            form=FormularioCreacion(request.POST)

            if form.is_valid():
            
                nuevoArticuloLiq= ArticuloFarmaciaLiquido()#el modelo

                nuevoArticuloLiq.nombreArticulo=form.cleaned_data['nombreArticulo']
                nuevoArticuloLiq.cantidad=form.cleaned_data['cantidad']
                nuevoArticuloLiq.fecharda=form.cleaned_data['fecharda']
                nuevoArticuloLiq.save()
            
            
            
                return redirect('/stock/liquidos/')
            
        
        else:
            form = FormularioCreacion()

        return render(request, 'stock/create.html', {'form' : form})

    else:
        return redirect("/login/login")


def delete(request, id):
    if request.user.username == "alejandro":
        articulo=ArticuloFarmacia.objects.get(id=id)

        articulo.delete()

        return redirect('/stock/')

    else:
        return redirect("/login/login")

def deleteLiquido(request, id):
    if request.user.username == "alejandro":
        articulo=ArticuloFarmaciaLiquido.objects.get(id=id)

        articulo.delete()

        return redirect('/stock/liquidos/')
    else:
        return redirect("/login/login")

