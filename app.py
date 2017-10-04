from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug import secure_filename
import os, os.path

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/images/<imagename>")
def get_images(imagename):
    return send_from_directory(os.path.join(
            './','./'),imagename)

@app.route("/get-images-list")
def get_images_list():
    imgs = []
    path = "./"
    valid_images = [".jpg",".gif",".png", ".jpeg"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        else:
            imgs.append(f)
    return jsonify(imgs)

@app.route('/uploader', methods = ['POST'])
def file_uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return render_template('successful-upload.html')

# Change from get to delete
@app.route("/delete-image/<imagename>", methods = ['DELETE'])
def del_image(imagename):
    os.remove(os.path.join('./', imagename))
    return render_template('successfully-deleted.html')

if __name__ == "__main__":
    app.run()
