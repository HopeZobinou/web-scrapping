from math import sqrt

def sim_distance(prefs, p1, p2):
    '''
    Returns a distance-based similarity score for person1 and person2.
    '''

    # Get the list of shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[p1][item] - prefs[p2][item], 2)
                          for item in si])

    return 1 / (1 + sqrt(sum_of_squares))

def sim_pearson(prefs, p1, p2):
    '''
    Returns the Pearson correlation coefficient for p1 and p2.
    '''

    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    
    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0
    
    # Sum calculations
    n = len(si)
    
    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    
    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    
    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    
    # Calculate r (Pearson score)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r

def topMatches(
    prefs,
    person,
    n=5,
    similarity=sim_pearson,
):
    '''
    Returns the best matches for person from the prefs dictionary. 
    Number of results and similarity function are optional params.
    '''

    scores = [(similarity(prefs, person, other), other) for other in prefs
              if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def bottomMatches(
    prefs,
    person,
    n=5,
    similarity=sim_pearson,
):
    '''
    Returns the best matches for person from the prefs dictionary. 
    Number of results and similarity function are optional params.
    '''

    scores = [(similarity(prefs, person, other), other) for other in prefs
              if other != person]
    scores.sort()
    #scores.reverse()
    return scores[0:n]

def getRecommendations(prefs, person, similarity=sim_pearson):
    '''
    Gets recommendations for a person by using a weighted average
    of every other user's rankings
    '''

    totals = {}
    simSums = {}
    for other in prefs:
    # Don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # Ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                # The final score is calculated by multiplying each item by the
                #   similarity and adding these products together
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # Create the normalized list
    rankings = [(total / simSums[item], item) for (item, total) in
                totals.items()]
    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings

def transformPrefs(prefs):
    '''
    Transform the recommendations into a mapping where persons are described
    with interest scores for a given title e.g. {title: person} instead of
    {person: title}.
    '''

    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Flip item and person
            result[item][person] = prefs[person][item]
    return result

def load_data(file_path):
    #Load data from a file .data file and return a dictionary of users and their ratings.
    
    ratings = {} #Holds the data in u.data line by line
    with open(file_path, 'r') as file:
        for line in file:
            user, movie, rating, _ = line.split('\t') #Kkips the date part in the data
            ratings.setdefault(user, {})
            ratings[user][movie] = float(rating)
    return ratings

def find_correlated_users(prefs, target_user, n=5):
    #Find the top n most and least correlated users to the target user.

    scores = [(sim_pearson(prefs, target_user, other), other) for other in prefs if other != target_user]

    # Sort based on similarity
    scores.sort()
    scores.reverse()

    most_correlated = scores[:n]
    least_correlated = scores[-n:]

    return most_correlated, least_correlated

def get_unseen_movies(user_ratings, user): #Return a set of movies that the user has not yet rated.
    seen_movies = user_ratings[user]
    all_movies = set(movie for movies in user_ratings.values() for movie in movies)
    return all_movies - set(seen_movies)

def predict_ratings(user_ratings, target_user, similarity=sim_pearson): #Predicts ratings for all movies the target user hasn't seen, based on ratings from similar users
    totals = {} #Keeps a running total of weighted ratings for each movie.
    sim_sums = {} #Dictionary keeps track of the sum of the similarity scores for each movie that users similar to the target user have rated.

    for other in user_ratings:
        if other == target_user: #Skips the user itself
            continue

        sim = similarity(user_ratings, target_user, other)

        for movie in user_ratings[other]:
            if movie not in user_ratings[target_user]: #Only score movies target user hasn't seen

                #Similarity * Score
                totals.setdefault(movie, 0)
                totals[movie] += user_ratings[other][movie] * sim

                #Sum of similarities
                sim_sums.setdefault(movie, 0)
                sim_sums[movie] += sim

    #Create the normalized list
    #Weighted Avg = Weighted Total / Similarity Total 
    rankings = [(total / sim_sums[movie], movie) for movie, total in totals.items()] 

    return rankings


if __name__ == "__main__":

    user_ratings = load_data('c:/Users/hopez/Documents/Data440/Homework7/u.data')
    #print(user_ratings)
    #print(user_ratings.keys())

    #print(find_correlated_users(user_ratings, '323'))
    #print(get_unseen_movies(user_ratings, '323'))
    '''
    unseen_movies = get_unseen_movies(user_ratings, '323')
    rankings = predict_ratings(user_ratings, '323')

    top_5_rec = sorted(rankings)[-5:]
    bottom_5_rec = sorted(rankings)[:5]

    print(top_5_rec)
    print()
    print(bottom_5_rec)
    '''
    movies = transformPrefs(user_ratings)

    print(topMatches(movies, '929')) #Movie = Harriet the Spy (1996)
    print(bottomMatches(movies, '929'))
    print()
    print(topMatches(movies, '455')) #Movie = Jackie Chan's First Strike (1996)
    print(bottomMatches(movies, '455')) 

