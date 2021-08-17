#cadastrar album título, artista, ano e incluir todas as faixas
# consultar o album por nome e mostrar todas as faixas dele
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import artista as art
import musica as mus

class Album:

    def __init__(self, titulo, artista, ano, faixas):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = faixas

        self.__artista.addAlbum(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAno(self):
        return self.__ano

    def getFaixas(self):
        return self.__faixas        

    def addFaixa(self, musica):
        self.__faixas.append(musica)

class LimiteCadastraAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Album")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameFaixas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameFaixas.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo,text="Título do álbum: ")
        self.labelTitulo.pack(side="left")
        self.labelArtista = tk.Label(self.frameArtista,text="Nome do artista: ")
        self.labelArtista.pack(side="left")
        self.labelAno = tk.Label(self.frameAno,text="Ano do álbum: ")
        self.labelAno.pack(side="left")
        self.labelFaixas = tk.Label(self.frameFaixas,text="Faixas do álbum: ")
        self.labelFaixas.pack(side="left")

        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
        self.inputArtista = tk.Entry(self.frameArtista, width=20)
        self.inputArtista.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")
        self.inputFaixas = tk.Entry(self.frameFaixas, width=200)
        self.inputFaixas.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Música")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cria Albúm")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Consulta álbum")
        self.controle = controle

        self.frameNome2 = tk.Frame(self)
        self.frameButton2 = tk.Frame(self)
        self.frameNome2.pack()
        self.frameButton2.pack()

        self.labelNome2 = tk.Label(self.frameNome2,text="Nome do álbum: ")
        self.labelNome2.pack(side="left")

        self.inputNome2 = tk.Entry(self.frameNome2, width=20)
        self.inputNome2.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton2 ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaHandler)

class LimiteMostraAlbum():
    def __init__(self, str):
        messagebox.showinfo('Album', str)

class CtrlAlbum():
    def __init__(self, controlePrincipal):
        self.CtrlPrincipal = controlePrincipal
        self.artista = []
        self.faixasAlbum = []

        if not os.path.isfile("album.pickle"):
            self.listaAlbuns =  []
        else:
            with open("album.pickle", "rb") as f:
                self.listaAlbuns = pickle.load(f)

    def salvaAlbum(self):
        if len(self.listaAlbuns) != 0:
            with open("album.pickle","wb") as f:
                pickle.dump(self.listaAlbuns, f)
    
    #para pegar o nome do album
    def getAlbum(self, nome):
        albRet = None
        for alb in self.listaAlbuns:
            if alb.getTitulo() == nome:
                albRet = alb
        return albRet
    
    #para pegar o artista do album
    def getArtista(self):
        for alb in self.listaAlbuns:
            return alb.getArtista()
    
    #para pegar o ano do album
    def getAno(self):
        for alb in self.listaAlbuns:
            return alb.getAno()

    #para pegar as musicas do album
    def getMusicasAlbum(self):
        musAlbum = []
        for nom in self.faixasAlbum:
            #if nom.getTitulo() in self.listaAlbuns:
            musAlbum.append(nom)
        return musAlbum
    
    def getNomesAlbuns(self):
        nomes = []
        for alb in self.listaAlbuns:
            nomes.append(alb.getTitulo())
        return nomes
    
    #coloca o nome de todos as musicas em uma lista
    def getListaMusicas(self):
        listaMusicas = []
        for mus in self.faixasAlbum:
            listaMusicas.append(mus.getTitulo())
        return listaMusicas

    
    def addFaixa(self, titulo, artista):
        for art in self.artista:
            #art = artista        
        #nroFaixa = len(self.faixas)
        #musica = Musica(titulo, artista, self, nroFaixa)
            art.faixas.append(titulo)
    
    #add album na lista de albuns do artista
    def addAlbum(self, artista, titulo):
        self.albunsArtista = []
        listaArtistas = []
        listaArtistas = self.CtrlPrincipal.CtrlArtista.getListaNomes()
        for art in listaArtistas:
            if art.getNome() == artista:
                art = artista
                art.self.albunsArtista.append(titulo)
        #artAux.albuns.append(titulo)
    
    #chama a interface para cadastrar o album
    def insereAlbum(self):
        self.faixasAlbum = []
        self.limiteIns = LimiteCadastraAlbum(self)
    
    #chama a interface para consultar album
    def conAlbum(self):
        self.limiteIns = LimiteConsultaAlbum(self)
    
    #para inserir musicas no album
    def insereMusica(self, event):
        musica2 = self.limiteIns.inputFaixas.get()
        musica = self.CtrlPrincipal.ctrlMusica.getMusica(musica2)
        self.faixasAlbum.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Musica adicionada')
        self.limiteIns.inputFaixas.delete(0, len(self.limiteIns.inputFaixas.get()))

    #cadastra o album
    def enterHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        artista2 = self.limiteIns.inputArtista.get()
        artista = self.CtrlPrincipal.ctrlArtista.getArtista(artista2)
        ano = self.limiteIns.inputAno.get()
        album = Album(titulo, artista, ano, self.faixasAlbum)
        self.listaAlbuns.append(album)
        self.limiteIns.mostraJanela('Sucesso', 'Álbum cadastrado com sucesso')
        self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputArtista.delete(0, len(self.limiteIns.inputArtista.get()))
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        self.limiteIns.inputFaixas.delete(0, len(self.limiteIns.inputFaixas.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()
    
    def consultaHandler(self, event):
        nome2 = self.limiteIns.inputNome2.get()
        str = ''

        if nome2 in self.getNomesAlbuns():
            album = self.getAlbum(nome2)

            str = 'Album: ' + nome2 + '\n'
            str += 'Músicas: ' + '\n'
            for mus in album.getFaixas():
                str += mus.getNomeMusica() + '\n'
        
        self.LimiteLista = LimiteMostraAlbum(str)



        
        #for alb in self.listaAlbuns:
        #    if alb.getTitulo() == nome2:
        #        str += 'Título: ' + alb.getTitulo() + '\n'
        #        str += 'Faixas:\n'
        #        for mus in alb.getFaixas():
        #            str += mus.getNomeMusica() + '\n'
        
        
        
        

        