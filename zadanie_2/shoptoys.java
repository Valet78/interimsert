package zadanie_2;

import java.util.HashMap;

public class shoptoys {
    

    public static void main(String[] args) {
        UI intface = new UI();
        FM fMan = new FM();
        play pL = new play();
        HashMap <String, Toys> mapToys = new HashMap<String, Toys>();
        HashMap <String, Toys> mapTemp = new HashMap<String, Toys>();
        mapToys = fMan.LoadFile();      // Загрузка данных из файла
        
        int ind = intface.Hello();      // Приветствие и выбор Гость или Сотрудник
        while (ind == 1 || ind == 2) {      
            switch (ind){
                case 1:                 // Гость 
                    ind = intface.Guest();
                    mapTemp = intface.GuestTodo(ind, mapToys); // Продажа игрушки
                    // Если были внесены изменения в базу - пезаписываем её
                    if (intface.GetStatus()) {
                        fMan.SaveFile(mapTemp);
                        mapToys = fMan.LoadFile();
                    }       
                    break;
                
                case 2:                 // Сотрудник
                    ind = intface.Sotr();
                    mapTemp = intface.SotrToDo(ind, mapToys);
                    // Если были внесены изменения в базу - пезаписываем её
                    if (intface.GetStatus()) {
                        fMan.SaveFile(mapTemp);
                        mapToys = fMan.LoadFile();
                    }                 
                    break;
            }
        ind = intface.Hello();      // Приветствие и выбор Гость или Сотрудник
        }
        
        // fMan.SaveFile(mapToys);
        
        



    }
    
}
