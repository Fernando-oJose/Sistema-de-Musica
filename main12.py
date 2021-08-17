import tkinter as tk
from tkinter import messagebox
import artista as art
import album as alb
import playlist as pla
import musica as mus

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('400x350')
        self.menubar = tk.Menu(self.root)        
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.artistaMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastraArtista)
        self.artistaMenu.add_command(label="Consultar", \
                    command=self.controle.consultaArtista)
        self.artistaMenu.add_command(label="Cadastrar Música", \
                    command=self.controle.cadastrarMusicas)
        self.menubar.add_cascade(label="Artista", \
                    menu=self.artistaMenu)
        
        self.albumMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastraAlbum)
        self.albumMenu.add_command(label="Consultar", \
                    command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label="Album", \
                    menu=self.albumMenu)
            
        self.playlistMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastraPlaylist)
        self.playlistMenu.add_command(label="Consultar", \
                    command=self.controle.consultaPlaylist)
        self.menubar.add_cascade(label="Playlist", \
                    menu=self.playlistMenu)
            
        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlArtista = art.CtrlArtista()
        self.ctrlAlbum = alb.CtrlAlbum(self)
        self.ctrlPlaylist = pla.CtrlPlaylist(self)
        self.ctrlMusica = mus.CtrlMusica(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trabalho 12")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraArtista(self):
        self.ctrlArtista.insereArtista()

    def consultaArtista(self):
        self.ctrlArtista.conArtista()
    
    def cadastrarMusicas(self):
        self.ctrlMusica.cadMusicas()

    def cadastraAlbum(self):
        self.ctrlAlbum.insereAlbum()

    def consultaAlbum(self):
        self.ctrlAlbum.conAlbum()

    def cadastraPlaylist(self):
        self.ctrlPlaylist.inserePlaylist()

    def consultaPlaylist(self):
        self.ctrlPlaylist.conPlaylist()

    def salvaDados(self):
        self.ctrlArtista.salvaArtista()
        self.ctrlAlbum.salvaAlbum()
        self.ctrlPlaylist.salvaPlaylist()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()