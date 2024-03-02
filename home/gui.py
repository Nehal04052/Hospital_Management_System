import sys
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageOps
from .button_function import login
from home import button_function

class Application(tk.Frame):
    def __init__(self, master):  # Add 'master' as an argument
        super().__init__(master, bg='light blue', padx=5)  # Use 'master' here
        self.master = master  # Store 'master' in 'self.master'
        self.master.title("Hospital management system")
        self.master.wm_iconbitmap(r'D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\hospital.ico')
        self.grid(sticky="nsew")  # Use grid instead of pack

        self.create_widgets()
        self.update_image()  # Call this function once to start the loop
        # Bind the window close event to a function
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        


    def create_widgets(self):
        # Login button
        self.login = tk.Button(self, text="Login", command=lambda: button_function.login(self.master,self.login),borderwidth=0,background='blueviolet',relief='ridge', activebackground='white',width=10,height=1,font=("Comic Sans MS", 15,'bold'),fg='white')
        self.login.grid(row=0, column=2, sticky="ne",pady=4,padx=10)  # Use grid instead of pack

        # Image slider
        self.images = [self.rounded_image(Image.open(r"D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\home\1.png").resize((self.winfo_screenwidth()-10, 415))), self.rounded_image(Image.open(r"D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\home\2.png").resize((self.winfo_screenwidth()-10, 415))), self.rounded_image(Image.open(r"D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\home\3.png").resize((self.winfo_screenwidth()-10, 415)))]
        self.image_label = tk.Label(self, image=self.images[0],background='light blue')
        self.image_label.grid(row=1, column=0, columnspan=3, sticky="nsew")  # Use grid instead of pack
        self.current_image = 0

        # Arrow buttons
        self.left_button = tk.Button(self, text="<", command=self.prev_image, borderwidth=0, background='SystemButtonFace', activebackground='SystemButtonFace')
        self.left_button.place(x=5, y=self.winfo_screenheight()//4)
        self.right_button = tk.Button(self, text=">", command=self.next_image, borderwidth=0, background='SystemButtonFace', activebackground='SystemButtonFace')
        self.right_button.place(x=self.winfo_screenwidth()-30, y=self.winfo_screenheight()//4)

        # Cards
        self.create_card(2, 0, "Comprehensive Healthcare", ["🏥 State-of-the-Art Facilities: Our hospital is equipped with cutting-edge technology and modern infrastructure to provide the highest standard of care.", "⚕️ Diverse Medical Specialties: From cardiology to pediatrics, our expert medical team covers a wide range of specialties, ensuring comprehensive healthcare services.", "🌐 Community-Centric Approach: We are committed to serving our community, providing accessible and compassionate healthcare for all."])
        self.create_card(2, 1, "Patient-Focused Care", ["💙 Patient-Centered Approach: Our dedicated staff prioritizes patient well-being, offering personalized care and support throughout the healing journey.", "🌈 Comfortable and Supportive Environment: Experience a warm and welcoming atmosphere designed to promote healing and comfort for patients and their families.", "🤝 Patient Education Programs: We believe in empowering our patients with knowledge."])
        self.create_card(2, 2, "Excellence in Service", ["🌟 Accredited Healthcare Professionals: Our team of skilled and accredited healthcare professionals is committed to delivering excellence in medical care.", "🏆 Award-Winning Services: Recognized for our outstanding services, we take pride in our achievements and continuous commitment to quality healthcare.", "🕒 24/7 Emergency Care: Your health is our priority."])

    def rounded_image(self, img):
        img = img.convert("RGBA")
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([(0, 0), img.size], 20, fill=255)
        img.putalpha(mask)
        return ImageTk.PhotoImage(img)

    def create_card(self, row, column, title, points):
        frame = tk.Frame(self, bd=2, relief="groove", bg='white', width=self.winfo_screenwidth()//1-10, height=200)
        frame.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)
        frame.grid_propagate(0)  # Prevents the frame from resizing to fit its contents
        label_title = tk.Label(frame, text=title, font=("Lucida Calligraphy", 23,'bold'), bg='white')
        label_title.pack(pady=10)
        for point in points:
            label_point = tk.Label(frame, text=point,font=("Comic Sans MS", 11), wraplength=self.winfo_screenwidth()//4, justify="center", bg='white')
            label_point.pack(anchor="w", padx=50,pady=2)
    
    def on_closing(self):
        # Stop the scheduled calls to update_image when the window is closed
     self.after_cancel(self.after_id)
     self.master.destroy()
     sys.exit()

    def update_image(self):
        self.image_label.configure(image=self.images[self.current_image])
        self.current_image = (self.current_image + 1) % len(self.images)
        self.after_id = self.after(2000, self.update_image)  # Save the after ID
  
    def next_image(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.image_label.configure(image=self.images[self.current_image])

    def prev_image(self):
        self.current_image = (self.current_image - 1) % len(self.images)
        self.image_label.configure(image=self.images[self.current_image])

