from tkinter import *
from backend import *

class fileManWindow():
    def __init__(self):
        self.window=Tk()
        self.backendObj=shellBackend()
        self.mainWindow()
        self.inputType="nothing"

    def handleShowFile(self,event):
        self.outputArea.insert(END,f"\n{self.backendObj.getls()}\n")
        self.outputArea.yview(END)
    def handleShowDirectory(self,event):
        self.outputArea.insert(END,f"\ncommand : pwd\nMyshell> {self.backendObj.getCurrentPos().decode('utf-8')}\n")
        self.outputArea.yview(END)
        

    def handleCreateFile(self,event):
        self.inputText.config(text="Enter the new file name:")
        self.inputFrame.place(rely=.5,relx=.01,relheight=.09,relwidth=.98)
        self.inputType="createFile"
    def handlCreateFolder(self,event):
        self.inputText.config(text="Enter the new folder name:")
        self.inputFrame.place(rely=.5,relx=.01,relheight=.09,relwidth=.98)
        self.inputType="createFolder"
    def handleDeleteFile(self,event):
        self.inputText.config(text="Enter the file name to delete:")
        self.inputFrame.place(rely=.5,relx=.01,relheight=.09,relwidth=.98)
        self.inputType="deleteFile"
    def handleDeleteFolder(self,event):
        self.inputText.config(text="Enter the folder name to delete:")
        self.inputFrame.place(rely=.5,relx=.01,relheight=.09,relwidth=.98)
        self.inputType="deleteFolder"

    def on_enter(self,event):
        inputRes=self.inputEntry.get()
        if(self.inputType=='createFile'):
            if(self.backendObj.createnewFile(inputRes)==0):
                self.outputArea.insert(END,"\nMyshell> File created Successfully.\n")
            else :
                self.outputArea.insert(END,"\nMyshell> Something went wrong.\n")
        elif(self.inputType=="createFolder"):
            if(self.backendObj.createNewFolder(inputRes)==0):
                self.outputArea.insert(END,"\nMyshell> Folder created Successfully.\n")
            else :
                self.outputArea.insert(END,"\nMyshell> Something went wrong.\n")
        elif(self.inputType=="deleteFile"):
            if(self.backendObj.deleteFile(inputRes)==0):
                self.outputArea.insert(END,"\nMyshell> File deleted Successfully.\n")
            else :
                self.outputArea.insert(END,"\nMyshell> Something went wrong.\n")
        elif(self.inputType=="deleteFolder"):
            if(self.backendObj.deleteFolder(inputRes)==0):
                self.outputArea.insert(END,"\nMyshell> Folder deleted Successfully.\n")
            else :
                self.outputArea.insert(END,"\nMyshell> Something went wrong.\n")
        self.outputArea.yview(END)
        self.inputFrame.place_forget()
    def handleExitWindow(self,event):
        self.window.after(1, self.window.destroy)


    def mainWindow(self):
        self.window.title("File Management Window")
        self.window.configure(width='800px',height='500px')

        self.showFiles=Button(self.window,text="Show files",font=('Arial',12,'bold'),cursor='hand2',borderwidth=3,relief='ridge')
        self.showFiles.place(relx=.01,relheight=.15,relwidth=.18)

        self.createFile=Button(self.window,text="Create File",font=('Arial',12,'bold'),cursor='hand2',borderwidth=3,relief='ridge')
        self.createFile.place(relx=.2,relwidth=.18,relheight=.15)
        self.createFolder=Button(self.window,text="Create Folder",font=('Arial',12,'bold'),cursor='hand2',borderwidth=3,relief='ridge')
        self.createFolder.place(relx=.39,relwidth=.18,relheight=.15)

        self.showDirectory=Button(self.window,text="Show Directory",font=('Arial',12,'bold'),cursor='hand2',borderwidth=3,relief='ridge')
        self.showDirectory.place(relx=.58,relwidth=.18,relheight=.15)

        self.deleteFile=Button(self.window,text="Delete File",font=('Arial',12,'bold'),cursor='hand2',borderwidth=3,relief='ridge')
        self.deleteFile.place(relx=.77,relwidth=.18,relheight=.15)
        self.deleteFolder=Button(self.window,text="Delete Folder",font=('Arial',12,'bold'),cursor='hand2',borderwidth=3,relief='ridge')
        self.deleteFolder.place(relx=.01,relwidth=.18,relheight=.15,rely=.16)
        self.exitButton=Button(self.window,text="Exit",font=('Arial',12,'bold'),cursor='hand2',borderwidth=3,relief='ridge')
        self.exitButton.place(relx=.2,relwidth=.18,relheight=.15,rely=.16)



        self.inputFrame=Frame(self.window,border=1,relief='groove')
        self.inputFrame.place(rely=.5,relx=.01,relheight=.09,relwidth=.98)
        self.inputFrame.place_forget()
        self.inputText=Label(self.inputFrame,text="",font=('Times',16),padx=4,pady=4,anchor='w')
        self.inputText.place(relx=.01,rely=.1,relheight=.8,relwidth=.7)

        self.inputEntry=Entry(self.inputFrame,font=('Times',14),justify='center',borderwidth=1,relief='ridge',fg="black")
        self.inputEntry.place(relx=.72,rely=.1,relheight=.8,relwidth=.27)
        self.inputEntry.bind("<Return>",self.on_enter)

        self.outputArea=Text(self.window,font=('Times',16),padx=4,pady=4,borderwidth=3,relief='ridge',bg="black",fg="lime",
                                                      insertbackground='lime')
        self.outputArea.place(relx=.01,rely=.6,relheight=.39,relwidth=.98)


        self.outputArea.insert(END,"Myshell> ")
        self.showFiles.bind("<Button-1>",self.handleShowFile)
        self.showDirectory.bind("<Button-1>",self.handleShowDirectory)
        self.createFile.bind("<Button-1>",self.handleCreateFile)
        self.createFolder.bind("<Button-1>",self.handlCreateFolder)
        self.deleteFile.bind("<Button-1>",self.handleDeleteFile)
        self.deleteFolder.bind("<Button-1>",self.handleDeleteFolder)
        self.exitButton.bind("<Button-1>",self.handleExitWindow)
        


    def run(self):
        self.window.mainloop()

        
        
# try:
#     app=fileManWindow()
#     app.run()
# except Exception as e:
#     print(e)