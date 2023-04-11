package zadanie_2;

// import java.sql.Date;
// import java.util.Calendar;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;
import java.util.Scanner;


public class UI {
    private boolean status = false;
    static int numPlay = 0, rand = 0;
    
    public UI(){}

    public boolean GetStatus(){return this.status;}
    public void SetStatus(boolean inStatus){this.status = inStatus;}
    
    public int Hello(){                         // Приветствие и выбор Гость или Сотрудник
        int input = 0;
        Scanner inStr = new Scanner(System.in);
        Clr();
        System.out.println();
        System.out.println("Добро пожаловать в магазин игрушек HappyToys.");
        System.out.println("Иногда мы проводим розыгрыш игрушек, и у Вас есть шанс");
        System.out.println("стать обладателем одной из них.\n");

        System.out.println("Подскажите, Вы гость или сотрудник магазина?");
        System.out.println("1. Вы - гость.");
        System.out.println("2. Вы - сотрудник.");
        System.out.println("___________________________");
        System.out.println("0. Для выхода из программы.");
        input = inStr.nextInt();
        while (input < 0 || input > 2) {
            System.out.println("Введите '1', '2' или '0', только эти значения!");
            input = inStr.nextInt();
        }
        // inStr.close();    
        return input;        
    }

    // Выбор действия Гостя
    public int Guest(){
        int input = 0;
        Scanner inStr1 = new Scanner(System.in);
        Clr();
        System.out.println();
        System.out.println("Вы желаете:");
        System.out.println("1. Выбрать игрушки для покупки.");
        System.out.println("2. Поучаствовать в розыгрыше.");
        
        input = inStr1.nextInt();
        while (input != 1 && input != 2) {
            System.out.println("Введите '1' или '2'!");
            input = inStr1.nextInt();
        }
        return input;
        // inStr1.close();
                
    }    
    
    public HashMap <String, Toys> GuestTodo(int inSel, HashMap <String, Toys> inMap){     // Действий Гостя
        int id = 1, input = 0, kol = 0;
        String indt = "";
        play pLay = new play();
        Random rnd = new Random();
        Scanner inStr2 = new Scanner(System.in);
        HashMap<Integer,String> numStrok = new HashMap<Integer,String>();
        switch (inSel){
            case 1:            
                Clr();
                System.out.println("Вот какие игрушки есть у нас в магазине:");    
                for(HashMap.Entry <String, Toys> item : inMap.entrySet()){
                    numStrok.put(id, item.getKey());
                    System.out.printf("%d. %s в количестве %d шт. по цене %.2f руб. за шт.\n", id, item.getValue().GetName(), item.getValue().GetNumber(), item.getValue().GetPrice());
                    id ++;
                }
                System.out.println("\n Сделайте свой выбор и внесите указанную сумму.");
                input = inStr2.nextInt();
                while (input >= id || input <= 0) {
                    System.out.println("Введите номер строки!");
                    input = inStr2.nextInt();
                }
                indt = numStrok.get(input);
                kol = inMap.get(indt).GetNumber();
                System.out.print("Введите необходимое количество: ");
                input = inStr2.nextInt();
                while(input > kol){
                    System.out.print("У нас нет такого количества. Введите адекватное значение: ");
                    input = inStr2.nextInt();
                }
                System.out.printf("С Вас %.2f руб. Не забудбте их передать сотруднику магазина.", inMap.get(indt).GetPrice() * input);
                inMap.get(indt).SetNumber(kol - input);

                this.status = true;                  

                System.out.println("\nДля продолжения нажмите Enter.");
                inStr2.nextLine();
                break;
                                // ******************    Розыгрыш    ******************** //
                case 2:                  
                HashMap<String, Integer> playMap = new HashMap<String, Integer>();
                List <String> playList = new ArrayList<String>();
                // List <String> rndList = new ArrayList<String>();
                // List <Integer> indList = new ArrayList<Integer>();
                int size = playList.size();

                playMap = pLay.SumToys(inMap);
                playMap.forEach((kk, vv) -> {
                    for (int ii = 0; ii < vv; ii++){
                        playList.add(kk);
                    }                
                });
                
                size = playList.size();
                System.out.printf("Итак, в разыгрыше участвует %d игрушек из %d.\n", size, pLay.GetSumm());
                System.out.print("Система случайным образом распределила Вам следующую игрушку:");
                rand = rnd.nextInt(0,  size);
                System.out.println(inMap.get(playList.get(rand)).GetName() + ". Поздравляем!");
                id = inMap.get(playList.get(rand)).GetNumber();
                if (id > 0){
                    inMap.get(playList.get(rand)).SetNumber(id - 1);
                }
                this.status = true;

                /* 
                for (int ii = 0; ii < size; ii++){
                    rand = rnd.nextInt(0,  size);
                    while (indList.contains(rand)){
                        rand = rnd.nextInt(0,  size + 1);
                    }
                    indList.add(rand);
                }
                                        
                 */
                
                
                System.out.println("\nДля продолжения нажмите Enter.");
                inStr2.nextLine();
                break;
        }
        return inMap;

    }

    public int Sotr(){
        int input = 0;
        Scanner inStr3 = new Scanner(System.in);


        Clr();
        System.out.println("Выберите действия:");
        System.out.println("1. Просмотреть записи");
        System.out.println("2. Удалить запись");
        System.out.println("3. Добавить запись");
        System.out.println("4. Редактировать запись");
        
        input = inStr3.nextInt();
        while (input > 4 || input <= 0) {
            System.out.println("Введите указанные значения!");
            input = inStr3.nextInt();
        }
        return input;
    }
    
    public HashMap<String,Toys> SotrToDo(int inInd, HashMap<String,Toys> inMap){
        int id = 1, input = 0;
        String idToys = "", inpTxt;
        LocalDateTime dt = LocalDateTime.now();
        Scanner inStr4 = new Scanner(System.in);
        Scanner inStr5 = new Scanner(System.in);
        HashMap<Integer,String> numStrok = new HashMap<Integer,String>();
        Clr();
        switch(inInd){
            case 1:                 // Просмотреть записи
                System.out.println("Имеются следующие записи:");
                for(HashMap.Entry <String, Toys> item : inMap.entrySet()){
                    System.out.printf("%d. %s \t%d шт. \tпо цене %.2f руб. за шт. \t rate = %.1f\n", id, item.getValue().GetName(), 
                                item.getValue().GetNumber(), item.getValue().GetPrice(), item.getValue().GetRate());
                    id ++;
                }
                SetStatus(false);
                System.out.println("\nДля продолжения нажмите Enter.");
                inStr4.nextLine();
                break;

            case 2:                // Удалить запись
                System.out.println("Имеются следующие записи:");    
                for(HashMap.Entry <String, Toys> item : inMap.entrySet()){
                    numStrok.put(id, item.getKey());
                    System.out.printf("%d. %s \t%d шт. \tпо цене %.2f руб. за шт. \t rate = %.1f\n", id, item.getValue().GetName(), 
                                item.getValue().GetNumber(), item.getValue().GetPrice(), item.getValue().GetRate());
                    id ++;
                }
                System.out.println("\nКакую запись Вы желаете удалить?");
                input = inStr4.nextInt();
                while (input >= id || input <= 0) {
                    System.out.println("Введите номер строки!");
                    input = inStr4.nextInt();
                }
                idToys = numStrok.get(input);
                System.out.printf("%d. %s будет удалена.\n", input, inMap.get(idToys) );
                inMap.remove(idToys); 
                
                SetStatus(true);
                System.out.println("\nДля продолжения нажмите Enter.");
                inStr4.nextLine();
                break;
                
            case 3:             // Добавить запись
                String nameTXT, numberTXT, priceTXT, rateTXT;
                System.out.println("Введите данные новой записи: \n");
                System.out.print("Наименование: ");
                nameTXT = inStr4.nextLine();
                System.out.print("Количество: ");
                numberTXT = inStr4.nextLine();
                System.out.print("Цена: ");
                priceTXT = inStr4.nextLine();
                System.out.print("Вероятность выпадения: ");
                rateTXT = inStr4.nextLine();

                System.out.println("\nНовая запись будет добавлена.");
                
                idToys = (String) dt.format(DateTimeFormatter.ofPattern("uuuuMMddHHmm"));
                
                int numInt = Integer.parseInt(numberTXT); 
                double prDouble = Double.parseDouble(priceTXT);
                double rtDouble = Double.parseDouble(rateTXT);
                
                inMap.put(idToys, new Toys(nameTXT, numInt, prDouble, rtDouble));
                SetStatus(true);
                System.out.println("\nДля продолжения нажмите Enter.");
                inStr4.nextLine();

                break;
            case 4:             // Редактировать запись
                System.out.println("Имеются следующие записи:");    
                for(HashMap.Entry <String, Toys> item : inMap.entrySet()){
                    numStrok.put(id, item.getKey());
                    System.out.printf("%d. %s \t%d шт. \tпо цене %.2f руб. за шт. \t rate = %.1f\n", id, item.getValue().GetName(), 
                                item.getValue().GetNumber(), item.getValue().GetPrice(), item.getValue().GetRate());
                    id ++;
                }
                System.out.println("\nКакую запись Вы желаете изменить?");
                input = inStr4.nextInt();
                while (input >= id || input <= 0) {
                    System.out.println("Введите номер строки!");
                    input = inStr4.nextInt();
                }
                idToys = numStrok.get(input);

                System.out.println();
                System.out.println("Выберите поле, которое Вы хотите изменить:");
                System.out.println("1. Наименование");
                System.out.println("2. Количество");
                System.out.println("3. Значение цены");
                System.out.println("4. Весовой коэффициент");

                input = inStr4.nextInt();
                while (input > 4 || input <= 0) {
                    System.out.println("Введите значение Вашего выбора!");
                    input = inStr4.nextInt();
                }

                switch (input) {
                    case 1:
                        System.out.println();
                        System.out.print("Введите новое наименование: ");
                        inpTxt = inStr5.nextLine();
                        inMap.get(idToys).SetName(inpTxt);
                        break;
                    case 2:
                        System.out.println();
                        System.out.print("Введите новое значение количества: ");
                        inpTxt = inStr5.nextLine();
                        inMap.get(idToys).SetNumber(Integer.parseInt(inpTxt));
                        break;
                    case 3:
                        System.out.println();
                        System.out.print("Укажите новую цену: ");
                        inpTxt = inStr5.nextLine();
                        inMap.get(idToys).SetPrice(Double.parseDouble(inpTxt));
                        break;
                    case 4:
                        System.out.println();
                        System.out.print("Укажите новое значение весового коэффициента: ");
                        inpTxt = inStr5.nextLine();
                        inMap.get(idToys).SetRate(Double.parseDouble(inpTxt));
                        break;
                }

                               
                SetStatus(true);
                
                System.out.println("\nДля продолжения нажмите Enter.");
                inStr4.nextLine();






                break;



        }



        return inMap;
    }




    private void Clr(){
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
}
