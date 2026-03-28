from app.models.person import Persons
from app.ext.database import db
from app.helpers.elo import generate_ratings
from random import randint

def get_random_persons():
    try:
        results = Persons.query.all()
        data = [row.to_dict() for row in results]
        random_index = randint(0, len(data) - 1)
        first_person = data[random_index]
        data.pop(random_index)
        random_index = randint(0, len(data) - 1)
        second_person = data[random_index]
        data = [
            first_person, second_person
        ]
        print(data)
        return data, 200
    except:
        return {'messsage': "Erro Interno do Servidor."}, 500

def insert_rating(id_winner, id_loser):
    try:
        print(id_winner, id_loser)
        winner = Persons.query.get(id_winner)
        loser = Persons.query.get(id_loser)
        
        ratings = generate_ratings(winner.rating, loser.rating)
        
        winner.rating = ratings['rating_winner_new']
        loser.rating = ratings['rating_loser_new']
        
        db.session.commit()
 
        return {
            'message': "Operação realizada com sucesso"
        }, 200
    except:
        return {'messsage': "Erro Interno do Servidor."}, 500

def get_ranking_persons():
    try:
        results = Persons.query.order_by(Persons.rating.desc()).limit(10).all()
        data = [row.to_dict() for row in results]
        return data, 200
    except:
        return {'messsage': "Erro Interno do Servidor."}, 500

