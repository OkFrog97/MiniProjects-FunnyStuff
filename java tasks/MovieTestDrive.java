class Movie {
    
    // Movie_information
    String title;
    String genre;
    int rating;
    
    // Movie_functions
    voit playIt() {
        System.out.println("Проигрывается фильм");
    }
}

class MovieTestDrive {
    
    Movie jocker = new Movie();
    
    jocker.title = "Jocker";
    jocker.genre = "Fantastic";
    jocker.rating = 10;
    
    jocker.playIt();
    System.out.println(jocker.title,"/n", jocker.genre, "/n", jocker.rating);
}