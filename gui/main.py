import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
import os

class FashionClassifier:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fashion Classifier")
        self.root.geometry("350x200")
        self.setup_ui()
    
    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Fashion-MNIST Classifier", 
                 font=("Arial", 14, "bold")).pack(pady=(0, 20))
        
        ttk.Button(frame, text="Upload Image", 
                  command=self.upload_image).pack(pady=10)
        
        self.status = tk.StringVar(value="Ready")
        ttk.Label(frame, textvariable=self.status, 
                 foreground="blue").pack(pady=(15, 0))
    
    #ensures images are processed correctly
    def upload_image(self):
        file_path = filedialog.askopenfilename(
            title="Select image",
            filetypes=[("Images", "*.png *.jpg *.jpeg *.gif *.bmp *.webp")]
        )
        
        if not file_path:
            return
        
        self.status.set("Processing...")
        self.root.update()
        
        try:
            result = self.predict(file_path)
            filename = os.path.basename(file_path)
            
            self.status.set(f"{result['class']} ({result['confidence']})")
            
            messagebox.showinfo("Result", 
                f"File: {filename}\n"
                f"Prediction: {result['class']}\n"
                f"Confidence: {result['confidence']}")
                
        except Exception as e:
            self.status.set("Error occurred")
            messagebox.showerror("Error", str(e))
    
    def predict(self, file_path):
        with open(file_path, 'rb') as f:
            response = requests.post(
                "http://localhost:5001/predict", 
                files={'file': f}, 
                timeout=10
            )
        
        if response.status_code != 200:
            raise Exception("API request failed")
        
        return response.json()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FashionClassifier()
    app.run()
