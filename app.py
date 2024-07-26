from flask import Flask, request, jsonify
from flask_cors import CORS
import qrcode
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

os.makedirs('static/qrcodes', exist_ok=True)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    name = request.form['name']
    email = request.form['email']
    qr_data = f"{name} | {email}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    file_path = f'static/qrcodes/{email}.png'
    img.save(file_path)

    return jsonify({'success': True, 'qr_code_url': file_path})

if __name__ == '__main__':
    app.run(debug=True)
