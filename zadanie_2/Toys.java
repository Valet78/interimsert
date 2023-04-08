package zadanie_2;

public class Toys{
    private int id = 0;
    private String name = "";
    private int number = 0;
    private double rate = 0;


    public Toys(){
        this.id = 0;
        this.name = "Noname";
        this.number = 0;
        this.rate = 99.9;
    }

    public int GetId(){return this.id;}
    public String GetName(){return this.name;}
    public int GetNumber(){return this.number;}
    public double GetRate(){return this.rate;}

    public void SetId(int inId){this.id = inId;}
    public void SetName(String inName){this.name = inName;}
    public void SetNumber(int inNumber){this.number = inNumber;}
    public void SetRate(double inRate){this.rate = inRate;}

} 