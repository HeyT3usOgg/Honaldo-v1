import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import sys
import os

ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.i_v = []
janela.title("Honaldo v1")
janela.geometry("800x1000")


def p_caminho(arquivo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, arquivo)
    else:
        BASE = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(BASE, arquivo) 
    

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
    butcher = None

i_do = p_caminho("Midia/Sound/Musica/I_DO.ogg")
i_do_l = p_caminho("Midia/Sound/Musica/I_DO.txt")
try:
    i_do_c = i_do
except Exception:
    i_do = None

infeliz = p_caminho("Midia/Sound/Musica/INFELIZ.ogg")
infeliz_l = p_caminho("Midia/Sound/Musica/INFELIZ.txt")
try:
    infeliz_c = infeliz
except Exception:
    infeliz = None

looping = p_caminho("Midia/Sound/Musica/LOOPING_THE_ROOMS_Teto.ogg")
looping_l = p_caminho("Midia/Sound/Musica/LOOPING_THE_ROOMS_Teto.txt")
try:
    looping_c = looping
except Exception:
    looping = None

machine = p_caminho("Midia/Sound/Musica/MACHINE_LOVE.ogg")
machine_l = p_caminho("Midia/Sound/Musica/MACHINE_LOVE.txt")
try:
    machine_c = machine
except Exception:
    machine = None

mesmerizer = p_caminho("Midia/Sound/Musica/MESMERIZER.ogg")
mesmerizer_l = p_caminho("Midia/Sound/Musica/MESMERIZER.txt")
try:
    mesmerizer_c = mesmerizer
except Exception:
    mesmerizer = None

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
    janela.Nat1 = ImageTk.PhotoImage(nat_r)
    Nat1 = janela.Nat1
except Exception:
    Nat1 = None

Fuck_c = p_caminho("Midia/Image/FuckYou/fuck_you.png")
try:
    fuck_o = Image.open(Fuck_c)
    fuck_r = fuck_o.resize((150,150), Image.Resampling.LANCZOS)
    janela.Fuck1 = ImageTk.PhotoImage(fuck_r)
    Fuck1 = janela.Fuck1
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

    elif texto_d =="clear" in texto_d:
        a_chat.config(state=tk.NORMAL)
        a_chat.delete("1.0", tk.END)
        a_chat.config(state=tk.DISABLED)

    elif texto_d == "teto":
        a_chat.insert(ctk.END, "Honaldo: Teto!\n", "bot")
        c_teto = random.choice(teto_m)
        while hasattr(janela, 'ultimo_teto') and c_teto == janela.ultimo_teto and len(teto_m) > 1:
            c_teto = random.choice(teto_m)
        janela.ultimo_teto = c_teto
        if os.path.exists(c_teto):
            try:
                i_teto = Image.open(c_teto)
                im_teto = i_teto.resize((150, 150), Image.Resampling.LANCZOS)
                n_v = ImageTk.PhotoImage(im_teto)
                janela.i_v.append(n_v)
                a_chat.image_create(ctk.END, image=n_v)
                a_chat.insert(ctk.END, "\n\n")
            except Exception as e:
                print()

    elif texto_d == "posso te comer?":
        a_chat.insert(ctk.END, "Honaldo: ...\n\n", "bot")
        if Nat1:
            a_chat.image_create(ctk.END, image=Nat1) 
            a_chat.insert(ctk.END, "\n\n")

    elif texto_d == "oi":
        a_chat.insert(ctk.END, "Honaldo: Fale!\n\n", "bot")

    elif texto_d == "sarve":
        a_chat.insert(ctk.END, "Honaldo: Sarve!\n\n", "bot")

    elif texto_d == "qual é sua versão?":
        a_chat.insert(ctk.END, "Honaldo: Não sabe ser o nome da janela?\n\n", "bot")

    elif texto_d == "quem te fez?":
        a_chat.insert(ctk.END, "Honaldo: Um preguiçoso, maluco chamado T3us >:(\n\n", "bot")

    elif texto_d == "frase filosofica":
        frase = random.choice(texto_f) 
        a_chat.insert(ctk.END, f"Honaldo: {frase}\n\n", "bot")

    elif texto_d == "quem é você?":
        a_chat.insert(ctk.END, "Honaldo: Eu sou o Honaldo, não me faça perguntas, eu odeio o meu trabalho\n\n", "bot")

    elif texto_d == "tu é ruim":
        a_chat.insert(ctk.END, "Honaldo: Tomar no cu não quer né?\n\n", "bot")

    elif texto_d == "tu é um lixo":
        a_chat.insert(ctk.END, "Honaldo: \n\n", "bot")
        if Fuck1:
            a_chat.image_create(ctk.END, image=Fuck1) 
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

    elif texto_d == "birdbrain":
        a_chat.insert(ctk.END, "Honaldo: BIRDBRAIN!\n", "bot")
        pygame.mixer.music.load(birdbrain_c)
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


    a_chat.config(state=ctk.DISABLED)
    a_chat.yview(ctk.END)
    entrada_c.delete(0,ctk.END)


a_chat = tk.Text(janela, bd=0, bg="#242424", fg="white", 
                 insertbackground="white", highlightthickness=0, 
                 font=("Arial", 12), wrap=tk.WORD)
a_chat.config(state=tk.DISABLED)
a_chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

a_chat.tag_config("letra_musica", foreground="yellow", font=("Arial", 11, "italic"), justify="left")
a_chat.tag_config("usuario", foreground="blue")
a_chat.tag_config("bot", foreground="green")

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

janela.mainloop()