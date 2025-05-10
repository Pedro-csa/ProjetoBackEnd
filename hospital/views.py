from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.http import JsonResponse
from .models import *
from datetime import date,datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import traceback
import json


#Bloco Inicial
def adminlogin(request):

    error = ""
    
    if request.method == 'POST':
        usuario= request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user is not None:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        else:
            error = "yes"

    context = {'error': error}
    return render(request, 'login.html', context)

def Index(request):
    return render(request,'index.html')

def home(request):
    if not request.user.is_staff:
        return redirect('login_admin')

    total_medicos = Medico.objects.count()
    total_pacientes = Paciente.objects.count()
    total_consultas = Consulta.objects.count()

    context = {
        'total_medicos': total_medicos,
        'total_pacientes': total_pacientes,
        'total_consultas': total_consultas
    }

    return render(request, 'admin_home.html', context)

def Sobre(request):
    return render(request,'sobre.html')

def contato(request):
    if request.method == "POST":
        nome = request.POST.get('name')
        email = request.POST.get('email')
        print("Mensagem recebida de:", nome, email)
        return render(request, "contato.html", {'enviado': True})
    return render(request, "contato.html")

def Logout(request):
    logout(request)
    return redirect('index')

#Bloco do Médico
@csrf_exempt
def add_medico(request):
    if request.method == 'POST':
        try:
            if request.headers.get('Content-Type') == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST

            nome = data.get('nome')
            telefone = data.get('telefone')
            especialidade = data.get('especialidade')
            crm = data.get('crm')
            email = data.get('email')
            data_contratacao = data.get('data_contratacao')

            medico = Medico.objects.create(
                nome=nome,
                telefone=telefone,
                especialidade=especialidade,
                crm=crm,
                email=email,
                data_contratacao=data_contratacao
            )

            # Se for JSON, retorna JSON:
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'mensagem': 'Médico criado com sucesso', 'id': medico.id_medico}, status=201)

            # Se for formulário HTML, renderiza a página:
            return render(request, 'add_medico.html', {'error': 'no'})

        except Exception as e:
            print("Erro ao cadastrar médico:", e)
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'erro': 'Erro ao cadastrar médico'}, status=400)

            return render(request, 'add_medico.html', {'error': 'yes'})

    return render(request, 'add_medico.html')

def view_medico(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Medico.objects.all()
    d = {'doc':doc}
    return render(request,'view_medico.html', d)

def edit_medico(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    medico = get_object_or_404(Medico, id_medico=pid)

    if request.method == "POST":
        medico.nome = request.POST.get('nome')
        medico.crm = request.POST.get('crm')
        medico.email = request.POST.get('email')
        medico.telefone = request.POST.get('telefone')
        medico.especialidade = request.POST.get('especialidade')
        try:
            medico.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_medico.html', {'medico': medico, 'error': error})

def Delete_medico(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    
    try:
        medico = Medico.objects.get(id_medico=pid)
        medico.delete()
    except Medico.DoesNotExist:
        print(f"Médico com id {pid} não encontrado.")
    
    return redirect('view_medico')

#Bloco do Paciente
@csrf_exempt
def add_paciente(request):
    if not request.user.is_authenticated and request.content_type != 'application/json':
        return redirect('login')

    if request.method == 'POST':
        try:
            # Se o conteúdo for JSON, extraímos com json.loads
            if request.headers.get('Content-Type') == 'application/json':
                data = json.loads(request.body)
                nome = data.get('nome')
                data_nascimento = data.get('data_nascimento')
                cpf = data.get('cpf')
                telefone = data.get('telefone')
                email = data.get('email')
                endereco = data.get('endereco')
            else:
                # Caso contrário, tratamos como formulário
                nome = request.POST.get('nome')
                data_nascimento = request.POST.get('data_nascimento')
                cpf = request.POST.get('cpf')
                telefone = request.POST.get('telefone')
                email = request.POST.get('email')
                endereco = request.POST.get('endereco')

            # Cria o paciente
            paciente = Paciente.objects.create(
                nome=nome,
                data_nascimento=data_nascimento,
                cpf=cpf,
                telefone=telefone,
                email=email,
                endereco=endereco,
                data_cadastro=timezone.now()
            )

            # Resposta adequada conforme origem da requisição
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'mensagem': 'Paciente criado com sucesso', 'id': paciente.id_paciente}, status=201)
            else:
                return render(request, 'add_paciente.html', {'error': 'no'})

        except Exception as e:
            print("Erro ao cadastrar paciente:", e)
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'erro': 'Erro ao cadastrar paciente'}, status=400)
            return render(request, 'add_paciente.html', {'error': 'yes'})

    # GET: retorna normalmente a tela
    return render(request, 'add_paciente.html')

def view_paciente(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Paciente.objects.all()
    d = {'pat':pat}
    return render(request,'view_paciente.html', d)

def edit_paciente(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    paciente = get_object_or_404(Paciente,id_paciente=pid)

    if request.method == "POST":
        paciente.nome = request.POST.get('nome')
        paciente.telefone = request.POST.get('telefone')
        paciente.endereco = request.POST.get('endereco')
        paciente.email = request.POST.get('email')
        try:
            paciente.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_paciente.html', locals())

def Delete_Paciente(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    paciente = get_object_or_404(Paciente, id_paciente=pid)
    paciente.delete()
    return redirect('view_paciente')

@csrf_exempt
def get_paciente(request, pid):
    if request.method == 'GET':
        try:
            paciente = Paciente.objects.get(id_paciente=pid)
            dados = {
                'id': paciente.id_paciente,
                'nome': paciente.nome,
                'cpf': paciente.cpf,
                'email': paciente.email,
                'telefone': paciente.telefone,
                'endereco': paciente.endereco,
                'data_nascimento': paciente.data_nascimento.strftime('%Y-%m-%d'),
                'data_cadastro': paciente.data_cadastro.strftime('%Y-%m-%d %H:%M:%S') if paciente.data_cadastro else None
            }
            return JsonResponse(dados, status=200)
        except Paciente.DoesNotExist:
            return JsonResponse({'erro': 'Paciente não encontrado'}, status=404)
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

    
#Bloco da Consulta

def add_consulta(request):
    error = ""
    medicos = Medico.objects.all()
    pacientes = Paciente.objects.all()

    if request.method == 'POST':
        try:
            if request.headers.get('Content-Type') == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST

            id_medico = data.get('medico')
            id_paciente = data.get('paciente')
            data_str = data.get('data_consulta')
            hora_str = data.get('hora_consulta')
            descricao = data.get('descricao')

            data_hora = timezone.make_aware(datetime.strptime(f"{data_str} {hora_str}", "%Y-%m-%d %H:%M"))
            medico = get_object_or_404(Medico, id_medico=id_medico)
            paciente = get_object_or_404(Paciente, id_paciente=id_paciente)

            consulta = Consulta.objects.create(
                id_medico=medico,
                id_paciente=paciente,
                data_consulta=data_hora,
                descricao=descricao,
                status='Agendada'
            )

            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'mensagem': 'Consulta criada com sucesso', 'id': consulta.id_consulta}, status=201)

            error = "no"
        except Exception as e:
            print("Erro ao agendar consulta:", e)
            traceback.print_exc()
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'erro': 'Erro ao agendar consulta'}, status=400)
            error = "yes"

    return render(request, 'add_consulta.html', {'error': error, 'medicos': medicos, 'pacientes': pacientes})

def view_consulta(request):
    if not request.user.is_staff:
        return redirect('login')
    consultas = Consulta.objects.select_related('id_paciente', 'id_medico').all()
    return render(request, 'view_consulta.html', {'consultas': consultas})

def delete_consulta(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    consulta = get_object_or_404(Consulta, id_consulta=pid)
    consulta.delete()
    return redirect('view_consulta')