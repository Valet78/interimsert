package zadanie_2;


import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.util.HashMap;
// import java.util.Map;

public class FM {
    
    public FM(){}

    public HashMap<String, Toys> LoadFile(){
        String row;
        String pathFile  = FileSystems.getDefault().getPath("").toAbsolutePath().toString() + "\\zadanie_2\\base.csv";
        HashMap<String, Toys> resMap = new HashMap<String, Toys>();
        try {
            BufferedReader csvReader = new BufferedReader(new FileReader(pathFile));
                        
            while ((row = csvReader.readLine()) != null) { 
                String[] data = row.split(";"); 
                int nums = Integer.parseInt(data[2]);
                double prices = Double.parseDouble(data[3]);
                double rates = Double.parseDouble(data[4]);
                
                resMap.put(data[0], new Toys(data[1], nums, prices, rates));
                

            } 
            csvReader.close(); 

          
        } catch (Exception e) {
            System.out.println("Файл не найден!");
        }        
        
        return resMap;
    }
    
    public void SaveFile(HashMap<String, Toys> inMap){
        String pathFile  = FileSystems.getDefault().getPath("").toAbsolutePath().toString() + "\\zadanie_2\\base.csv";
        try {
            FileWriter fileCSV = new FileWriter(pathFile);

            // }
            inMap.forEach((ks, val) -> {
                try {
                    fileCSV.append(ks);
                    fileCSV.append(";");
                    fileCSV.append(val.GetName());
                    fileCSV.append(";");
                    fileCSV.append(Integer.toString(val.GetNumber()));
                    fileCSV.append(";");
                    fileCSV.append(Double.toString(val.GetPrice()));
                    fileCSV.append(";");
                    fileCSV.append(Double.toString(val.GetRate()));
                    fileCSV.append("\n");
                } catch (IOException e) {
                    System.out.println("Ошибка записи в файл!");                   
                }                
            });

            fileCSV.flush(); 
            fileCSV.close(); 

        } catch (Exception e) {
            System.out.println("Файл не найден!");
        }
    }    
}
