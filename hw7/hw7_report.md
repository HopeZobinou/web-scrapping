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
## Discussion

# Q3

## Answer

## Discussion

# References

* Insert Reference 1, <https://www.example.com>
* Insert Reference 2, <https://www.example.com/reallyreallyreally-extra-long-URI/>
