package zadanie_2;

import java.util.HashMap;

public class shoptoys {

    public static void main(String[] args) {
        UI intface = new UI();
        FM fMan = new FM();
        HashMap <String, Toys> mapToys = new HashMap<String, Toys>();
        mapToys = fMan.LoadFile();
        System.out.println(mapToys);
        int ind = intface.Hello();
        
        
        mapToys.put("02012023", new Toys("Tosha"));
        intface.SelUs(ind, mapToys);
        
        fMan.SaveFile(mapToys);
        
        



    }
    
}
