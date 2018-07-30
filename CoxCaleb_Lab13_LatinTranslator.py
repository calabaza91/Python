#This program uses checkbuttons to translate three latin words to english

import tkinter

class MyGUI:
    def __init__(self):
        #Create main window
        self.main_window = tkinter.Tk()
        #Label for GUI program
        self.label = tkinter.Label(self.main_window,
                                   text = 'Latin Translator')
        #Pack label
        self.label.pack()

        #Make frames
        self.title_frame = tkinter.Frame(self.main_window)
        self.word_frame = tkinter.Frame(self.main_window)
        self.botm_frame = tkinter.Frame(self.main_window)


        #Titles for latin and english words
        self.lat = tkinter.Label(self.title_frame,
                                 text='Latin')
        self.eng = tkinter.Label(self.title_frame,
                                 text='\tEnglish')

        self.lat.pack(side='left')
        self.eng.pack(side='left')


        #Frame for words
        self.top_frame = tkinter.Frame(self.word_frame)
        self.mid_frame = tkinter.Frame(self.word_frame)

        

#Latin Word Buttons        
        #Create an IntVar object to use w/ checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        #Set values to 0 so that no radio button is selected.
        #i.e there is no default
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        #Create radio button widgets in top_frame
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Sinister\t',
                                       variable = self.cb_var1,
                                       command=self.translate)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Dexter\t',
                                       variable = self.cb_var2,
                                       command=self.translate)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Medium\t',
                                       variable = self.cb_var3,
                                       command=self.translate)
                                       #This will show the translation
                                       #w/o a button

        #Pack Radiobuttons
        self.cb1.pack(side= 'top')
        self.cb2.pack(side= 'top')
        self.cb3.pack(side= 'top')




#English Translations        
        #Create StringVar object for translations lables
        self.value1 = tkinter.StringVar()
        self.value2 = tkinter.StringVar()
        self.value3 = tkinter.StringVar()

        #Create lables
        self.lab1 = tkinter.Label(self.mid_frame,
                                  textvariable = self.value1)
        self.lab2 = tkinter.Label(self.mid_frame,
                                  textvariable = self.value2)
        self.lab3 = tkinter.Label(self.mid_frame,
                                  textvariable = self.value3)


        self.lab1.pack(side='top')
        self.lab2.pack(side= 'top')
        self.lab3.pack(side = 'top')


        #Quit button
        self.quit_button = tkinter.Button(self.botm_frame,
                                          text ='Quit',
                                          command =self.main_window.destroy)
        self.quit_button.pack()

        #Pack Frames

        self.title_frame.pack()
        self.top_frame.pack(side='left')
        self.mid_frame.pack(side='left')
        self.word_frame.pack()
        self.botm_frame.pack()

        #Start main loop......THIS IS RECURSION!!!
        tkinter.mainloop()


#Shows translation in separate window
    def translate(self):
        #Show translation
        if self.cb_var1.get()==1:
            self.value1.set('Left')
        #Hide translation
        else:
            self.value1.set('')
            
        if self.cb_var2.get()==1:
             self.value2.set('Right')
        else:
            self.value2.set('')
             
        if self.cb_var3.get()==1:
             self.value3.set('Center')
        else:
            self.value3.set('')

#Create an instance of MyGUI class
my_gui = MyGUI()

