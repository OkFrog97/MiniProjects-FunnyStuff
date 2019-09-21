class Movie {
    
    // Movie_information
    String title;
    String genre;
    int rating;
    
    // Movie_functions
    void playIt() {
        System.out.println("Play films");
    }
}

class MovieTestDrive {
    public static void main (String[] arts){
        Movie jocker = new Movie();
        jocker.title = "Jocker"; 
        jocker.genre = "Fantastic"; 
        jocker.rating = 10;
        
        jocker.playIt();
        System.out.println(jocker.title);
    }
}