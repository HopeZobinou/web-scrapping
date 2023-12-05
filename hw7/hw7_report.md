# HW7 - Report
### Hope Zobinou
### DATA 440, Fall 2023 
### 11/30/2023

# Q1
Find 3 users who are closest to you in terms of age, gender, and occupation.  

For each of those 3 users:
* *A: What are their top 3 (favorite) films?*
* *B: What are their bottom 3 (least favorite) films?*

Based on the movie values in those 6 tables (3 users X (favorite + least favorite)), choose a user that you feel is most like you.  Feel free to note any outliers (e.g., "I mostly identify with user 123, except I did not like "Ghost" at all").  You can investigate more than just the top 3 and bottom 3 movies to find your best match.

This user is the *substitute you*.  
## Answer

I am 21, male, and a student. The 3 users that are close to me based on age, gender, and occupation are "81|21|M|student|21218", "323|21|M|student|19149", "259|21|M|student|48823." 

||81's top 3|||
|---|---|---|---|
|**Movie**|
| Time to Kill, A (1996)|
| Schindler's List (1993)|
| Silence of the Lambs, The (1991)|

|| 81's bottom 3|||
|---|---|---|---|
|**Movie**|
| Very Brady Sequel, A (1996)|
| Father of the Bride Part II (1995)|
| Beverly Hills Ninja (1997)|

|| 323's top 3|||
|---|---|---|---|
|**Movie**|
| Godfather, The (1972)|
| Michael Collins (1996)|
| Braveheart (1995)|

|| 323's bottom 3|||
|---|---|---|---|
|**Movie**|
| Jungle2Jungle (1997)|
| Murder at 1600 (1997)|
| Money Talks (1997)|

|| 259's top 3|||
|---|---|---|---|
|**Movie**|
| Usual Suspects, The (1995)|
| Apocalypse Now (1979)|
| Titanic (1997)|

|| 259's bottom 3|||
|---|---|---|---|
|**Movie**|
| Mars Attacks! (1996)|
| Beautiful Girls (1996)|
| Full Monty, The (1997)|

I don't enjoy watching movies so I haven't a lot of movies. The only movies I recognize are Godfather and Braveheart. Those 2 movies are in 323's top 3 rated movies. I like those movies as well. I don't know the movies in his bottom 3. 323 is most like me.

Below are pictures of the process I took to get the user and the movie info.

![q1_closest_users](https://github.com/HopeZobinou/data440/assets/81893993/d7ecbf85-83b3-4cd1-b8c5-12f037434a3c)
![q1_looking_for_top_bottom_movies](https://github.com/HopeZobinou/data440/assets/81893993/5fbc06d7-cb59-4045-a5ee-e8fb720cb3e8)
![q1_finding_the_movies](https://github.com/HopeZobinou/data440/assets/81893993/a0089612-c589-4a1e-a603-33eec5a532b9)

## Discussion
I opened the user, data, and item files in Notepad++. In those files, I used "control f" to search for the users and their top/bottom-ranked movies.  

# Q2

Based on the ratings that users have given to the movies, answer the following questions:

* *A: Which 5 users are most correlated to the* substitute you *(i.e., which 5 users rate movies most similarly to the* substitute you?)
* *B: Which 5 users are least correlated (i.e., negative correlation)?*


## Answer
A: User 98, 88, 172, 571, 369
B: User 375, 93, 358, 855, 845

Below is the code I used to get the answer.

```python
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

if __name__ == "__main__":

    user_ratings = load_data('c:/Users/hopez/Documents/Data440/Homework7/u.data')
    #print(user_ratings)
    #print(user_ratings.keys())

    print(find_correlated_users(user_ratings, '323'))
```
Here is an image of the output

![q2_output](https://github.com/HopeZobinou/data440/assets/81893993/d7d465bd-76fe-464c-87a4-0e62705f3a6d)

## Discussion
I used the functions provided by the professor to build the backbone of the 2 functions I made-Reference 1. With the first function, I wanted to read in the data from the data file and load it into a dictionary so I could work with it like how it is in the example code. The next function just does list comprehension of calling sim_pearson and sorting them. Once the list is sorted you can get the top and bottom 5 by using "[:n]" and "[-n:]" respectively.   

# Q3
Compute ratings for all the films that the *substitute you* has not seen.  

Provide a list of the top 5 recommendations for films that the *substitute you* should see.  

Provide a list of the bottom 5 recommendations (i.e., films the *substitute you* is almost certain to hate).

## Answer
Top 5 films that user 323 should see: Swept from the Sea (1997), Scarlet Letter, The (1926), Germinal (1993), Line King: Al Hirschfeld, The (1996), Pompatus of Love, The (1996).

Bottom 5 films user 323 would hate: Broken English (1996), Boys, Les (1997), Jerky Boys, The (1994), Awfully Big Adventure, An (1995), Last Summer in the Hamptons (1995).

```python
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
    unseen_movies = get_unseen_movies(user_ratings, '323')
    rankings = predict_ratings(user_ratings, '323')

    top_5_rec = sorted(rankings)[-5:]
    bottom_5_rec = sorted(rankings)[:5]

    print(top_5_rec)
    print()
    print(bottom_5_rec)
```

## Discussion
I made 2 functions to solve this. The first function just collects all the movies the user hasn't seen by subtracting a list of all the movies and the movies seen by the user. The second function calculates the ratings and sorts them. 2 dictionaries, (total) one that Keeps a running total of weighted ratings for each movie, and (sim_sums) keeps track of the sum of the similarity scores for each movie that users similar to the target user have rated. together bother can be used in the Weighted Avg = Weighted Total / Similarity Total formula-Reference 2.   

# Q4
Choose your (the real you, not the *substitute you*) favorite and least favorite film from the list of 1,682 movies in `u.item`.  
For each film, generate a list of the top 5 most correlated and bottom 5 least correlated films. 

*Q: Based on your knowledge of the resulting films, do you agree with the results?*  In other words, do you personally like/dislike the resulting films?  
* If you have not heard of the recommended movies, search for the movie's trailer on YouTube and watch it before you answer.  If you do this, include the link to the trailer in your report.  For example, the [trailer for "Top Gun (1986)"](https://www.youtube.com/watch?v=xa_z57UatDY) was found by searching for "top gun 1986 trailer" on Google. 

## Answer
My favorite movie from this list is Harriet the Spy (1996). My least favorite movie from this list is Jackie Chan's First Strike (1996).

Top 5 correlated to Harriet the Spy: Killing Zoe (1994), xDeath and the Maiden (1994), xOnce \Upon a Time in the West (1968), \Fearless (1993), \Selena (1997).

Bottom 5 least correlated to Harriet the Spy: \Race the Sun (1996), \Widows' Peak (1994), \Dracula: Dead and Loving It (1995), Simple Twist of Fate, A (1994), \Shallow Grave (1994).

Top 5 correlated to Jackie Chan's First Strike: \Underworld (1997), \Funny Face (1957), \To Live (Huozhe) (1994), \Two Bits (1995), \Loch Ness (1995).

Bottom 5 least correlated to Jackie Chan's First Strike: \Horseman on the Roof, The (Hussard sur le toit, Le) (1995), \Misérables, Les (1995), xStrawberry and Chocolate (Fresa y chocolate) (1993), xTop Hat (1935), \Kissed (1996).

["Trailer for Killing Zoe"] (https://www.youtube.com/watch?v=_tjzuutVnzs&t=5s)
["Trailer for Death and the Maiden"] (https://www.youtube.com/watch?v=MxR1pHaMpcY&t=3s)
["Trailer for Once Upon a Time in the West"] (https://www.youtube.com/watch?v=c8CJ6L0I6W8&t=84s)
["Trailer for Fearless"] (https://www.youtube.com/watch?v=Tm5jBa4LzxQ&t=2s)
["Trailer for Selena"] (https://www.youtube.com/watch?v=EVMSuZXEz4s&t=2s)

["Trailer for Race the Sun"] (https://www.youtube.com/watch?v=tZ1CGEFd6kw)
["Trailer for Widows' Peak"] (https://www.youtube.com/watch?v=_Z0NmfGwnUc)
["Trailer for Dracula: Dead and Loving It"] (https://www.youtube.com/watch?v=ctsxTvTQUZI)
["Trailer for Simple Twist of Fate"] (https://www.youtube.com/watch?v=Mt2__27L358)
["Trailer for Shallow Grave"] (https://www.youtube.com/watch?v=m_kbECzNnnk)

["Trailer for Underworld"] (https://www.youtube.com/watch?v=uuEu82y8u1o)
["Trailer for Funny Face"] (https://www.youtube.com/watch?v=Hs6ASCq9YtY)
["Trailer for To Live"] (https://www.youtube.com/watch?v=IhRgMU0wyB8)
["Trailer for Two Bits"] (https://www.youtube.com/watch?v=I7iDEt9s2DA)
["Trailer for Loch Ness"] (https://www.youtube.com/watch?v=L90001PVzec)

["Trailer for Horseman on the Roof"] (https://www.youtube.com/watch?v=xFAD_lsdGAw)
["Trailer for Misérables, Les"] (https://www.youtube.com/watch?v=DvP_b_0pcI0) 
["Trailer for Strawberry and Chocolate"] (https://www.youtube.com/watch?v=qWv7dKxWhz4)
["Top Hat"] (https://www.youtube.com/watch?v=vbMpecOKoDY)
["Trailer for Kissed"] (https://www.youtube.com/watch?v=AakbRH_71gE)

Below is the code and output for this question.

```python
    movies = transformPrefs(user_ratings)

    print(topMatches(movies, '929')) #Movie = Harriet the Spy (1996)
    print(bottomMatches(movies, '929'))
    print()
    print(topMatches(movies, '455')) #Movie = Jackie Chan's First Strike (1996)
    print(bottomMatches(movies, '455')) 
```

![q4_output](https://github.com/HopeZobinou/data440/assets/81893993/e35ff5ce-84a7-47c8-add7-fd25db98340f)

## Discussion
I agree with the recommendations given. The movie titles with an 'x' next to it, I disagree with its placement, and for the titles with a '\', I agree with the placement.

# References

* Reference 1, <https://github.com/anwala/teaching-web-science/blob/main/fall-2022/week-11/data_440_03_f22_mod_11_pci_ch_02.ipynb>
* Reference 2, <https://docs.google.com/presentation/d/1v-NjOb3ZFroOWbCMG-gQWQrqj6xKXWmh/edit#slide=id.p52>
