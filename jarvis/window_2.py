import tkinter as tk
from tkinter import Label, Text, Frame
from PIL import Image, ImageTk
import os
import sys
import time

def window_2():
    
    root2 = tk.Tk()
    root2.title("Echo - Main Interface")

    
    root2.attributes("-fullscreen", True)

    
    bg_image_path = r"C:\Users\jenil\OneDrive\Desktop\sem5\image3.jpg"  
    if os.path.exists(bg_image_path):
        bg_image = Image.open(bg_image_path)

        
        bg_image = bg_image.resize((root2.winfo_screenwidth(), root2.winfo_screenheight()), Image.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)

        bg_label = Label(root2, image=bg_image)
        bg_label.image = bg_image  
        bg_label.place(relwidth=1, relheight=1)
    else:
        print(f"Error: Image '{bg_image_path}' not found")

    
    msg_frame = Frame(root2, bg="lightblue", bd=2, relief="groove")

    
    message_box_height = int(root2.winfo_screenheight() * 0.5)  
    message_box_width = int(root2.winfo_screenwidth() * 0.4)    

    
    msg_frame.place(relx=1, rely=1, anchor='se', width=message_box_width, height=message_box_height)

    title_label = Label(msg_frame, text="Command Box", bg="lightblue", fg="black", font=("Arial", 14, "bold"))
    title_label.pack(pady=5)

    
    message_box = Text(msg_frame, bg="white", fg="black", font=("Arial", 10))
    message_box.pack(expand=True, fill=tk.BOTH)  

    
    class StdoutRedirector:
        def __init__(self, textbox):
            self.textbox = textbox

        def write(self, text):
            if not self.textbox.winfo_ismapped():  
                return
            self.textbox.insert(tk.END, text)
            self.textbox.see(tk.END)  
            sys.__stdout__.write(text)  

        def flush(self):
            pass

    sys.stdout = StdoutRedirector(message_box)

    
    print("Echo initialized...")
    print("Waiting for commands...")


    def close_jarvis():
        print("Going to sleep...")
        time.sleep(2)
        root2.quit() 
        sys.exit()  

    
    def check_for_commands():
        
        command = message_box.get("1.0", tk.END).strip().lower()  

        if "finally sleep" in command:
            close_jarvis()  

        
        root2.after(1000, check_for_commands)

    
    root2.protocol("WM_DELETE_WINDOW", close_jarvis)

    
    check_for_commands()

    root2.mainloop()


    sys.stdout = sys.__stdout__