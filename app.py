from flask import Flask, request, render_template, redirect, url_for
import os
from verify_faces import verify_faces

app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Save uploaded files
        profile_pic = request.files["profilePic"]
        gov_id = request.files["govId"]

        profile_pic_path = os.path.join(app.config['UPLOAD_FOLDER'], "profile_picture.jpg")
        gov_id_path = os.path.join(app.config['UPLOAD_FOLDER'], "gov_id.jpg")

        profile_pic.save(profile_pic_path)
        gov_id.save(gov_id_path)

        # Verify faces
        is_verified, distance = verify_faces(profile_pic_path, gov_id_path)
        if is_verified:
            return render_template("index.html", message="Verification Successful!")
        else:
            return render_template("index.html", message="Verification Failed. Faces do not match.")

    return render_template("index.html", message="")

if __name__ == "__main__":
    app.run(debug=True)
