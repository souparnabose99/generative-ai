from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from profile_summarizer import summarize_profile


load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary_and_facts, interests, profile_information, profile_pic_url = summarize_profile(name=name)
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
            "interests": interests.to_dict(),
            "profile_information": profile_information.to_dict(),
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)