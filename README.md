```
███████╗████████╗███████╗███╗   ██╗ ██████╗
██╔════╝╚══██╔══╝██╔════╝████╗  ██║██╔═══██╗
███████╗   ██║   █████╗  ██╔██╗ ██║██║   ██║
╚════██║   ██║   ██╔══╝  ██║╚██╗██║██║   ██║
███████║   ██║   ███████╗██║ ╚████║╚██████╔╝
╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝
```

# 📌 About the Project

This project implements **image steganography** to securely hide text messages within images using **Flask**. It enhances security with **password protection**, **blue-channel encoding**, and an **end marker** for accurate retrieval.

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/souvick98/Image-Stegnography.git
   ```
2. Install dependencies:
   ```bash
   pip install flask pillow opencv-python numpy werkzeug gunicorn
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```
4. Open in your browser:
   ```
   http://127.0.0.1:5000
   ```

## 🔑 Usage

1. **Upload an Image** – Choose an image to hide your message.
2. **Enter a Secret Message & Password** – Your message will be encrypted inside the image.
3. **Download the Encrypted Image** – Share it securely.
4. **Decrypt the Image** – Upload the encoded image and enter the password to retrieve the message.

## 🛠 Technologies Used

- 🐍 **Flask** – Web framework for backend development.
- 🎨 **HTML & CSS** – Frontend for a user-friendly interface.
- 🖼 **Pillow (PIL)** – Image processing for encoding and decoding text.
- 📷 **OpenCV** – Used for advanced image manipulation.
- 🔢 **NumPy** – Efficient pixel-level operations.
- 🔐 **Werkzeug** – Manages password security and encryption.
- ⚙ **Gunicorn** – WSGI server for deploying the Flask application.
- 🛠 **Visual Studio Code & IDLE** – Development environments.
- 🏗 **GitHub** – Version control and collaboration.

---
🚀 **Developed with ❤️ by [Souvick Das](https://github.com/souvick98)**


