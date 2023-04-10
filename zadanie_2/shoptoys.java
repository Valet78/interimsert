package zadanie_2;

import java.util.HashMap;

public class shoptoys {

    public static void main(String[] args) {
        UI intface = new UI();
        FM fMan = new FM();
        HashMap <String, Toys> mapToys = new HashMap<String, Toys>();
        mapToys = fMan.LoadFile();      // Загрузка данных из файла
        
        int ind = intface.Hello();      // Приветствие и выбор Гость или Сотрудник
               
        intface.SelUs(ind, mapToys);    //
        
        // fMan.SaveFile(mapToys);
        
        



    }
    
}
