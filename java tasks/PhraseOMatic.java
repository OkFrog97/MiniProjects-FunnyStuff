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
            int oneLength = wordListOne.length;
            int twoLength = wordListTwo.length;
            int threeLength = wordListThree.length;
            
            //genetate random numbers
            int rand1 = (int) (Math.random()*oneLength);
            int rand2 = (int) (Math.random()*twoLength);
            int rand3 = (int) (Math.random()*threeLength);
            
            //make a phrase
            String phrase = wordListOne[rand1] + " " + wordListTwo[rand2] + " " + wordListThree[rand3];
            
            System.out.println(phrase);
    }
}