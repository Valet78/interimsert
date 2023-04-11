package zadanie_2;

import java.util.HashMap;

public class play {
    private static int summ = 0;

    public play(){}

    public int GetSumm(){return summ;}
    

    public HashMap<String, Integer> SumToys(HashMap<String, Toys> inMap){
               
        HashMap<String, Integer> sumType = new HashMap<String, Integer>();
        // Вычисляем общее количество игрушек
        inMap.forEach((kk, vv) -> {summ += vv.GetNumber(); });
        // В розыгрыше будет участвовать только 15% от общей суммы
        inMap.forEach((kk, vv) -> {
            int temp = (int) ((vv.GetNumber() * vv.GetRate()) / 100 );
            sumType.put(kk, temp);
        });

        return sumType;
    }


}
