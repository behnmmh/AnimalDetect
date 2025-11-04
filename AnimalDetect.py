import os
import warnings
from PIL import Image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # حذف پیام‌های info و warning از TensorFlow
warnings.filterwarnings("ignore")
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
model = load_model("animals.h5")
import customtkinter as ctk
from tkinter.filedialog import askopenfilename

root = ctk.CTk()
root.geometry("400x400")

root.config(bg="#222")
root.overrideredirect(True)
outer_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="cyan")
outer_frame.pack(padx=0, pady=0)
root.attributes('-alpha', 0.9)  # 0.0 کاملاً شفاف، 1.0 کاملاً مات

# فریم داخلی با رنگ پس‌زمینه اصلی یا دلخواه
inner_frame = ctk.CTkFrame(outer_frame,width=400,height=400 ,corner_radius=0, fg_color="#222")
inner_frame.pack(padx=1, pady=1)  # فاصله برای نوار سفید
def start_move(event):
    root.x = event.x_root
    root.y = event.y_root

# تابع برای حرکت پنجره
def do_move(event):
    dx = event.x_root - root.x
    dy = event.y_root - root.y
    x = root.winfo_x() + dx
    y = root.winfo_y() + dy
    root.geometry(f"+{x}+{y}")
    root.x = event.x_root
    root.y = event.y_root

# وصل کردن رویداد کلیک و درگ به inner_frame
inner_frame.bind("<Button-1>", start_move)
inner_frame.bind("<B1-Motion>", do_move)
def select_file():
    img_path = askopenfilename(
        title="انتخاب عکس",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
    img = image.load_img(img_path, target_size=(224, 224))

    img = np.array(img).reshape(1, 224, 224, 3)
    x = model.predict(img)
    predicted_class = np.argmax(x, axis=1)
    print(predicted_class)
    name.place(y=1000)
    label.place(y=1000)
    path = ''
    if predicted_class[0] == 0:
        path = 'icons/dog.png'
    if predicted_class[0] == 1:
        path = 'icons/horse.png'
    if predicted_class[0] == 2:
        path = 'icons/elephant.png'
    if predicted_class[0] == 3:
        path = 'icons/butterfly.png'
    if predicted_class[0] == 4:
        path = 'icons/chicken.png'
    if predicted_class[0] == 5:
        path = 'icons/cat.png'
    if predicted_class[0] == 6:
        path = 'icons/cow.png'
    if predicted_class[0] == 7:
        path = 'icons/sheep.png'
    if predicted_class[0] == 8:
        path = 'icons/squirrel.png'
    img_pil = Image.open(path)  # باز کردن تصویر با PIL
    img = ctk.CTkImage(img_pil, size=(120, 120))

    answer  = ctk.CTkLabel(inner_frame, text='',image=img, text_color='green', font=('ariel', 25, 'bold'))
    answer.place(relx=0.37,rely=0.31)
    img_back = Image.open('icons/refresh.png')  # باز کردن تصویر با PIL
    img_back = ctk.CTkImage(img_back, size=(45, 45))
    def back():
        name.place(y=255)
        label.place(y=155)
        answer.place(y=1000)
        back_button.place(y=1000)

    back_button = ctk.CTkButton(inner_frame,text='',image=img_back,width=30,fg_color="#222",hover_color="#222",cursor='hand2',command=back)
    back_button.place(relx=0.45,rely=0.72)
    # کلاس با بیشترین احتمال


img_pil = Image.open("icons/folder.png")  # باز کردن تصویر با PIL
icon = ctk.CTkImage(img_pil, size=(80, 80))

label = ctk.CTkButton(inner_frame, image=icon,bg_color='#222',fg_color='#222',hover_color='#222', text="",cursor='hand2',command=select_file)
label.place(relx=0.335,y=155)
name = ctk.CTkLabel(inner_frame,text='click here',text_color='green',font=('ariel',25,'bold'))
name.place(relx=0.51,y=265,anchor='center')
close_button = ctk.CTkButton(
        inner_frame,
        text="❌",
        width=20,
        height=20,
        corner_radius=2,
        fg_color="#222",
        hover_color="#222",
        text_color="#999",
        cursor='hand2',
        font=("Arial", 9),
        command=root.destroy

    )
close_button.place(x=370,y=6)
root.mainloop()
