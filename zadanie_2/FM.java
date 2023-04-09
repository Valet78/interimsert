package zadanie_2;


import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.util.HashMap;
// import java.util.Map;

public class FM {
    
    public FM(){}

    public HashMap<String, Toys> LoadFile(){
        // String pathFile  = FileSystems.getDefault().getPath("").toAbsolutePath().toString() + "\\zadanie_2\\base.csv";
        HashMap<String, Toys> resMap = new HashMap<String, Toys>();
        
        
        
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
                    fileCSV.append(val.GetId());
                    fileCSV.append(";");
                    fileCSV.append(val.GetName());
                    fileCSV.append(";");
                    fileCSV.append(Integer.toString(val.GetNumber()));
                    fileCSV.append(";");
                    fileCSV.append(Double.toString(val.GetRate()));
                    fileCSV.append("\n");
                } catch (IOException e) {
                    
                    // e.printStackTrace();
                }
                

                
            });

            fileCSV.flush(); 
            fileCSV.close(); 


        } catch (Exception e) {
            
        }




    }
    
    
}
