def generate_ratings(winner_rating, loser_rating):
    K = 10
    expectation_winner = 1/(1 + 10 ** ((loser_rating-winner_rating) / 400) )
    expectation_loser = 1/(1 + 10 ** ((winner_rating-loser_rating) / 400) )
    rating_winner_new = winner_rating + K * (1 - expectation_winner)
    rating_loser_new = loser_rating + K * (0 - expectation_loser)
    
    dict_ratings = {
        'rating_winner_new': rating_winner_new,
        'rating_loser_new': rating_loser_new
    }
    
    return dict_ratings