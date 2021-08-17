#cadastrar apenas pelo nome
# consulta pelo nome e mostra todos os albuns do artista e todas as faixas de cada album
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Artista:

    def __init__(self, nome):
        self.__nome = nome

        self.__albuns = []
        self.__musicas = []

    def getNome(self):
        return self.__nome

    def getAlbuns(self):
        return self.__albuns

    def getMusicas(self):
        return self.__musicas        

    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)

class LimiteCadastraArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome,text="Nome do artista: ")
        self.labelNome.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Consulta artista")
        self.controle = controle

        self.frameNome2 = tk.Frame(self)
        self.frameButton2 = tk.Frame(self)
        self.frameNome2.pack()
        self.frameButton2.pack()

        self.labelNome2 = tk.Label(self.frameNome2,text="Nome do artista: ")
        self.labelNome2.pack(side="left")

        self.inputNome2 = tk.Entry(self.frameNome2, width=20)
        self.inputNome2.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton2 ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaHandler)

class LimiteMostraArtista():
    def __init__(self, str):
        messagebox.showinfo('Artista', str)

class CtrlArtista():       
    def __init__(self):
        #albuns do artista
        self.listaAlbuns = []
        #faixas do artista
        self.faixas = []

        if not os.path.isfile("artista.pickle"):
            self.listaArtistas =  []
        else:
            with open("artista.pickle", "rb") as f:
                self.listaArtistas = pickle.load(f)

    def salvaArtista(self):
        if len(self.listaArtistas) != 0:
            with open("artista.pickle","wb") as f:
                pickle.dump(self.listaArtistas, f)
    
    #para pegar o nome do artista
    def getArtista(self, nome):
        artRet = None
        for art in self.listaArtistas:
            if art.getNome() == nome:
                artRet = art
        return artRet
    
    #coloca o nome de todos os artistas em uma lista
    def getListaNomes(self):
        listaNomes = []
        for art in self.listaArtistas:
            listaNomes.append(art.getNome())
        return listaNomes
    
    #para pegar o nome do album
    def getAlbum(self):
        for alb in self.listaAlbuns:
            return alb.getNome()

    #pega as musicas do artista
    def getMusicasArtista(self):
        musicasArtista = []
        for art in self.listaArtistas:
            musicasArtista.append(art.getMusicas())
        return musicasArtista
    
    #chama a interface para cadastrar o artista
    def insereArtista(self):
        self.limiteInsere = LimiteCadastraArtista(self)
    
    def conArtista(self):
        self.limiteIns = LimiteConsultaArtista(self) 
    
    #cadastra o artista
    def enterHandler(self, event):
        nome = self.limiteInsere.inputNome.get()
        artista = Artista(nome)
        self.listaArtistas.append(artista)
        self.limiteInsere.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteInsere.inputNome.delete(0, len(self.limiteInsere.inputNome.get()))
    
    def fechaHandler(self, event):
        self.limiteInsere.destroy()

    #chama a interface para consultar o artista
    def mostraArtista(self):       
        self.limiteIns = LimiteConsultaArtista(self)
    
    #consulta o artista
    def consultaHandler(self, event):
        nome2 = self.limiteIns.inputNome2.get()
        str = ''

        if nome2 in self.getListaNomes():
            artista = self.getArtista(nome2)

        for art in self.listaArtistas:
            if art.getNome() == nome2:
                str = 'Nome: ' + artista.getNome() +'\n'
                for alb in artista.getAlbuns():
                    str += 'Album: ' + alb.getTitulo() + '\n'
                    str += 'Faixas: ' + '\n'
                    for mus in alb.getFaixas():
                        str += mus.getNomeMusica() + '\n'
            
        self.LimiteLista = LimiteMostraArtista(str)
                    
        

        #str += '\nAlbum\n'
        #pegar o nome do album
        #for alb in self.listaAlbuns:
        #    str += alb.getAlbum()
        #    str += '\nMúsicas\n'
        #    #pegar musicas em cada album
        #    for mus in self.faixas:
        #        #ver se a musica está dentro do album
        #        if mus.getTitulo() in self.listaAlbuns:
        #            str += mus.getTitulo() + '\n'
            
            
        
        


