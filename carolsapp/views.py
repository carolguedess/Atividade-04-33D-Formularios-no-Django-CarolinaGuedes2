from django.shortcuts import render,redirect
from .models import sucessos,transformacao

# Create your views here.
def home(request):
  Sucessos=sucessos.objects.all()
  transformation=transformacao.objects.all()
  return render(request, "home.html", context={"Sucessos":Sucessos, "transformation":transformation})

def create_sucesso(request):
  if request.method=="POST":
    sucessos.objects.create(
      title= request.POST["title"],
      peças= request.POST["peças"],
      estampa= request.POST["estampa"],
      genre= request.POST["genre"],
    )

    return redirect('home')
  return render(request,"forms.html", context={"action":"Adicionar"})

def update_sucesso(request,id):
  sucesso= sucessos.objects.get(id=id)
  if request.method=="POST":
    sucesso.title= request.POST["title"]
    sucesso.peças= request.POST["peças"]
    sucesso.estampa= request.POST["estampa"]
    sucesso.genre= request.POST["genre"]
    sucesso.save()

    return redirect('home')
  return render(request,"forms.html",context={"action":"Atualizar","sucesso":sucesso})

def delete_sucesso(request,id):
  sucesso= sucessos.objects.get(id=id)
  if request.method=="POST":
    if "confirm" in request.POST:
      sucesso.delete()

    return redirect('home')
  return render(request,"are_you_sure.html",context={"sucesso":sucesso})

def create_transformacao(request):
  if request.method=="POST":
    transformacao.objects.create(
      title= request.POST["title"],
      frequencia= request.POST["frequencia"],
      ano= request.POST["ano"],
    )

    return redirect('home')
  return render(request,"forms.html", context={"action":"Adicionar"})

def update_transformacao(request,id):
  transformacoes= transformacao.objects.get(id=id)
  if request.method=="POST":
    transformacoes.title= request.POST["title"]
    transformacoes.frequencia= request.POST["frequencia"]
    transformacoes.ano= request.POST["ano"]
    transformacoes.save()

    return redirect('home')
  return render(request,"forms.html",context={"action":"Atualizar","transformacao":transformacao})

def delete_transformacao(request,id):
  transformacoes= transformacao.objects.get(id=id)
  if request.method=="POST":
    if "confirm" in request.POST:
     transformacoes.delete()

    return redirect('home')
  return render(request,"are_you_sure.html",context={"transformacao":transformacao})