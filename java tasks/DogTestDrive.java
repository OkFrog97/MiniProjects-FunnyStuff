class Dog {
    int size;
    String breed;
    String name;
    
    void bark() {
        System.out.println("Bow! WOw!");
    }
}

class DogTestDrive {
    public static void main(String[] args){
    // Проверочный код для класса DogTestDrive    
        Dog bim = new Dog();
        bim.size = 40;
        bim.bark();
    }
}