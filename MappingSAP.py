#Developed by BigSy
#Developer Luiz Gustavo Rodrigues Magalhães
#=================//========================
#This small system was developed for the automation and autonomy of the users in a company that uses sap systems.
#The mapping of the instances was done by the support team, but with MappingSAP this process is done by the user with just one click.
#The system is dependent of a bat (cmd) file that consumes an XML with the necessary SAP instances 


from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "12")

        self.container1 = Frame(master)
        self.container1["pady"] = 50
        self.container1.pack()
        
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.msg= Label(self.container1, text="Seja bem vindo ao Mapeador de SAP")
        self.msg["font"] = ("Verdana", "12", "italic")
        self.msg.pack()

        self.submit = Button(self.container2)
        self.submit["text"] = "Mapear"
        self.submit["font"] = ("Calibri", "12", "bold")
        self.submit["width"] = 10
        self.submit["command"] = self.mapear
        self.submit.pack(side=LEFT)

        self.sair = Button(self.container2)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "12", "bold")
        self.sair["width"] = 10
        self.sair["command"] = self.container2.quit
        self.sair.pack (side=LEFT)
        
    def mapear(self):
        self.msg["text"] = "Aguarde 10 segundos!! Em seguida aperte SAIR. SAP MAPEADO!"
        self.msg["font"] = ("Verdana", "12", "italic", "bold")
        from pywinauto.application import Application
        app = Application(backend= 'uia').start("URL") #Em URL apontar o caminho do mapeamento de rede que se encontra o seu arquivo bat que consome uma XML com todas as instâncias SAP a ser mapeada
        
root = Tk()
Application(root)
root.mainloop()


