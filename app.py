from flask import Flask, render_template, request, send_file
import cv2
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Encryption function with password
def encrypt_image(image_path, message, password, output_path):
    img = cv2.imread(image_path)
    if img is None:
        return False, "Image not found!"

    encoded_message = password + ":" + message + "$END$"  # Append end marker
    height, width, _ = img.shape
    n, m = 0, 0  # Store only in Blue channel

    for char in encoded_message:
        img[n, m, 0] = ord(char)  # Store in Blue channel
        m += 1
        if m >= width:
            m = 0
            n += 1
        if n >= height:
            return False, "Message too long for image!"

    cv2.imwrite(output_path, img)
    return True, output_path

# Decryption function with password
def decrypt_image(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        return False, "Image not found!"

    extracted_text = ""
    height, width, _ = img.shape
    n, m = 0, 0  # Read only from Blue channel

    while True:
        char = chr(img[n, m, 0])
        if extracted_text.endswith("$END$"):  # Stop at end marker
            extracted_text = extracted_text[:-5]  # Remove marker
            break
        extracted_text += char
        m += 1
        if m >= width:
            m = 0
            n += 1
        if n >= height:
            break

    if ":" in extracted_text:
        extracted_password, secret_message = extracted_text.split(":", 1)
        if extracted_password == password:
            return True, secret_message
        else:
            return False, "Incorrect password!"
    
    return False, "Decryption failed!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    if request.method == "POST":
        file = request.files["image"]
        message = request.form["message"]
        password = request.form["password"]
        output_path = os.path.join(UPLOAD_FOLDER, "encrypted.png")

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        success, result = encrypt_image(file_path, message, password, output_path)
        if success:
            return send_file(output_path, as_attachment=True)
        else:
            return render_template("encrypt.html", error=result)
    return render_template("encrypt.html")

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    if request.method == "POST":
        file = request.files["image"]
        password = request.form["password"]

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        success, message = decrypt_image(file_path, password)
        return render_template("decrypt.html", message=message if success else "Error: " + message)
    return render_template("decrypt.html")

if __name__ == "__main__":
    app.run(debug=True)
