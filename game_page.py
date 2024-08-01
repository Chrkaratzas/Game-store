from tkinter import *
from PIL import Image, ImageTk
import webbrowser

root = Tk()
root.title('Game page')

# Load and resize images
def load_and_resize_image(file_path, size=(100, 100)):
    img = Image.open(file_path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Assuming you have .ico file for the window icon
root.iconbitmap('icon.ico')

# Load images for buttons
img1 = load_and_resize_image('community.png')
img3 = load_and_resize_image('info.jpg')
img4 = load_and_resize_image('start.jpeg')
img5 = load_and_resize_image('Phasmophobia.jpg')
img6 = load_and_resize_image('Demonologist.jpg')
img7 = load_and_resize_image('Bigfoot.jpg')


# Define button functions
def start_button():
    top = Toplevel()
    top.title("Game gallery")
    top.iconbitmap('icon.ico')

    def open_phasmo():
        top.destroy()
        root.destroy()
        app_id = '739630'  # App ID για το Phasmophobia
        steam_url = f'steam://run/{app_id}'
        webbrowser.open(steam_url)


    def open_demon():
        top.destroy()
        root.destroy()
        app_id = '1929610'   
        steam_url = f'steam://run/{app_id}'
        webbrowser.open(steam_url)

    def open_big():
        top.destroy()
        root.destroy()
        app_id = '509980'
        steam_url = f'steam://run/{app_id}' 
        webbrowser.open(steam_url)


    phasmo_frame = Frame(top,borderwidth=25)
    phasmo_image = Label(phasmo_frame,image=img5)
    phasmo_button = Button(phasmo_frame,text="Start",padx=40,pady=40, command=open_phasmo)
    phasmo_frame.grid(row=0,column=0)
    phasmo_image.grid(row=0,column=0)
    phasmo_button.grid(row=0,column=2)

    demon_frame = Frame(top,borderwidth=25)
    demon_image = Label(demon_frame,image=img6)
    demon_button = Button(demon_frame,text="Start",padx=40,pady=40, command=open_demon)
    demon_frame.grid(row=1,column=0)
    demon_image.grid(row=0,column=0)
    demon_button.grid(row=0,column=2)

    big_frame = Frame(top,borderwidth=25)
    big_image = Label(big_frame,image=img7)
    big_button = Button(big_frame,text="Start",padx=40,pady=40, command=open_big)
    big_frame.grid(row=2,column=0)
    big_image.grid(row=0,column=0)
    big_button.grid(row=0,column=2)

    top.mainloop()

def info_button():
    top = Toplevel()
    top.title("Info gallery")
    top.iconbitmap('icon.ico')


    phasmo_frame = Frame(top,borderwidth=25)
    phasmo_image = Label(phasmo_frame,image=img5)
    phasmo_label = Label(phasmo_frame,text="Phasmophobia is a 4 player online co-op psychological horror. Paranormal activity is on the rise and it’s up to you and your team to use all the ghost-hunting equipment at your disposal in order to gather as much evidence as you can.")
    phasmo_frame.grid(row=0,column=0)
    phasmo_image.grid(row=0,column=0)
    phasmo_label.grid(row=0,column=1)

    demon_frame = Frame(top,borderwidth=25)
    demon_image = Label(demon_frame,image=img6)
    demon_label = Label(demon_frame,text="Το Demonologist είναι ένα Co-Op παιχνίδι τρόμου που μπορεί να παιχτεί με το πολύ 4 άτομα και τουλάχιστον 1 άτομο. Στόχος σας είναι να εντοπίσετε τον τύπο του κακού πνεύματος σε καταραμένα μέρη με την ομάδα σας ή μόνοι σας χρησιμοποιώντας τον εξοπλισμό σας.")
    demon_frame.grid(row=1,column=0)
    demon_image.grid(row=0,column=0)
    demon_label.grid(row=0,column=1)

    big_frame = Frame(top,borderwidth=25)
    big_image = Label(big_frame,image=img7)
    big_label = Label(big_frame,text="You are a Bigfoot hunter with an important mission: to put an end to rumours once and for all and prove to yourself that Bigfoot is not just a myth or an invention of the mind...")
    big_frame.grid(row=2,column=0)
    big_image.grid(row=0,column=0)
    big_label.grid(row=0,column=1)


def community_button():
    top = Toplevel()
    top.title("Community Links")
    top.iconbitmap('icon.ico')

    def open_phasmo_com():
        webbrowser.open('https://steamcommunity.com/app/739630')

    def open_demon_com():
        webbrowser.open('https://steamcommunity.com/app/1929610')
    
    def open_big_com():
        webbrowser.open('https://steamcommunity.com/app/509980')

    phasmo_frame = Frame(top,borderwidth=25)
    phasmo_image = Label(phasmo_frame,image=img5)
    phasmo_label = Label(phasmo_frame,text="Link to phasmophobia's steam community:")
    phasmo_button = Button(phasmo_frame, text="GO", command=open_phasmo_com)
    phasmo_frame.grid(row=0,column=0)
    phasmo_image.grid(row=0,column=0)
    phasmo_label.grid(row=0,column=1)
    phasmo_button.grid(row=0,column=2)

    demon_frame = Frame(top,borderwidth=25)
    demon_image = Label(demon_frame,image=img6)
    demon_label = Label(demon_frame,text="Link to demonologist's steam community:")
    demon_button = Button(demon_frame, text="GO", command=open_demon_com)
    demon_frame.grid(row=1,column=0)
    demon_image.grid(row=0,column=0)
    demon_label.grid(row=0,column=1)
    demon_button.grid(row=0,column=2)

    big_frame = Frame(top,borderwidth=25)
    big_image = Label(big_frame,image=img7)
    big_label = Label(big_frame,text="Link to bigfoot's steam community:")
    big_button = Button(big_frame, text="GO", command=open_big_com)
    big_frame.grid(row=2,column=0)
    big_image.grid(row=0,column=0)
    big_label.grid(row=0,column=1)
    big_button.grid(row=0,column=2)


# Create buttons with images and text
Start_button = Button(root, text="START", image=img4, compound=TOP, padx=100, pady=350, command=start_button, bg="red")
Start_button.grid(row=0, column=0, padx=10, pady=10)

Info_button = Button(root, text="INFO", image=img3, compound=TOP, padx=100, pady=350, command=info_button, bg="green")
Info_button.grid(row=0, column=1, padx=10, pady=10)

Community_button = Button(root, text="COMMUNITY", image=img1, compound=TOP, padx=100, pady=350, command=community_button, bg="grey")
Community_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()