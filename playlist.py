# Cadastrar informar o nome, combobox com os nomes dos artistas 
# e listbox com as musicas do artista selecio
# Consultar pelo nome e mostrar todas as musicas da playlist
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import artista as art
import album as alb
import musica as mus

class Playlist:

    def __init__(self, nome, musicas):
        self.__nome = nome

        self.__musicas = musicas

    def getNome(self):
        return self.__nome

    def getMusicas(self):
        return self.__musicas

    def addMusica(self, musica):
        self.__musicas.append(musica)

class LimiteCadastraPlaylist(tk.Toplevel):
    def __init__(self, controle, listaArtistas, listaMusicas):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameArtista.pack()
        self.frameMusicas.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome,text="Nome da playlist: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        #combobox para os nomes dos artistas
        self.labelArtista = tk.Label(self.frameArtista,text="Escolha o artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaArtistas

        self.labelMusicas = tk.Label(self.frameMusicas,text="Escolha as músicas: ")
        self.labelMusicas.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMusicas)
        self.listbox.pack(side="left")
        for mus in listaMusicas:
            self.listbox.insert(tk.END, mus)
        
        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Música")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Playlist")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)    

class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x300')
        self.title("Consulta Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
        
      
        self.labelNome = tk.Label(self.frameNome,text="Nome da Playlist: ")
        self.labelNome.pack(side="left")
    

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaPlaylist)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)        

class LimiteMostraPlaylist():
    def __init__(self, str):
        messagebox.showinfo('Playlist', str)

class CtrlPlaylist():    
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaMusicasPlaylist = []
        self.listaMusicas = []

        if(not os.path.isfile("playlist.pickle")):
            self.listaPlaylist =  []
        else:
            with open("playlist.pickle", "rb") as f:
                self.listaPlaylist = pickle.load(f)

    def salvaPlaylist(self):
        if len(self.listaPlaylist) != 0:
            with open("playlist.pickle","wb") as f:
                pickle.dump(self.listaPlaylist, f)
    
    def conPlaylist(self):
        self.limiteIns = LimiteConsultaPlaylist(self) 
    
    def getPlaylist(self, nome):
        playRet = None
        for play in self.listaPlaylist:
            if play.getNome() == nome:
                playRet = play
        return playRet
    
    #nomes de todas plays
    def getListaNomePlays(self):
        nomes = []
        for play in self.listaPlaylist:
            nomes.append(play.getNome())
        return nomes
    
    #chama a interface para criar a playlist
    def inserePlaylist(self):        
        self.listaMusicasPlaylist = []
        nomesArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomes()
        self.listaMusicas = self.ctrlPrincipal.ctrlArtista.getMusicasArtista()
        self.limiteIns = LimiteCadastraPlaylist(self, nomesArtistas, self.listaMusicas)
    
    def criaPlaylist(self, event):
        nomePlay = self.limiteIns.inputNome.get()
        #artSel = self.limiteIns.escolhaCombo.get()
        #art = self.ctrlPrincipal.ctrlArtista.getArtista(artSel)
        playlist = Playlist(nomePlay, self.listaMusicasPlaylist)
        self.listaPlaylist.append(playlist)
        self.limiteIns.mostraJanela('Sucesso', 'Playlist criada com sucesso')
        self.limiteIns.destroy()
    
    def consultaPlaylist(self, event):
        nomePl2 = self.limiteIns.inputNome.get()
        nomePl = self.ctrlPrincipal.ctrlPlaylist.getPlaylist(nomePl2)
        str = ''

        if nomePl in self.getListaNomePlays():
            playlist = self.getPlaylist(nomePl)
            
            str = 'Playlist: ' + nomePl + '\n'
            str += 'Músicas: ' + '\n'
            for mus in playlist.getMusicas():
                str += mus.getNomeMusica() + '    ' + mus.getArtista().getNome()+'\n'
        
        self.limiteLista = LimiteMostraPlaylist(str)
    
    def insereMusica(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        musica = self.ctrlPrincipal.ctrlMusica.getMusica(musicaSel)
        self.listaMusicasPlaylist.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Musica adicionada')
        self.limiteIns.listbox.delete(tk.ACTIVE)
    
    def mostraPlaylist(self):
        str = ''
        for play in self.listaPlaylist:
            str += 'Nome: ' + play.getNome() + '\n'
            str += 'Musicas:\n'
            for musi in play.getMusicas():
                str += musi.getNomeMusica() + '\n'
            str += '------\n'

        self.limiteLista = LimiteMostraPlaylist(str)