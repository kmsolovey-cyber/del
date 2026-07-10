import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from VisionProcessor import VisionProcessor

class ChromaticApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chromatic Threshold App")

        self.processor = VisionProcessor("image.jpg")
        self.mask = None

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.tab_control = ttk.Frame(self.notebook)
        self.tab_result = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_control, text="Контроль")
        self.notebook.add(self.tab_result, text="Результат")

        self.scale = ttk.Scale(self.tab_control, from_=0, to=255, orient=tk.HORIZONTAL)
        self.scale.set(128)
        self.scale.pack(fill="x", padx=10, pady=10)

        self.btn_run = ttk.Button(self.tab_control, text="Выполнить", command=self.run)
        self.btn_run.pack(pady=10)

        self.btn_save = ttk.Button(self.tab_control, text="Сохранить маску", command=self.save)
        self.btn_save.pack(pady=10)

        self.canvas = tk.Label(self.tab_result)
        self.canvas.pack()

        self.root.mainloop()

    def run(self):
        thr = int(self.scale.get())
        self.mask = self.processor.get_cr_mask(thr)

        rgb = cv2.cvtColor(self.mask, cv2.COLOR_GRAY2RGB)
        pil = Image.fromarray(rgb)
        tk_img = ImageTk.PhotoImage(pil)

        self.canvas.img = tk_img
        self.canvas.config(image=tk_img)

    def save(self):
        if self.mask is not None:
            cv2.imwrite("cr_mask_output.png", self.mask)
            print("Сохранено: cr_mask_output.png")

if __name__ == "__main__":
    ChromaticApp()
