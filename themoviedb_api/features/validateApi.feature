Feature: Validate TheMovieDb API

    Scenario: movie top rated HTTP response 200
        Given a valid api_key
        when requesting movie top rated
        then api should return valid data

    Scenario: movie top rated HTTP response 401
        Given a non valid api_key
        when requesting movie top rated with no valid data
        then api return http code error 401

    Scenario: movie top rated HTTP response 404
        Given a non api valid URL
        when requesting movie top rated with no valid url
        then api should return a HTTP error code 404

    Scenario: movie rating HTTP response 201
        Given a valid api_key and movie_id
        when request rating the movie
        then should return HTTP code 201

    Scenario: movie rating HTTP response 401
        Given a non valid api_key and valid movie_id
        when request rating the movie with no valid data
        then should return HTTP code 401
    
    Scenario: movie rating HTTP response 404
        Given a non valid URL
        when requesting rating the movie with no valid url
        then should return HTTP code 404