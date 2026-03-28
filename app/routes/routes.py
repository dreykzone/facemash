from flask import Blueprint, render_template, jsonify, request
from app.services.person import insert_rating, get_random_persons, get_ranking_persons

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@routes.route("/ranking", methods=["GET"])
def ranking():
    return render_template("ranking.html")

@routes.route("/api/v0/persons", methods=["GET"])
def vote_persons():
    result, status_code  = get_random_persons()
    return jsonify(result), status_code
    
@routes.route("/api/v0/persons", methods=["PUT"])
def update_rating():
    data = request.get_json()
    id_winner = data.get("id_winner")
    id_loser = data.get("id_loser")
    
    if not id_winner or not id_loser:
        return jsonify({"ID dos usuários são obrigatórios."}), 400
    
    if not isinstance(id_winner, int) or not isinstance(id_loser, int):
        return jsonify({"ID dos usuários não são valores inteiros."}), 400
    
    result, status_code = insert_rating(id_winner, id_loser)
    
    return jsonify(result), status_code
    
@routes.route("/api/v0/ranking", methods=["GET"])
def get_ranking():
    result, status_code = get_ranking_persons()
    return jsonify(result), status_code