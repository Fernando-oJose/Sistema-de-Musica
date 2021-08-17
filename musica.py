import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Musica:

    def __init__(self, titulo, artista, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__nroFaixa = nroFaixa

        self.__faixas = []

        #artista.addMusica(self)

    def getNomeMusica(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    #def getAlbum(self):
    #    return self.__album
        
    def getNroFaixa(self):
        return self.__nroFaixa

class LimiteCadastraMusicas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('450x300')
        self.title("Musica")
        self.controle = controle

        
        self.frameTitulo = tk.Frame(self)
        self.frameNroFaixa = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameNroFaixa.pack()
        self.frameArtista.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.labelNroFaixa = tk.Label(self.frameNroFaixa,text="Nro Faixa: ")
        self.labelArtista = tk.Label(self.frameArtista,text="Artista: ")
        self.labelTitulo.pack(side="left")
        self.labelNroFaixa.pack(side="left")  
        self.labelArtista.pack(side="left")  

        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
        self.inputNroFaixa = tk.Entry(self.frameNroFaixa, width=20)
        self.inputNroFaixa.pack(side="left") 
        self.inputArtista = tk.Entry(self.frameArtista, width=20)
        self.inputArtista.pack(side="left") 

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg) 

class CtrlMusica():       
    def __init__(self, controlePrincipal):
        if not os.path.isfile("musica.pickle"):
            self.listaMusicas =  []
        else:
            with open("musica.pickle", "rb") as f:
                self.listaMusicas = pickle.load(f)

        self.ctrlPrincipal = controlePrincipal

    def salvaMusicas(self):
        if len(self.listaMusicas) != 0:
            with open("musica.pickle","wb") as f:
                pickle.dump(self.listaMusicas, f)

    def getMusica(self, nome):
        musRet = None
        for mus in self.listaMusicas:
            if mus.getNomeMusica() == nome:
                musRet = mus
        return musRet

    def getListaTitulos(self):
        listaTitulos = []
        for mus in self.listaMusicas:
            listaTitulos.append(mus.getNomeMusica())
        return listaTitulos

    def cadMusicas(self):
        self.limiteIns = LimiteCadastraMusicas(self)


    def enterHandler(self, event):
        
        nome = self.limiteIns.inputTitulo.get()
        nro = self.limiteIns.inputNroFaixa.get()
        artista = self.limiteIns.inputArtista.get()
        
        musica = Musica(nome, artista, nro)
        
        self.listaMusicas.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Musica registrada com sucesso')
        