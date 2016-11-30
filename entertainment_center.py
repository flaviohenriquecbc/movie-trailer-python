import media
import fresh_tomatoes

#These are my favority movies that will will be stored using Classes
TRUMAN_SHOW = media.Movie("The Truman Show",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDIzODcyY2EtMmY2MC00ZWVlLTgwMzAtMjQwOWUyNmJjNTYyXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=loTIzXAS7v4")

IL_MOSTRO = media.Movie("Il mostro",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI2ODAwNDc2NF5BMl5BanBnXkFtZTcwMDMyMzIyMQ@@._V1_UY268_CR3,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=CE9h4jkNYoI")

THE_GODFATHER = media.Movie("The Godfather",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTUxOTdjMDMtMWY1MC00MjkxLTgxYTMtYTM1MjU5ZTJlNTZjXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY268_CR3,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

movies = [TRUMAN_SHOW, IL_MOSTRO, THE_GODFATHER]

#passes the movies list to the fresh_tomatoes class to load the interface
fresh_tomatoes.open_movies_page(movies)
