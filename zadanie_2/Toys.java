package zadanie_2;

public class Toys{
       
    private String name = "";
    private int number = 0;
    private double price = 0;
    private double rate = 0;    
    

    public Toys (String inName, int inNum, double inPrice, double inRate){
        this.name = inName;
        this.number = inNum;
        this.price = inPrice;
        this.rate = inRate;
    }


    public Toys(){
        this("Noname", 0, 0, 0);
    }

    public String GetName(){return this.name;}
    public int GetNumber(){return this.number;}
    public double GetPrice(){return this.price;}
    public double GetRate(){return this.rate;}    

    public void SetName(String inName){this.name = inName;}
    public void SetNumber(int inNumber){this.number = inNumber;}
    public void SetPrice (double inPrice) {this.price = inPrice;}
    public void SetRate(double inRate){this.rate = inRate;}

} 