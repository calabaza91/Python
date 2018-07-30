

import tkinter

class MilesPerGal_GUI:

    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.miles_label = tkinter.Label(self.top_frame,
                                         text='Enter miles:')
        self.miles_entry = tkinter.Entry(self.top_frame,
                                          width=10)

        
        self.gal_label = tkinter.Label(self.top_frame,
                                       text='Enter gallons:')
        self.gal_entry =tkinter.Entry(self.top_frame,
                                      width=10)
        #Pack labels
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side = 'left')
        self.gal_label.pack(side='left')
        self.gal_entry.pack(side = 'left')


        
        self.mpg_descr_label = tkinter.Label(self.mid_frame,
                                       text='MPG: ')

        self.value = tkinter.StringVar()

        self.mpg_label = tkinter.Label(self.mid_frame,
                                       textvariable = self.value)

        #Pack widgets
        self.mpg_descr_label.pack(side='left')
        self.mpg_label.pack(side='left')


        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Calculate MPG',
                                          command=self.mpg_calc)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

        

    def mpg_calc(self):

        miles = float(self.miles_entry.get())

        gallons = float(self.gal_entry.get())
        mpg = miles/gallons

        self.value.set(mpg)


mpgGUI = MilesPerGal_GUI()
