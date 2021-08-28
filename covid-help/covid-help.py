from tkinter import Button, Label, LabelFrame, PhotoImage, Tk ,W,E,N,S,Entry,END,StringVar,Scrollbar,Toplevel
from tkinter import ttk
import sqlite3

class covidhelp:
    database = 'C:/Users/lenovo/Desktop/covid-help/covid.db'
    
    def __init__(self,root):
        self.root = root
        self.create_gui()
        ttk.Style = ttk.Style()
        ttk.Style.configure("Treeview",font=('helvetica',10))
        ttk.Style.configure("Treeview.Heading",font=('helvetica',11,'bold'))
        
    def execute_db_query(self,query,parameters=()):
        with sqlite3.connect(self.database) as conn:
            print(conn)
            print(' you have successfully connected to the Database')
            cursor = conn.cursor()
            query_result = cursor.execute(query,parameters)
            conn.commit()   
        return query_result
    
    
    def create_gui(self):
        self.Donation()
        self.receive()
        self.create_message_area()
        self.create_tree_view()
        #self.view_donars()
        self.create_scrollbar()
        self.icon()
        
        
        
    def icon(self):
        photo = PhotoImage(file="C:/Users/lenovo/Desktop/covid-help/logos/LogoMakr-0WzAEA.gif")
        label = Label(image=photo)
        label.image = photo
        label.grid(row=2,column=3,sticky='ew')
        
    def create_tree_view(self):
        self.tree = ttk.Treeview(height=10 , columns=(1,2,3,4),style="Treeview")
        self.tree.grid(row=13,column=0,columnspan=5)
        self.tree.heading('#0',text='Name',anchor=W)
        self.tree.heading("1",text="Email Address",anchor=W)
        self.tree.heading("2",text='Contact Number',anchor=W)
        self.tree.heading("3",text='City',anchor=W)
        self.tree.heading("4",text='Things',anchor=W)
        
    def Donation(self) :
        labelframe = LabelFrame(self.root, text='Donate', bg="sky blue", font="helvetica 15")
        labelframe.grid(row=2, column=0, padx=8, pady=8, sticky='ew')
        Label(labelframe, text='Name: ', bg="sky blue", fg="black",font="helvetica 12").grid(row=3, column=1, sticky=W, pady=2, padx=15)
        self.namefield = Entry(labelframe)
        self.namefield.grid(row=3, column=2, sticky=W, padx=5,)
        Label(labelframe, text="Address ", bg="sky blue", fg="black",font="helvetica 12").grid(row=4, column=1, sticky=W, pady=2, padx=15)
        self.emailfield = Entry(labelframe)
        self.emailfield.grid(row=4,column=2,sticky=W,padx=5 , pady=2)
        Label(labelframe, text= 'Number: ', bg="sky blue", fg="black",font="helvetica 12").grid(row=5, column=1, sticky=W, pady=2, padx=15)
        self.numfield = Entry(labelframe)
        self.numfield.grid(row=5,column=2,sticky=W,padx=5 , pady=2)
        Label(labelframe, text= 'City: ', bg="sky blue", fg="black",font="helvetica 12").grid(row=6, column=1, sticky=W, pady=2, padx=15)
        self.cityfield = Entry(labelframe)
        self.cityfield.grid(row=6, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text= 'Thing: ', bg="sky blue", fg="black",font="helvetica 12").grid(row=7, column=1, sticky=W, pady=2, padx=15)
        self.thingfield = Entry(labelframe)
        self.thingfield.grid(row=7, column=2, sticky=W, padx=5, pady=2)
        Button(labelframe, text="DONATE", command=self.add_donation, bg="blue", fg="black",font="helvetica 12").grid(row=9, column=1, sticky=E, padx=5, pady=5)
        #Button(labelframe, text="Delete Selected", command=self.add_donation, bg="blue", fg="sky blue").grid(row=6, column=2, sticky=E, padx=5, pady=5)
    
    def receive(self) :
        labelframeR = LabelFrame(self.root, text='Get Help', bg="sky blue", font="helvetica 15")
        labelframeR.grid(row=8, column=0, padx=8, pady=8, sticky='ew')
        Label(labelframeR, text= 'City: ', bg="Sky blue", fg="black",font="helvetica 12").grid(row=9, column=1, sticky=W, pady=2, padx=15)
        self.Rcityfield = Entry(labelframeR)
        self.Rcityfield.grid(row=9, column=2, sticky=W, padx=5, pady=2)
        Label(labelframeR, text= 'Thing: ', bg="sky blue", fg="black",font="helvetica 12").grid(row=10, column=1, sticky=W, pady=2, padx=15)
        self.Rthingfield = Entry(labelframeR)
        self.Rthingfield.grid(row=10, column=2, sticky=W, padx=5, pady=2)
        Button(labelframeR, text="Search", command=self.view_donars, bg="blue", fg="black",font="helvetica 12").grid(row=11, column=1, sticky=E, padx=5, pady=5)
        Button(labelframeR, text="Delete False", command=self.on_delet_selected_button_clicked, bg="red", fg="white",font="helvetica 12").grid(row=11, column=2, sticky=E, padx=5, pady=5)
        
        
    def create_scrollbar(self):
        self.scrollbar = Scrollbar(orient='vertical',command=self.tree.yview)
        self.scrollbar.grid(row=13,column=5,columnspan=3,rowspan=10,sticky="sn")
        
        
    def create_message_area(self):
        self.message = Label(text='',fg='red',font="helvetica 15")
        self.message.grid(row=12,column=0,sticky="sn")
        
    def add_donation(self):
        if self.validated():
            if self.number():
            
                query = 'INSERT INTO covid VALUES(NULL,?, ?,?,?,?)'
                parameters = (self.namefield.get(),self.emailfield.get(), self.numfield.get(),self.cityfield.get(),self.thingfield.get())
                self.execute_db_query(query, parameters)
                self.message['text'] = 'New Donar {} added'.format(self.namefield.get())
                self.namefield.delete(0, END)
                self.emailfield.delete(0, END)
                self.numfield.delete(0, END)
                self.cityfield.delete(0, END)
                self.thingfield.delete(0, END)
            else:
                self.message['text'] = 'enter correct number '
            #self.view_donars()
            
            #self.view_donars()
            
        else:
            self.message['text'] = 'Donate field cannot be blank'
            #self.view_donars()
            
    def view_donars(self):
        
        name = self.Rcityfield.get()
        thing = self.Rthingfield.get()
        if self.Rvalidated() and self.Tvalidated():
        
            items = self.tree.get_children()
            for item in items:
                self.tree.delete(item)
            query = 'SELECT * FROM covid where city = ? and Thing = ?'
            donar_entries = self.execute_db_query(query,(name,thing,))
            for row in donar_entries:
                    self.tree.insert('', 0, text=row[1], values=(row[2],row[3],row[4],row[5]))
        elif self.Rvalidated():
            items = self.tree.get_children()
            for item in items:
                self.tree.delete(item)
            query = 'SELECT * FROM covid where city = ?'
            donar_entries = self.execute_db_query(query,(name,))
            for row in donar_entries:
                    self.tree.insert('', 0, text=row[1], values=(row[2],row[3],row[4],row[5]))
        elif self.Tvalidated():
            items = self.tree.get_children()
            for item in items:
                self.tree.delete(item)
            query = 'SELECT * FROM covid where Thing = ?'
            donar_entries = self.execute_db_query(query,(thing,))
            for row in donar_entries:
                    self.tree.insert('', 0, text=row[1], values=(row[2],row[3],row[4],row[5]))
        else:
            self.message['text'] = 'Search field cannot be blank'
                
    def delete_donor(self):
        self.message['text']=''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM covid Where name = ?'
        self.execute_db_query(query,(name,))
        self.message['text']='Donor {} deleted'.format(name)
        self.view_donars()
    
    def on_delet_selected_button_clicked(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text']='No item selected to delete'
            return
        self.delete_donor()
    
    
    def validated(self):
        return len(self.namefield.get()) != 0 and len(self.emailfield.get()) != 0 and len(self.numfield.get()) != 0 and len(self.cityfield.get()) != 0 and len(self.thingfield.get()) != 0
    
    def Rvalidated(self):
        return len(self.Rcityfield.get()) != 0 
    
    def Tvalidated(self):
        return len(self.Rthingfield.get()) != 0
    
    def number(self):
        return len(self.Rthingfield.get()) == 10
    
    
if __name__ == '__main__':
    root =Tk()
    root.title('Covid - HELPER')
    root.geometry("1100x720")
    root.resizable(width=False, height=False)
    application = covidhelp(root)
    root.mainloop() 