package zadanie_2;

import java.util.HashMap;
import java.util.Scanner;


public class UI {
    // Scanner inStr = new Scanner(System.in);
    public UI(){}

    public int Hello(){
        int input = 0;
        Scanner inStr = new Scanner(System.in);

        System.out.println();
        System.out.println("Добро пожаловать в магазин игрушек HappyToys.");
        System.out.println("Иногда мы проводим розыгрыш игрушек, и у Вас есть шанс");
        System.out.println("стать обладателем одной из них.\n");

        System.out.println("Подскажите, Вы гость или сотрудник магазина?");
        System.out.println("Введите '1' если Вы гость и '2' если Вы сотрудник.");
        input = inStr.nextInt();
        while (input != 1 && input != 2) {
            System.out.println("Введите '1' если Вы гость и '2' если Вы сотрудник!");
            input = inStr.nextInt();
        }
        // inStr.close();    
        return input;        
    }


    public int Guest(){
        int input = 0;
        Scanner inStr1 = new Scanner(System.in);
        
        System.out.println();
        System.out.println("Вы желаете:");
        System.out.println("1. Выбрать игрушки для покупки.");
        System.out.println("2. Поучаствовать в розыгрыше.");
        input = inStr1.nextInt();
        while (input != 1 && input != 2) {
            System.out.println("Введите '1' или '2'!");
            input = inStr1.nextInt();
        }
        // inStr1.close();
        return input;        
    }    
    
    public void SelUs(int ind, HashMap <String, Toys> inMap){
        
        switch (ind){
            case 1:
                ind = Guest();
                GuestTodo(ind, inMap);
                
            break;
            case 2:
                // fMan.LoadFile();


            break;
        }

    }


    public void GuestTodo(int inSel, HashMap <String, Toys> inMap){

        switch (inSel){
            case 1:
                // System.out.println(inMap.get("02012023").GetName() + " - " +  inMap.get("02012023").GetId());
                
            break;
            case 2:


            break;
        }

    }
    
}
