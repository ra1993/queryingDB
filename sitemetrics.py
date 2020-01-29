import sqlite3
#in your terminal you can access database by using sqlite3 <dbname> .q is to quit db terminal
with sqlite3.connect("sitemetrics.db") as conn:
    cursor = conn.cursor()


#### Answer the following questions in this file, with the results and the sql you wrote to get it.
#-------------

##### How many people are from California?  
    cursor.execute("""SELECT name FROM users WHERE state = "CA" """)
    cali = cursor.fetchall()
    #print(len(cali))  14 people

##### Who has the most page views? How many do they have, and where are they from?
    cursor.execute("""SELECT * FROM users WHERE page_views = (SELECT MAX(page_views) FROM users)""")
    max_views = cursor.fetchall()
    #print(max_views)
    #Edison Mcintyre

##### Who has the least page views? How many do they have and where are they from?
    cursor.execute("""SELECT * FROM users WHERE page_views = (SELECT MIN(page_views) FROM users)""")
    min_views = cursor.fetchall()
    #print(min_views)
    #Hattie Ross from MA

##### Who are the most recent visitors to the site?(at least 3)
    cursor.execute("""SELECT * FROM users ORDER BY last_visit DESC LIMIT 3;""")
    recent_views = cursor.fetchall()
    
    #Otha ORtiz, Selina Hardy, Terrance Allen
    #print(recent_views)

##### Who was the first visitor?
    cursor.execute("""SELECT * FROM users ORDER BY last_visit ASC LIMIT 1;""")
    first_view = cursor.fetchall()

    #print(first_view)
    #'Woodrow Duffy'

##### Who has an email address with the domain 'horse.edu'?
    cursor.execute("""SELECT * FROM users WHERE email LIKE "%@horse.edu%" """)
    horse_email = cursor.fetchall()

    print(horse_email)
    #Valentine Gonzales
##### How many people are from the city Graford?
    cursor.execute("""SELECT * FROM users where city = "Graford" """)
    graford_people = cursor.fetchall()
    
    #print(len(graford_people))
    #3 people

##### What are the names of all the cities that start with the letter V, in alphabetical order?
    cursor.execute("""SELECT DISTINCT city FROM users WHERE substr(city,1,1) = "V" """)
    v_cities = cursor.fetchall()

    print(v_cities)
    #('Van',), ('Valley View',), ('Victoria',), ('Vega',)

##### What are the names and home cities for people searched for the word "drain"?
    cursor.execute("""SELECT users.name, users.city FROM users
    JOIN user_searches ON users.id = user_searches.user_id
    JOIN search_terms ON search_terms.id = user_searches.term_id
    WHERE word = "drain" """)
    drain_users = cursor.fetchall()
    
    #print(list(drain_users))
    #('Nelly Beach', 'Graford'), ('Penelope Stein', 'Runaway Bay'), ('Tisha Gill', 'Bausell and Ellis'), ('Rolando Crowley', 'Buda')]

##### How many times was "trousers" a search term?
    cursor.execute (""" SELECT * FROM search_terms WHERE word = "trousers"
    """)
    trousers_num = cursor.fetchall()
    #print(len(trousers_num))
    #1 time

##### What were the search terms used by visitors who last visited on August 22 2014?
    cursor.execute("""SELECT search_terms.word FROM search_terms 
        JOIN user_searches ON search_terms.id = user_searches.term_id 
        JOIN users ON users.id = user_searches.user_id 
        WHERE last_visit = "2014-08-22" """)
    aug_22_searches = cursor.fetchall()

    #print(aug_22_searches)
    #[('sweet',), ('or',), ('left',), ('word',), ('female',), ('ball',)]

##### What was the most frequently used search term by people from Idaho?
    cursor.execute("""SELECT search_terms.word, COUNT(user_searches.term_id) AS cnt
            FROM search_terms 
            JOIN user_searches ON search_terms.id = user_searches.term_id 
            JOIN users ON users.id = user_searches.user_id 
            WHERE users.state LIKE "%ID%"
            GROUP BY search_terms.word ORDER BY cnt DESC LIMIT 1""")
    idaho_searches = cursor.fetchall()

    #print(idaho_searches)
    #[('tongue', 2)]
        

##### What is the name of user 391, and what are his search terms?
    user391 = [391]
    cursor.execute("""SELECT name FROM users WHERE id = ?;""" , user391)
    name391 = c.fetchall() #Stan Alston
    cursor.execute("""SELECT search_terms.word FROM search_terms 
        JOIN user_searches ON search_terms.id = user_searches.term_id 
        JOIN users ON users.id = user_searches.user_id 
        WHERE user_id = ?;""" , user391)
    search_terms_391 = cursor.fetchall() 
    
    #print(search_terms_391)
    #ornament, heat, sex, secret, dry
