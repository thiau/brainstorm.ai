from flask import Flask, request, jsonify, render_template
app = Flask(__name__, template_folder="../client", static_folder="../client")
