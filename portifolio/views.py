from django.shortcuts import render, redirect
from .sql import Habilidade, Projeto
from django.core.mail import EmailMessage
from django.conf import settings

def create_db () :
    Projeto.create_proj('HenriPDF', 'Projeto que permite concatenar e resumir PDFs com IA. Possui uma interface gráfica para seleção do PDF e para a visualização do resumo. Utiliza Python, Agno e Llama 3.3 (Ou outro de escolha).', 'https://github.com/HenriqueSM0/henri_pdf', 'https://youtu.be/BDJqZLmWmyA')
    Projeto.create_proj('ChatBot Agno', 'Projeto que usa Python, Agno e Llama 3.3 (Ou outro de escolha), e usa uma interface gráfica aonde é possível escrever um prompt e receber uma resposta do modelo.', 'https://github.com/HenriqueSM0/chatbot_llama', 'https://youtu.be/SvUgvgZShE0')

def home(request) :
    habs = Habilidade.get_habs()
    return render(request, 'home.html', {'habilidades':habs})

def proj_list (request) :
    projs = Projeto.get_projs()
    return render(request, 'projetos.html', {'projetos':projs})

def email (request) :
    if (request.method == 'POST') :
        nome = request.POST.get('name')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        texto = request.POST.get('text')
        message = EmailMessage(
            subject=assunto,
            body=f"{nome} :\n\n{texto}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
            reply_to=[email]
        ).send()
        if (message == 1) : return render(request, 'email.html', {'result':'e-mail enviado com sucesso!'})
        else : return render(request, 'email.html', {'result':'ocorreu um erro no envio do e-mail!'})
    return render(request, 'email.html')
    