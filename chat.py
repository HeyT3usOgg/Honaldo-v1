import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import platform
import subprocess
import random
import time
import getpass
import pygame
import sys
import os

nome_usuario = getpass.getuser()
ctk.set_appearance_mode('dark')


def p_caminho(arquivo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, arquivo)
    else:
        BASE = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(BASE, arquivo) 
    
desktop = tk.Tk()
desktop.title(f"{nome_usuario}'s PC")
desktop.attributes('-fullscreen', True)

desktop.i_v = []

caminho_wall = p_caminho("Midia/Wallpaper/xp2.png")
original = Image.open(caminho_wall)

wall_redimensionado = original.resize((1920, 1080), Image.Resampling.LANCZOS)
desktop.wallpaper = ImageTk.PhotoImage(wall_redimensionado)

tela_desktop = tk.Canvas(desktop, highlightthickness=0)
tela_desktop.place(x=0, y=0, relwidth=1, relheight=1)
tela_desktop.create_image(0, 0, image=desktop.wallpaper, anchor="nw")

pygame.mixer.init()

Metal_c = p_caminho("Midia/Sound/Sons/metal_pipe.ogg")
try:
    Metal = pygame.mixer.Sound(Metal_c)
except Exception:
    Metal = None

ronaldo_c = p_caminho("Midia/Sound/Sons/ronaldo.ogg")
try:
    ronaldo = pygame.mixer.Sound(ronaldo_c)
except Exception:
    ronaldo = None



campeao_c = p_caminho("Midia/Sound/Sons/campeao.ogg")
try:
    campeao = pygame.mixer.Sound(campeao_c)
except Exception:
    campeao = None

Onimai_c = p_caminho("Midia/Sound/Sons/Onimai.ogg")
try:
    Onimai = pygame.mixer.Sound(Onimai_c)
except Exception:
    Onimai = None

mahiro1_c = p_caminho("Midia/Sound/Sons/mahiro_som1.ogg")
try:
    mahiro1 = pygame.mixer.Sound(mahiro1_c)
except Exception:
    mahiro1 = None

mahiro_2_c = p_caminho("Midia/Sound/Sons/mahiro2.ogg")
try:
    mahiro_2 = pygame.mixer.Sound(mahiro_2_c)
except Exception:
    mahiro_2 = None

get_to_me = p_caminho("Midia/Sound/Musica/GET_TO_ME.ogg")
get_to_me_l = p_caminho("Midia/Sound/Musica/GET_TO_ME.txt")
try:
    get_to_me_c = get_to_me
except Exception:
    get_to_me = None

birdbrain = p_caminho("Midia/Sound/Musica/BIRDBRAIN.ogg")
birdbrain_l = p_caminho("Midia/Sound/Musica/BIRDBRAIN.txt")
try:
    birdbrain_c = birdbrain
except Exception:
    birdbrain = None

butcher = p_caminho("Midia/Sound/Musica/BUTCHER_VANITY.ogg")
butcher_l = p_caminho("Midia/Sound/Musica/BUTCHER_VANITY.txt")
try:
    butcher_c = butcher
except Exception:
    butcher_c = None

i_do = p_caminho("Midia/Sound/Musica/I_DO.ogg")
i_do_l = p_caminho("Midia/Sound/Musica/I_DO.txt")
try:
    i_do_c = i_do
except Exception:
    i_do_c = None

infeliz = p_caminho("Midia/Sound/Musica/INFELIZ.ogg")
infeliz_l = p_caminho("Midia/Sound/Musica/INFELIZ.txt")
try:
    infeliz_c = infeliz
except Exception:
    infeliz_c = None

looping = p_caminho("Midia/Sound/Musica/LOOPING_THE_ROOMS_Teto.ogg")
looping_l = p_caminho("Midia/Sound/Musica/LOOPING_THE_ROOMS_Teto.txt")
try:
    looping_c = looping
except Exception:
    looping_c = None

machine = p_caminho("Midia/Sound/Musica/MACHINE_LOVE.ogg")
machine_l = p_caminho("Midia/Sound/Musica/MACHINE_LOVE.txt")
try:
    machine_c = machine
except Exception:
    machine_c = None

mesmerizer = p_caminho("Midia/Sound/Musica/MESMERIZER.ogg")
mesmerizer_l = p_caminho("Midia/Sound/Musica/MESMERIZER.txt")
try:
    mesmerizer_c = mesmerizer
except Exception:
    mesmerizer_c = None

Monitoring_J = p_caminho("Midia/Sound/Musica/MONITORING.J.ogg")
Monitoring_l_J = p_caminho("Midia/Sound/Musica/MONITORING.J.txt")
try:
    Monitoring_c = Monitoring_J
except Exception:
    Monitoring_c = None

Monitoring_E = p_caminho("Midia/Sound/Musica/MONITORING.E.ogg")
Monitoring_l_E = p_caminho("Midia/Sound/Musica/MONITORING.E.txt")
try:
    Monitoring_c = Monitoring_E
except Exception:
    Monitoring_c = None

teto_m = [
    p_caminho("Midia/Image/Teto/teto.png"),
    p_caminho("Midia/Image/Teto/teto2.png"),
    p_caminho("Midia/Image/Teto/teto3.png"),
    p_caminho("Midia/Image/Teto/teto4.png"),
    p_caminho("Midia/Image/Teto/teto5.png"),
]

help = p_caminho("Help/help.txt")

Nat_c = p_caminho("Midia/Image/Natsuki/natsuki.png")
try:
    nat_o = Image.open(Nat_c)
    nat_r = nat_o.resize((150,150), Image.Resampling.LANCZOS)
    desktop.Nat1 = ImageTk.PhotoImage(nat_r)
    Nat1 = desktop.Nat1
except Exception:
    Nat1 = None

campeao_c = p_caminho("Midia/Image/memes/campeao.png")
try:
    campeao_o = Image.open(campeao_c)
    campeao_r = campeao_o.resize((150,150), Image.Resampling.LANCZOS)
    desktop.campeao1 = ImageTk.PhotoImage(campeao_r)
    campeao1 = desktop.campeao1
except Exception:
    campeao1 = None

p_c = p_caminho("Midia/Image/memes/templet.png")
try:
    p_o = Image.open(p_c)
    p_r = p_o.resize((150,150), Image.Resampling.LANCZOS)
    desktop.p1 = ImageTk.PhotoImage(p_r)
    p1 = desktop.p1
except Exception:
    p1 = None

hipe_c = p_caminho("Midia/Image/memes/hipe2.png")
try:
    hipe_o = Image.open(hipe_c)
    hipe_r = hipe_o.resize((150,150), Image.Resampling.LANCZOS)
    desktop.hipe1 = ImageTk.PhotoImage(hipe_r)
    hipe1 = desktop.hipe1
except Exception:
    hipe1 = None

Fuck_c = p_caminho("Midia/Image/FuckYou/fuck_you.png")
try:
    fuck_o = Image.open(Fuck_c)
    fuck_r = fuck_o.resize((150,150), Image.Resampling.LANCZOS)
    desktop.Fuck1 = ImageTk.PhotoImage(fuck_r)
    Fuck1 = desktop.Fuck1
except Exception:
    Fuck1 = None

texto_f = [
    "Desista dos seus sonhos e morra",
    "Melhor um pau na mão do que um na bunda",
    "A vida é igual a um helicóptero, só que tu não sabe pilotar essa bomba",
    "                                                 -- Mudinho 2026",
    "Se você tentar falhar e conseguir, você descobriu o que é ser um sucesso no fracasso.",
    "Nunca deixe para amanhã o que você pode simplesmente não fazer nunca"
]

def mensagem(event=None):
    texto_d = entrada_c.get().strip().lower()

    if not texto_d:
        return
    
    a_chat.config(state=ctk.NORMAL)
    a_chat.insert(ctk.END, f"Tu: {entrada_c.get()}\n", "usuario")

    if texto_d == "help":
        if os.path.exists(help):
            with open(help, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "bot")

    elif "clear" in texto_d:
        a_chat.config(state=tk.NORMAL)
        a_chat.delete("1.0", tk.END)

    elif texto_d == "teto":
        a_chat.insert(ctk.END, "Honaldo: Teto!\n", "bot")
        c_teto = random.choice(teto_m)
        while hasattr(desktop, 'ultimo_teto') and c_teto == desktop.ultimo_teto and len(teto_m) > 1:
            c_teto = random.choice(teto_m)
        desktop.ultimo_teto = c_teto
        if os.path.exists(c_teto):
            try:
                i_teto = Image.open(c_teto)
                im_teto = i_teto.resize((150, 150), Image.Resampling.LANCZOS)
                n_v = ImageTk.PhotoImage(im_teto)
                janela.i_v.append(n_v)
                a_chat.image_create(tk.END, image=n_v)
                a_chat.insert(ctk.END, "\n\n")
            except Exception as e:
                print("ERRO:", e)

    elif texto_d == "posso te comer?":
        a_chat.insert(ctk.END, "Honaldo: ...\n\n", "bot")
        if Nat1:
            a_chat.image_create(tk.END, image=Nat1) 
            a_chat.insert(ctk.END, "\n\n")

    elif texto_d == "oi":
        a_chat.insert(ctk.END, "Honaldo: Fale!\n\n", "bot")

    elif texto_d == "sarve":
        a_chat.insert(ctk.END, "Honaldo: Sarve!\n\n", "bot")

    elif texto_d == "qual é sua versão?":
        a_chat.insert(ctk.END, "Honaldo: DESDA V1 OLHA PRO TITULO DA JANELA PORRA!\n\n", "bot")
        if hipe1:
                    a_chat.image_create(tk.END, image=hipe1) 
                    a_chat.insert(ctk.END, "\n\n")

    elif texto_d == "quem te fez?":
        a_chat.insert(ctk.END, "Honaldo: Um preguiçoso, maluco chamado T3us >:(\n\n", "bot")

    elif texto_d == "frase filosofica":
        frase = random.choice(texto_f) 
        a_chat.insert(ctk.END, f"Honaldo: {frase}\n\n", "bot")

    elif texto_d == "quem é você?":
        a_chat.insert(ctk.END, "Honaldo: Eu sou o Honaldo, não me faça perguntas, eu odeio o meu trabalho\n\n", "bot")

# v2

    elif texto_d == "posso falar com o seu criador?":
        a_chat.insert(ctk.END, "Honaldo: Acho melh-\n", "bot")
        
        def p2():
            a_chat.config(state=ctk.NORMAL)
            a_chat.insert(ctk.END, "T3us: Sarve! O que tu preci-\n", "t3us")
            a_chat.config(state=ctk.DISABLED)
            a_chat.yview(ctk.END)

        def p3():
            a_chat.config(state=ctk.NORMAL)
            a_chat.insert(ctk.END, "Honaldo: O que tu ta fazendo aqui?.\n\n", "bot")
            a_chat.config(state=ctk.DISABLED)
            a_chat.yview(ctk.END)

        def p4():
            a_chat.config(state=ctk.NORMAL)
            a_chat.insert(ctk.END, "T3us: Uai o cara me chamou aqui.\n", "t3us")
            a_chat.config(state=ctk.DISABLED)
            a_chat.yview(ctk.END)

        def p5():
            a_chat.config(state=ctk.NORMAL)
            a_chat.insert(ctk.END, "Honaldo: Foda-se irmão esse não é seu espaço!.\n\n", "bot")
            a_chat.config(state=ctk.DISABLED)
            a_chat.yview(ctk.END)

        def p6():
            a_chat.config(state=ctk.NORMAL)
            a_chat.insert(ctk.END, "T3us: MAS FUI EU QUE CRIEI O CODIGO.\n", "t3us")
            a_chat.config(state=ctk.DISABLED)
            a_chat.yview(ctk.END)

        def p7():
            a_chat.config(state=ctk.NORMAL)
            a_chat.insert(ctk.END, "Honaldo: E SOU EU QUEM RESPONDO!.\n\n", "bot")
            a_chat.config(state=ctk.DISABLED)
            a_chat.yview(ctk.END)

        def p8():
            a_chat.config(state=ctk.NORMAL)
            a_chat.insert(ctk.END, "T3us: EU NÃO VOU FICAR PUTO NÃO! Cade o T3us que tá fazendo o codigo?.\n", "t3us")
            a_chat.config(state=ctk.DISABLED)
            a_chat.yview(ctk.END)

        def p9():
                a_chat.config(state=ctk.NORMAL)
                a_chat.insert(ctk.END, "Eu?\n\n", "t3us")
                a_chat.config(state=ctk.DISABLED)
                a_chat.yview(ctk.END)

        def p10():
            a_chat.config(state=ctk.NORMAL)
            a_chat.insert(ctk.END, "T3us: Tu tem algum problema? Tu ta falando com tu mesmo e com o seu programa >:(\n", "t3us")
            a_chat.config(state=ctk.DISABLED)
            a_chat.yview(ctk.END)

        def p11():
                a_chat.config(state=ctk.NORMAL)
                a_chat.insert(ctk.END, "Eu não falo é nada...\n\n", "t3us")
                a_chat.config(state=ctk.DISABLED)
                a_chat.yview(ctk.END)

        desktop.after(800, p2)
        desktop.after(1600, p3)
        desktop.after(2400, p4)
        desktop.after(3200, p5)
        desktop.after(4000, p6)
        desktop.after(4800, p7)
        desktop.after(5600, p8)
        desktop.after(8000, p9)
        desktop.after(8800, p10)
        desktop.after(9600, p11)

    elif texto_d == "ei qual o nome daquele campeão que parece uma barata?":
            a_chat.insert(ctk.END, "Honaldo: Kha'zix\n", "bot")
            if campeao:
                campeao.play()
            if campeao1:
                a_chat.image_create(tk.END, image=campeao1) 
                a_chat.insert(ctk.END, "\n\n")

    elif texto_d == "qual é o sentido da vida?":
        a_chat.insert(ctk.END,
        "Honaldo: O sentido da vida não é um destino esperando para ser encontrado, mas algo que você constrói ao longo do caminho. Cada escolha molda quem você se torna, cada erro ensina uma lição diferente e cada pessoa que cruza sua vida deixa uma marca, por menor que seja. Não importa quantas vezes você caia o que realmente define sua história é a sua coragem de continuar caminhando, mesmo quando não existe garantia de que tudo vai dar certo. Talvez o verdadeiro significado seja transformar o tempo que recebemos em algo que valha a pena ser lembrado.\n\n",
        "bot"
        )

        def p2():
            a_chat.config(state=tk.NORMAL)
            a_chat.insert(ctk.END, "...\n\n", "bot")
            a_chat.config(state=tk.DISABLED)
            a_chat.yview(tk.END)

        def p3():
            a_chat.config(state=tk.NORMAL)
            a_chat.insert(ctk.END, "Dito isso...\n\n", "bot")
            a_chat.config(state=tk.DISABLED)
            a_chat.yview(tk.END)

        def p4():
            a_chat.config(state=tk.NORMAL)
            a_chat.insert(ctk.END, "Olha isso que eu desenhei :D:\n\n", "bot")

            janela.i_v.append(p1)
            a_chat.image_create(tk.END, image=p1)
            a_chat.insert(ctk.END, "\n\n")

            a_chat.config(state=tk.DISABLED)
            a_chat.yview(tk.END)

        desktop.after(24000, p2)
        desktop.after(28000, p3)
        desktop.after(30000, p4)


    elif texto_d == "tu é ruim":
        a_chat.insert(ctk.END, "Honaldo: Tomar no cu não quer né?\n\n", "bot")

    elif texto_d == "tu é um lixo":
        a_chat.insert(ctk.END, "Honaldo: \n\n", "bot")
        if Fuck1:
            a_chat.image_create(tk.END, image=Fuck1) 
            a_chat.insert(ctk.END, "\n\n")

    elif texto_d == "metal":
        a_chat.insert(ctk.END, "Honaldo: METAL PIPE!\n", "bot")
        if Metal:
            Metal.play()

    elif texto_d == "ronaldo":
        a_chat.insert(ctk.END, "Honaldo: O que ele disse?\n", "bot")
        if ronaldo:
            ronaldo.play()

    elif texto_d == "onimai":
        a_chat.insert(ctk.END, "Honaldo: onimai!\n", "bot")
        if Onimai:
            Onimai.play()

    elif texto_d == "mahiro":
        a_chat.insert(ctk.END, "Honaldo: :3\n", "bot")
        if mahiro1:
            mahiro1.play()

    elif texto_d == "mahiro2":
        a_chat.insert(ctk.END, "Honaldo: :>\n", "bot")
        if mahiro_2:
            mahiro_2.play()

    elif texto_d == "parar musica":
        pygame.mixer.music.stop()
        a_chat.insert(tk.END, "Honaldo: Já parei esse trem >:(\n\n", "bot")

    elif texto_d == "get to me":
        a_chat.insert(ctk.END, "Honaldo: Get To Me!\n", "bot")
        pygame.mixer.music.load(get_to_me_c)
        pygame.mixer.music.play()
        if os.path.exists(get_to_me_l):
            with open(get_to_me_l, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "letra_musica")

    elif texto_d == "monitoring":
        a_chat.insert(ctk.END, "Honaldo: Monitoring (JP)!\n", "bot")

        pygame.mixer.music.load(Monitoring_J)
        pygame.mixer.music.play()

        if os.path.exists(Monitoring_l_J):
            with open(Monitoring_l_J, "r", encoding="utf-8") as f:
                a_chat.insert(tk.END, f.read() + "\n\n", "letra_musica")

    elif texto_d == "monitoring em inglês":
        a_chat.insert(ctk.END, "Honaldo: Monitoring (EN)!\n", "bot")

        pygame.mixer.music.load(Monitoring_E)
        pygame.mixer.music.play()

        if os.path.exists(Monitoring_l_E):
            with open(Monitoring_l_E, "r", encoding="utf-8") as f:
                a_chat.insert(tk.END, f.read() + "\n\n", "letra_musica")

    elif texto_d == "birdbrain":
        a_chat.insert(ctk.END, "Honaldo: BIRDBRAIN!\n", "bot")
        pygame.mixer.music.load(birdbrain)
        pygame.mixer.music.play()
        if os.path.exists(birdbrain_l):
            with open(birdbrain_l, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "letra_musica")

    elif texto_d == "butcher":
        a_chat.insert(ctk.END, "Honaldo: BUTCHER!\n", "bot")
        pygame.mixer.music.load(butcher_c)
        pygame.mixer.music.play()
        if os.path.exists(butcher_l):
            with open(butcher_l, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "letra_musica")

    elif texto_d == "i do":
        a_chat.insert(ctk.END, "Honaldo: I DO!\n", "bot")
        pygame.mixer.music.load(i_do_c)
        pygame.mixer.music.play()
        if os.path.exists(i_do_l):
            with open(i_do_l, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "letra_musica")

    elif texto_d == "infeliz":
        a_chat.insert(ctk.END, "Honaldo: INFELIZ!\n", "bot")
        pygame.mixer.music.load(infeliz_c)
        pygame.mixer.music.play()
        if os.path.exists(infeliz_l):
            with open(infeliz_l, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "letra_musica")

    elif texto_d == "looping the rooms":
        a_chat.insert(ctk.END, "Honaldo: LOOPING THE ROOMS!\n", "bot")
        pygame.mixer.music.load(looping_c)
        pygame.mixer.music.play()
        if os.path.exists(looping_l):
            with open(looping_l, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "letra_musica")

    elif texto_d == "machine love":
        a_chat.insert(ctk.END, "Honaldo: MACHINE LOVE!\n", "bot")
        pygame.mixer.music.load(machine_c)
        pygame.mixer.music.play()
        if os.path.exists(machine_l):
            with open(machine_l, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "letra_musica")

    elif texto_d == "mesmerizer":
        a_chat.insert(ctk.END, "Honaldo: MESMERIZER!\n", "bot")
        pygame.mixer.music.load(mesmerizer_c)
        pygame.mixer.music.play()
        if os.path.exists(mesmerizer_l):
            with open(mesmerizer_l, "r", encoding="utf-8") as f:
                l_g = f.read()
                a_chat.insert(tk.END, l_g + "\n\n", "letra_musica")

    else:
        a_chat.insert(ctk.END, "Honaldo: Tá falando grego?\n\n", "bot")

    if texto_d != "falar com o seu criador?":
        a_chat.config(state=ctk.DISABLED)
        a_chat.yview(ctk.END)
        
    entrada_c.delete(0, ctk.END)

def abrir_janela():
    
    global janela, a_chat, entrada_c, frame_inferior, b_enviar

    janela = ctk.CTkToplevel(desktop)
    janela.i_v = []
    janela.title("Honaldo v2")
    janela.geometry("800x1000")

    a_chat = tk.Text(janela, bd=0, bg="#242424", fg="white", 
                 insertbackground="white", highlightthickness=0, 
                 font=("Arial", 12), wrap=tk.WORD)
    a_chat.config(state=tk.DISABLED)
    a_chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    a_chat.tag_config("letra_musica", foreground="yellow", font=("Arial", 11, "italic"), justify="left")
    a_chat.tag_config("usuario", foreground="blue")
    a_chat.tag_config("bot", foreground="green")
    a_chat.tag_config("t3us", foreground="yellow")

    frame_inferior = ctk.CTkFrame(janela, fg_color="transparent")
    frame_inferior.pack(fill=ctk.X, padx=10, pady=(50, 50))

    entrada_c = ctk.CTkEntry(frame_inferior, font=("Arial", 14), height=40)
    entrada_c.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=(0, 10))
    entrada_c.bind("<Return>", mensagem)

    b_enviar = ctk.CTkButton(frame_inferior, text="Manda", font=("Arial", 14), height=40, command=mensagem)
    b_enviar.pack(side=ctk.RIGHT)

    a_chat.config(state=ctk.NORMAL)
    a_chat.insert(ctk.END, "Digite 'help' para ver a lista de comandos.\n\n", "bot")
    a_chat.config(state=ctk.DISABLED)

    entrada_c.focus()

def explorador_lixeira():
    janela_lixeira = tk.Toplevel(desktop)
    janela_lixeira.title("")
    janela_lixeira.geometry("1920x800")

    lixeira_wall = p_caminho("Midia/Wallpaper/lixeira.png")
    bg_original = Image.open(lixeira_wall)
    bg_redimensionado = bg_original.resize((1920, 763), Image.Resampling.LANCZOS)
    janela_lixeira.bg_image = ImageTk.PhotoImage(bg_redimensionado)

    tela_janela = tk.Canvas(janela_lixeira, highlightthickness=0)
    tela_janela.place(x=0, y=0, relwidth=1, relheight=1)
    tela_janela.create_image(0, 0, image=janela_lixeira.bg_image, anchor="nw")

def explorador_meu_pc():
    janela_meu_pc = tk.Toplevel(desktop)
    janela_meu_pc.title("")
    janela_meu_pc.geometry("1920x800")

    meu_pc_wall = p_caminho("Midia/Wallpaper/my_computer.png")
    pc_original = Image.open(meu_pc_wall)
    pc_redimensionado = pc_original.resize((1920, 763), Image.Resampling.LANCZOS)
    janela_meu_pc.bg_image = ImageTk.PhotoImage(pc_redimensionado)

    tela_janela = tk.Canvas(janela_meu_pc, highlightthickness=0)
    tela_janela.place(x=0, y=0, relwidth=1, relheight=1)
    tela_janela.create_image(0, 0, image=janela_meu_pc.bg_image, anchor="nw")

    icone_documents = p_caminho("Midia/Icons/My_Documents.png")
    my_documents = Image.open(icone_documents)
    my_documents_r = my_documents.resize((64, 64), Image.Resampling.LANCZOS)
    janela_meu_pc.icone_doc_int = ImageTk.PhotoImage(my_documents_r)

    px1 = 250
    py1 = 200

    fundo_selecao1 = tela_janela.create_rectangle(
        px1 - 34, py1 - 34, px1 + 34, py1 + 34,
        outline="", fill="", width=1
    )

    icone_interno1 = tela_janela.create_image(px1, py1, image=janela_meu_pc.icone_doc_int)
    texto_interno1 = tela_janela.create_text(px1, py1 + 45, text="My Documents", fill="black", font=("Arial", 10, "bold"))

    def ao_entrar1(event):
        tela_janela.itemconfig(fundo_selecao1, fill="#0055ea", outline="#3399ff", stipple="gray50")

    def ao_sair1(event):
        tela_janela.itemconfig(fundo_selecao1, fill="", outline="", stipple="")

    for elemento in (fundo_selecao1, icone_interno1, texto_interno1):
        tela_janela.tag_bind(elemento, "<Enter>", ao_entrar1)
        tela_janela.tag_bind(elemento, "<Leave>", ao_sair1)
        tela_janela.tag_bind(elemento, "<Button-1>", lambda event: explorador_meu_documento())

    icone_pictures = p_caminho("Midia/Icons/My_Pictures.png")
    my_pictures = Image.open(icone_pictures)
    my_pictures_r = my_pictures.resize((64, 64), Image.Resampling.LANCZOS)
    
    janela_meu_pc.icone_pic_int = ImageTk.PhotoImage(my_pictures_r)
        
    px2 = 350
    py2 = 200
        
    icone_interno2 = tela_janela.create_image(px2, py2, image=janela_meu_pc.icone_pic_int)
    texto_interno2 = tela_janela.create_text(px2, py2 + 45, text="My Pictures", fill="black", font=("Arial", 10, "bold"))

def spoiler():
    janela_spoiler = tk.Toplevel(desktop)
    janela_spoiler.title("")
    janela_spoiler.geometry("800x800")

    spoiler_wall = p_caminho("Midia/Wallpaper/spoiler.png")
    spoiler_original = Image.open(spoiler_wall)
    spoiler_redimensionado = spoiler_original.resize((800, 800), Image.Resampling.LANCZOS)
    janela_spoiler.bg_image = ImageTk.PhotoImage(spoiler_redimensionado)

    tela_spoiler = tk.Canvas(janela_spoiler, highlightthickness=0)
    tela_spoiler.place(x=0, y=0, relwidth=1, relheight=1)
    tela_spoiler.create_image(0, 0, image=janela_spoiler.bg_image, anchor="nw")

def segredo():
    janela_segredo = tk.Toplevel(desktop)
    janela_segredo.title("")
    janela_segredo.geometry("800x800")

    segredo_wall = p_caminho("Midia/Wallpaper/segredo.png")
    segredo_original = Image.open(segredo_wall)
    segredo_redimensionado = segredo_original.resize((800, 800), Image.Resampling.LANCZOS)
    janela_segredo.bg_image = ImageTk.PhotoImage(segredo_redimensionado)

    tela_segredo = tk.Canvas(janela_segredo, highlightthickness=0)
    tela_segredo.place(x=0, y=0, relwidth=1, relheight=1)
    tela_segredo.create_image(0, 0, image=janela_segredo.bg_image, anchor="nw")


def lindinhos():
    janela_l = tk.Toplevel(desktop)
    janela_l.title("")
    janela_l.geometry("1920x800")

    lixeira_wall = p_caminho("Midia/Wallpaper/l.png")
    l_original = Image.open(lixeira_wall)
    l_redimensionado = l_original.resize((1920, 763), Image.Resampling.LANCZOS)
    janela_l.bg_image = ImageTk.PhotoImage(l_redimensionado)

    tela_janela = tk.Canvas(janela_l, highlightthickness=0)
    tela_janela.place(x=0, y=0, relwidth=1, relheight=1)
    tela_janela.create_image(0, 0, image=janela_l.bg_image, anchor="nw")


def explorador_meu_documento():
    janela_meu_documento = tk.Toplevel(desktop)
    janela_meu_documento.title("")
    janela_meu_documento.geometry("1920x800")

    meu_documento_wall = p_caminho("Midia/Wallpaper/documentos.png")
    documento_original = Image.open(meu_documento_wall)
    documento_redimensionado = documento_original.resize((1920, 763), Image.Resampling.LANCZOS)
    janela_meu_documento.bg_image = ImageTk.PhotoImage(documento_redimensionado)

    tela_janela = tk.Canvas(janela_meu_documento, highlightthickness=0)
    tela_janela.place(x=0, y=0, relwidth=1, relheight=1)
    tela_janela.create_image(0, 0, image=janela_meu_documento.bg_image, anchor="nw")

    icone_documents = p_caminho("Midia/Icons/My_Documents.png")
    my_documents = Image.open(icone_documents)
    my_documents_r = my_documents.resize((64, 64), Image.Resampling.LANCZOS)
    janela_meu_documento.icone_doc_int = ImageTk.PhotoImage(my_documents_r)
    
    px1 = 250
    py1 = 200
    
    fundo_selecao1 = tela_janela.create_rectangle(
        px1 - 34, py1 - 34, px1 + 34, py1 + 34,
        outline="", fill="", width=1
    )
    
    icone_interno1 = tela_janela.create_image(px1, py1, image=janela_meu_documento.icone_doc_int)
    texto_interno1 = tela_janela.create_text(px1, py1 + 45, text="Honaldo v3", fill="black", font=("Arial", 10, "bold"))
    
    def ao_entrar1(event):
        tela_janela.itemconfig(fundo_selecao1, fill="#0055ea", outline="#3399ff", stipple="gray50")
    
    def ao_sair1(event):
        tela_janela.itemconfig(fundo_selecao1, fill="", outline="", stipple="")
    
    for elemento in (fundo_selecao1, icone_interno1, texto_interno1):
        tela_janela.tag_bind(elemento, "<Enter>", ao_entrar1)
        tela_janela.tag_bind(elemento, "<Leave>", ao_sair1)
        tela_janela.tag_bind(elemento, "<Button-1>", lambda event: spoiler())

    icone_documents2 = p_caminho("Midia/Icons/My_Documents.png")
    my_documents2 = Image.open(icone_documents2)
    my_documents_r2 = my_documents2.resize((64, 64), Image.Resampling.LANCZOS)
    janela_meu_documento.icone_doc_2 = ImageTk.PhotoImage(my_documents_r2)
    
    px2 = 350
    py2 = 200
    
    fundo_selecao2 = tela_janela.create_rectangle(
        px2 - 34, py2 - 34, px2 + 34, py2 + 34,
        outline="", fill="", width=1
    )
    
    icone_interno2 = tela_janela.create_image(px2, py2, image=janela_meu_documento.icone_doc_int)
    texto_interno2 = tela_janela.create_text(px2, py2 + 45, text="Lindinhos", fill="black", font=("Arial", 10, "bold"))
    
    def ao_entrar2(event):
        tela_janela.itemconfig(fundo_selecao2, fill="#0055ea", outline="#3399ff", stipple="gray50")
    
    def ao_sair2(event):
        tela_janela.itemconfig(fundo_selecao2, fill="", outline="", stipple="")
    
    for elemento in (fundo_selecao2, icone_interno2, texto_interno2):
        tela_janela.tag_bind(elemento, "<Enter>", ao_entrar2)
        tela_janela.tag_bind(elemento, "<Leave>", ao_sair2)
        tela_janela.tag_bind(elemento, "<Button-1>", lambda event: lindinhos())

    icone_documents = p_caminho("Midia/Icons/My_Documents.png")
    my_documents2 = Image.open(icone_documents2)
    my_documents_r2 = my_documents2.resize((64, 64), Image.Resampling.LANCZOS)
    janela_meu_documento.icone_doc_2 = ImageTk.PhotoImage(my_documents_r2)
    
    px3 = 450
    py3 = 200
    
    fundo_selecao3 = tela_janela.create_rectangle(
        px3 - 34, py3 - 34, px3 + 34, py3 + 34,
        outline="", fill="", width=1
    )
    
    icone_interno3 = tela_janela.create_image(px3, py3, image=janela_meu_documento.icone_doc_int)
    texto_interno3 = tela_janela.create_text(
    px3, py3 + 45, 
    text="250GB de fotos do astolfo", 
    fill="black", 
    font=("Arial", 10, "bold"),
    width=100,
    justify="center"
)
    
    def ao_entrar3(event):
        tela_janela.itemconfig(fundo_selecao3, fill="#0055ea", outline="#3399ff", stipple="gray50")
    
    def ao_sair3(event):
        tela_janela.itemconfig(fundo_selecao3, fill="", outline="", stipple="")
    
    for elemento in (fundo_selecao3, icone_interno3, texto_interno3):
        tela_janela.tag_bind(elemento, "<Enter>", ao_entrar3)
        tela_janela.tag_bind(elemento, "<Leave>", ao_sair3)
        tela_janela.tag_bind(elemento, "<Button-1>", lambda event: segredo())


#- campo

def campo():
    root = tk.Toplevel(desktop)
    root.title("")
    root.geometry("550x450")

    isgameover = False
    row = 10
    col = 10
    bomb = 10
    flags = bomb

    stack = []
    closed = []
    flag_map = []
    mfield = []
    
    global map

    fr_tbar = tk.LabelFrame(root)
    fr_tbar.grid(row=0, column=0, padx=10, pady=10)

    fr_game = tk.LabelFrame(root)
    fr_game.grid(row=1, column=0, padx=10, pady=5)

    fr_dbar = tk.LabelFrame(root)
    fr_dbar.grid(row=2, column=0, padx=10, pady=10)

    lab_flag = tk.Label(fr_tbar, text="Flags: --")
    lab_flag.grid(row=0, column=0)

    def click(index):
        nonlocal isgameover, flags
        if index in closed or isgameover or index in flag_map:
            return
        if map[index] == "b":
            lab_over = tk.Label(fr_dbar, text="Game Over! You lost", fg="red")
            lab_over.pack()
            game_over()
            return
        stack.append(index)
        while len(stack) > 0:
            cl_ind = stack[-1]
            cl_exam = examine(cl_ind)
            closed.append(cl_ind)
            stack.pop()
            if cl_exam == 0:
                for i in surrounding(cl_ind):
                    if i not in closed and i not in stack:
                        stack.append(i)
                mfield[cl_ind].config(bg="grey")
            else:
                mfield[cl_ind].config(text=str(cl_exam))
        for i in flag_map:
            if i in closed:
                mfield[i].config(text="   ", fg="black")
                flags += 1
                flag_map.remove(i)
        lab_flag.config(text="Flags: " + str(flags))
        if len(closed) == row * col - bomb:
            lab_over = tk.Label(fr_dbar, text="You Won!", fg="green")
            lab_over.pack()
            game_over()

    def surrounding(index):
        tst = []
        for c in [-col, 0, col]:
            if index + c < 0 or index + c >= row * col:
                continue
            for i in [-1, 0, 1]:
                if index // col != (index + i) // col:
                    continue
                tst.append(index + c + i)
        if index in tst:
            tst.remove(index)
        return tst

    def examine(index):
        tot = 0
        for i in surrounding(index):
            if map[i] == "b":
                tot += 1
        return tot

    def first_click(index):
        global map
        map = ["b" for i in range(bomb)] + ["" for i in range(row * col - bomb)]
        random.shuffle(map)
        while map[index] == "b":
            random.shuffle(map)
        for i in range(row * col):
            mfield[i].config(command=lambda x=i: click(x))
            mfield[i].bind('<Button-3>', lambda eff, x=i: rightclick(event=eff, index=x))
        lab_flag.config(text="Flags: " + str(flags))
        click(index)

    def game_over():
        nonlocal isgameover
        isgameover = True
        for i in range(row * col):
            if map[i] == "b":
                mfield[i].config(text="B", fg="red")

    def rightclick(event, index):
        nonlocal flags
        if index in closed or isgameover:
            return
        if index in flag_map:
            mfield[index].config(text="   ", fg="black")
            flags += 1
            flag_map.remove(index)
        elif flags > 0:
            mfield[index].config(text=" ! ", fg="blue")
            flags -= 1
            flag_map.append(index)
        lab_flag.config(text="Flags: " + str(flags))

    for i in range(row * col):
        btn = tk.Button(fr_game, text="   ", width=3, height=1, command=lambda x=i: first_click(x))
        btn.grid(row=i // col, column=i % col)
        mfield.append(btn)


#- idiot

def idiot():
    global rodando_trollagem
    rodando_trollagem = True

    janelas_abertas = []

    try:
        pygame.mixer.quit()
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            
        caminho_audio = p_caminho("Midia/Image/video/You.ogg") 
        print(f"[DEBUG ÁUDIO] Tentando carregar em: {caminho_audio}")
        
        pygame.mixer.music.load(caminho_audio)
        pygame.mixer.music.set_volume(1.0) 
        pygame.mixer.music.play(-1)        
        print("[DEBUG ÁUDIO] Música tocando com sucesso!")
    except Exception as e:
        print(f"[ERRO DE ÁUDIO] Não foi possível tocar: {e}")

    def criar_uma_janela():
        if not rodando_trollagem:
            return

        janela = tk.Toplevel(desktop)
        janela.title("You are an idiot!")
        janelas_abertas.append(janela)
        
        width = desktop.winfo_screenwidth()
        height = desktop.winfo_screenheight()
        
        # Posição inicial aleatória
        x = random.randint(0, max(100, width - 250))
        y = random.randint(0, max(100, height - 150))
        
        direcao = {'esq': random.choice([True, False]), 'cima': random.choice([True, False])}
        cor = {'bg': 'white', 'fg': 'black'}
        
        label = tk.Label(janela, text="You are an idiot!", font=("Arial", 16, "bold"))
        label.pack(expand=True, fill="both")
        
        def mover_e_piscar():
            nonlocal x, y
            
            if not rodando_trollagem:
                return

            try:
                if not janela.winfo_exists():
                    return
            except:
                return

            if x > width - 200:
                direcao['esq'] = True
            if x < 0:
                direcao['esq'] = False
                
            if y > height - 100:
                direcao['cima'] = True
            if y < 0:
                direcao['cima'] = False
                
            x += -18 if direcao['esq'] else 18
            y += -18 if direcao['cima'] else 18
            
            if cor['bg'] == "white":
                cor['bg'] = "black"
                cor['fg'] = "white"
            else:
                cor['bg'] = "white"
                cor['fg'] = "black"
                
            label.config(bg=cor['bg'], fg=cor['fg'])
            janela.config(bg=cor['bg'])
            
            janela.geometry(f"220x120+{x}+{y}")
            janela.after(20, mover_e_piscar)

        mover_e_piscar()

    max_janelas = 30
    contador_criacao = {'atual': 0}

    def gerar_multiplas():
        if not rodando_trollagem:
            return
            
        if contador_criacao['atual'] < max_janelas:
            criar_uma_janela()
            criar_uma_janela()
            contador_criacao['atual'] += 2

            desktop.after(600, gerar_multiplas)

    criar_uma_janela()
    gerar_multiplas()

    def encerrar_trollagem():
        global rodando_trollagem
        rodando_trollagem = False
        
        # Para a música
        try:
            pygame.mixer.music.stop()
            print("[DEBUG ÁUDIO] Música encerrada pelo timer de segurança.")
        except Exception as e:
            print(f"[ERRO AO PARAR ÁUDIO]: {e}")
            
        for j in janelas_abertas:
            try:
                j.destroy()
            except:
                pass
                
        print("[INFO] Timer de segurança acionado: Trolls limpos da tela!")

    desktop.after(12000, encerrar_trollagem)

icone_idiot = p_caminho("Midia/Icons/idiot.png")
idiot_o = Image.open(icone_idiot)
idiot_r = idiot_o.resize((64, 64), Image.Resampling.LANCZOS)
desktop.icone_idiot = ImageTk.PhotoImage(idiot_r)

pos_x6 = 60
pos_y6 = 660

fundo_selecao6 = tela_desktop.create_rectangle(
    pos_x6 - 34, pos_y6 - 34, pos_x6 + 34, pos_y6 + 34,
    outline="", fill="", width=1
)

icon_idiot_tela = tela_desktop.create_image(pos_x6, pos_y6, image=desktop.icone_idiot)
texto_idiot = tela_desktop.create_text(pos_x6, pos_y6 + 45, text="?", fill="white", font=("Arial", 10, "bold"))

def ao_entrar6(event):
    tela_desktop.itemconfig(fundo_selecao6, fill="#0055ea", outline="#3399ff", stipple="gray50")

def ao_sair6(event):
    tela_desktop.itemconfig(fundo_selecao6, fill="", outline="", stipple="")

for elemento in (fundo_selecao6, icon_idiot_tela, texto_idiot):
    tela_desktop.tag_bind(elemento, "<Enter>", ao_entrar6)
    tela_desktop.tag_bind(elemento, "<Leave>", ao_sair6)
    
    tela_desktop.tag_bind(elemento, "<Button-1>", lambda event: idiot())



azul_hover = Image.new("RGBA", (74, 74), (0, 85, 234, 100)) 
desktop.img_hover = ImageTk.PhotoImage(azul_hover)

invisivel = Image.new("RGBA", (74, 74), (255, 255, 255, 0))
desktop.img_vazia = ImageTk.PhotoImage(invisivel)
    
icone_lixeira = p_caminho("Midia/Icons/lixeira_xp.png")
img_lixeira = Image.open(icone_lixeira)
img_lixeira_r = img_lixeira.resize((64, 64), Image.Resampling.LANCZOS)
desktop.icone_lixeira = ImageTk.PhotoImage(img_lixeira_r)

windows_icon = p_caminho("Midia/Icons/xp_icon.png")
windows_icon_o = Image.open(windows_icon)
windows_icon_r = windows_icon_o.resize((24, 24), Image.Resampling.LANCZOS)
desktop.icone_start = ImageTk.PhotoImage(windows_icon_r)

pos_x = 60
pos_y = 60

fundo_selecao = tela_desktop.create_rectangle(
    pos_x - 34, pos_y - 34, pos_x + 34, pos_y + 34,
    outline="", fill="", width=1
)

icone_img_lixeira = tela_desktop.create_image(pos_x, pos_y, image=desktop.icone_lixeira)
icone_texto_lixeira = tela_desktop.create_text(pos_x, pos_y + 45, text="Recycle Bin", fill="white", font=("Arial", 10, "bold"))

def ao_entrar(event):
    tela_desktop.itemconfig(fundo_selecao, fill="#0055ea", outline="#3399ff", stipple="gray50")

def ao_sair(event):
    tela_desktop.itemconfig(fundo_selecao, fill="", outline="", stipple="")

for elemento in (fundo_selecao, icone_img_lixeira, icone_texto_lixeira):
    tela_desktop.tag_bind(elemento, "<Enter>", ao_entrar)
    tela_desktop.tag_bind(elemento, "<Leave>", ao_sair)
    tela_desktop.tag_bind(elemento, "<Button-1>", lambda event: explorador_lixeira())

icone_computer = p_caminho("Midia/Icons/my_computer.png")

my_computer = Image.open(icone_computer)
my_computer_r = my_computer.resize((64, 64), Image.Resampling.LANCZOS)
desktop.icone_computer = ImageTk.PhotoImage(my_computer_r)

pos_x2 = 60
pos_y2 = 180

fundo_selecao2 = tela_desktop.create_rectangle(
    pos_x2 - 34, pos_y2 - 34, pos_x2 + 34, pos_y2 + 34,
    outline="", fill="", width=1
)
icon_computer = tela_desktop.create_image(pos_x2, pos_y2, image=desktop.icone_computer)
texto_computer = tela_desktop.create_text(pos_x2, pos_y2 + 45, text="My Computer", fill="white", font=("Arial", 10, "bold"))

def ao_entrar2(event):
    tela_desktop.itemconfig(fundo_selecao2, fill="#0055ea", outline="#3399ff", stipple="gray50")

def ao_sair2(event):
    tela_desktop.itemconfig(fundo_selecao2, fill="", outline="", stipple="")

for elemento in (fundo_selecao2, icon_computer, texto_computer):
    tela_desktop.tag_bind(elemento, "<Enter>", ao_entrar2)
    tela_desktop.tag_bind(elemento, "<Leave>", ao_sair2)
    tela_desktop.tag_bind(elemento, "<Button-1>", lambda event: explorador_meu_pc())

icone_documents = p_caminho("Midia/Icons/My_Documents.png")
my_documents = Image.open(icone_documents)
my_documents_r = my_documents.resize((64, 64), Image.Resampling.LANCZOS)
desktop.icone_documents = ImageTk.PhotoImage(my_documents_r)

pos_x3 = 60
pos_y3 = 300

fundo_selecao3 = tela_desktop.create_rectangle(
    pos_x3 - 34, pos_y3 - 34, pos_x3 + 34, pos_y3 + 34,
    outline="", fill="", width=1
)
icon_documents = tela_desktop.create_image(pos_x3, pos_y3, image=desktop.icone_documents)
texto_documents = tela_desktop.create_text(pos_x3, pos_y3 + 45, text="My Documents", fill="white", font=("Arial", 10, "bold"))

def ao_entrar3(event):
    tela_desktop.itemconfig(fundo_selecao3, fill="#0055ea", outline="#3399ff", stipple="gray50")

def ao_sair3(event):
    tela_desktop.itemconfig(fundo_selecao3, fill="", outline="", stipple="")

for elemento in (fundo_selecao3, icon_documents, texto_documents):
    tela_desktop.tag_bind(elemento, "<Enter>", ao_entrar3)
    tela_desktop.tag_bind(elemento, "<Leave>", ao_sair3)
    tela_desktop.tag_bind(elemento, "<Button-1>", lambda event: explorador_meu_documento())

icone_campo = p_caminho("Midia/Icons/Minesweeper.png")
my_campo = Image.open(icone_campo)
my_campo_r = my_campo.resize((64, 64), Image.Resampling.LANCZOS)
desktop.icone_campo = ImageTk.PhotoImage(my_campo_r)

pos_x4 = 60
pos_y4 = 420

fundo_selecao4 = tela_desktop.create_rectangle(
    pos_x4 - 34, pos_y4 - 34, pos_x4 + 34, pos_y4 + 34,
    outline="", fill="", width=1
)
icon_campo = tela_desktop.create_image(pos_x4, pos_y4, image=desktop.icone_campo)
texto_campo = tela_desktop.create_text(pos_x4, pos_y4 + 45, text="Minesweeper", fill="white", font=("Arial", 10, "bold"))

def ao_entrar4(event):
    tela_desktop.itemconfig(fundo_selecao4, fill="#0055ea", outline="#3399ff", stipple="gray50")

def ao_sair4(event):
    tela_desktop.itemconfig(fundo_selecao4, fill="", outline="", stipple="")

for elemento in (fundo_selecao4, icon_campo, texto_campo):
    tela_desktop.tag_bind(elemento, "<Enter>", ao_entrar4)
    tela_desktop.tag_bind(elemento, "<Leave>", ao_sair4)
    tela_desktop.tag_bind(elemento, "<Button-1>", lambda event: campo())

icone_honaldo = p_caminho("Midia/Icons/iu_.png")
my_honaldo = Image.open(icone_honaldo)
my_honaldo_r = my_honaldo.resize((64, 64), Image.Resampling.LANCZOS)
desktop.icone_honaldo = ImageTk.PhotoImage(my_honaldo_r)

pos_x5 = 60
pos_y5 = 540

fundo_selecao5 = tela_desktop.create_rectangle(
    pos_x5 - 34, pos_y5 - 34, pos_x5 + 34, pos_y5 + 34,
    outline="", fill="", width=1
)
icon_honaldo = tela_desktop.create_image(pos_x5, pos_y5, image=desktop.icone_honaldo)
texto_honaldo = tela_desktop.create_text(pos_x5, pos_y5 + 45, text="Honaldo v2", fill="white", font=("Arial", 10, "bold"))

def ao_entrar5(event):
    tela_desktop.itemconfig(fundo_selecao5, fill="#0055ea", outline="#3399ff", stipple="gray50")

def ao_sair5(event):
    tela_desktop.itemconfig(fundo_selecao5, fill="", outline="", stipple="")

for elemento in (fundo_selecao5, icon_honaldo, texto_honaldo):
    tela_desktop.tag_bind(elemento, "<Enter>", ao_entrar5)
    tela_desktop.tag_bind(elemento, "<Leave>", ao_sair5)
    tela_desktop.tag_bind(elemento, "<Button-1>", lambda event: abrir_janela())

altura_barra = 40
y_barra = 1080 - altura_barra

barra_tarefas = tela_desktop.create_rectangle(
    0, y_barra, 1920, 1080,
    fill="#245edb", outline="#1c48a6", width=2
)

fundo_start = tela_desktop.create_rectangle(
    0, y_barra, 130, 1080,
    fill="#3c8b3c", outline="#2b6b2b", width=2
)

icone_bandeira = tela_desktop.create_image(30, y_barra + 20, image=desktop.icone_start)

texto_start = tela_desktop.create_text(
    75, y_barra + 20,
    text="start", fill="white", font=("Arial", 16, "bold", "italic")
)

texto_relogio = tela_desktop.create_text(
    1860, y_barra + 20, 
    text="00:00 AM", fill="white", font=("Arial", 11)
)

def atualizar_relogio():
    hora_atual = time.strftime("%I:%M %p")
    
    tela_desktop.itemconfig(texto_relogio, text=hora_atual)
    
    desktop.after(1000, atualizar_relogio)

atualizar_relogio()

janela_icon = tk.Button(desktop, text="Abrir", command=abrir_janela)
#janela_icon.place(x=30, y=30)

desktop.mainloop()