public class PhraseOMatic {
    public static void main (String[] args){
            //Make three wordlists
            String[] wordListOne = 
                {"Круглосуточный","Трех-звездный","взаимный",
                "фронтэнд","проникающий","умный","шесть сигм","метод кратчайшего пути","динамичный"};
            
            String[] wordListTwo = 
                {"чистый продукт","умный","сетевой","использованный с выгодой","выровненный","общий","совместный","ускоренный"};
            
            String[] wordListThree = {"процесс","пункт разгрузки","талант","подход","тип структуры","портал","обзор","образец","пункт следования"};
            
            //find lenght of lists
            int oneLenght = wordListOne.lenght;
            int twoLenght = wordListTwo.lenght;
            int threeLenght = wordListThree.lenght;
            
            //genetate random numbers
            int rand1 = (int) (Math.random()*oneLenght);
            int rand2 = (int) (Math.random()*twoLenght);
            int rand3 = (int) (Math.random()*threeLenght);
            
            //make a phrase
            String phrase = wordListOne[rand1] + " " + wordListTwo[rand2] + " " + wordListThree[rand3];
            
            System.out.println(phrase);
    }
}