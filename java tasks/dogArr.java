class dogArr{
    String name;
    
    public static void main (String[] args){
        
        dogArr [] d = new dogArr[3];
        
        d[0] = new dogArr();
        d[1] = new dogArr();
        d[0].name = "Fido";
        
        System.out.println(d[0]);
        System.out.println(d[0].name);
        System.out.println(d[1].name);
        System.out.println(d[2]);
    }
}        