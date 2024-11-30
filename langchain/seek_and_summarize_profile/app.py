from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from profile_summarizer import summarize_profile


load_dotenv()
app = Flask(__name__)

