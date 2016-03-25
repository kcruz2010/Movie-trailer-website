import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come live",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  #  noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#  Shows Toy Story's movie trailer


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  #  noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#  Shows Avatar's movie trailer


wolf_of_wallstreet = media.Movie("Wolf of Wallstreet",
                                 "an autobiography of Jordan Belfort ",
                                 "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",  #  noqa
                                 "https://www.youtube.com/watch?v=PQleT6BtCbE")

#  Shows Wolf of Wallstreet's movie trailer


good_will_hunting = media.Movie("Good will hunting",
                                "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life",  #  noqa
                                "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",  #  noqa
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")

#  Shows Good will hunting's movie trailer


stand_and_deliver = media.Movie("Stand and Deliver",
                                "The story of Jaime Escalante, a high school teacher who successfully inspired his dropout prone students to learn calculus",  #  noqa
                                "https://upload.wikimedia.org/wikipedia/en/1/1f/Stand_and_deliver.jpg", #  noqa
                                "https://www.youtube.com/watch?v=GRtjlUfqJNg")

#  Shows Stand and Deliver's movie trailer


the_pursuit_of_happyness = media.Movie("The pursuit of happyness",
                                       "A struggling salesman takes custody of his son as he's poised to begin a life-changing professional endeavor",  #  noqa
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Poster-pursuithappyness.jpg/220px-Poster-pursuithappyness.jpg",  #  noqa
                                       "https://www.youtube.com/watch?v=SYg7RRYKWGw")

#  Shows the pursuit of happyness' movie trailer


movies = [toy_story, avatar, wolf_of_wallstreet, good_will_hunting, stand_and_deliver, the_pursuit_of_happyness]
fresh_tomatoes.open_movies_page(movies)
