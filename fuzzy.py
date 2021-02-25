from simpful import *

def ping():
    return 'pong'

def get_mamdani_inference(age, bmi, blood_pressure, blood_glucose, cholesterol):
    FS = FuzzySystem()

    # Declaring Age Set

    A_1 = FuzzySet(function=Triangular_MF(a=0,b=0,c=37), term="young")
    A_2 = FuzzySet(function=Triangular_MF(a=30,b=37,c=44), term="middle")
    A_3 = FuzzySet(function=Trapezoidal_MF(a=37,b=48,c=100,d=100), term="old")

    FS.add_linguistic_variable("Age", LinguisticVariable([A_1, A_2, A_3], concept="Age", universe_of_discourse=[0,100]))

    # Declaring BMI Set

    BMI_1 = FuzzySet(function=Triangular_MF(a=0,b=0, c=18), term="low")
    BMI_2 = FuzzySet(function=Triangular_MF(a=12,b=18,c=24), term="medium")
    BMI_3 = FuzzySet(function=Trapezoidal_MF(a=18,b=28,c=40,d=40), term="high")

    FS.add_linguistic_variable("BMI", LinguisticVariable([BMI_1, BMI_2, BMI_3], concept="BMI", universe_of_discourse=[0,40]))

    # Declaring Blood Pressure Set

    BP_1 = FuzzySet(function=Triangular_MF(a=0, b=0,c=139), term="low")
    BP_2 = FuzzySet(function=Triangular_MF(a=126, b=139,c=153), term="medium")
    BP_3 = FuzzySet(function=Trapezoidal_MF(a=139,b=155,c=180,d=180), term="high")

    FS.add_linguistic_variable("BP", LinguisticVariable([BP_1,BP_2,BP_3], concept="Blood Pressure", universe_of_discourse=[0,180]))

    # Declaring Blood Glucose Set

    BG_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=89), term="low")
    BG_2 = FuzzySet(function=Triangular_MF(a=84, b=111,c=139), term="medium")
    BG_3 = FuzzySet(function=Trapezoidal_MF(a=111,b=155,c=250,d=250), term="high")

    FS.add_linguistic_variable("BG", LinguisticVariable([BG_1,BG_2,BG_3], concept="Blood Glucose", universe_of_discourse=[0,250]))

    # Declaring Cholesterol Set

    C_1 = FuzzySet(function=Triangular_MF(a=0,b=0,c=196), term="low")
    C_2 = FuzzySet(function=Triangular_MF(a=187, b=218,c=249), term="medium")
    C_3 = FuzzySet(function=Trapezoidal_MF(a=218,b=262,c=350,d=350), term="high")

    FS.add_linguistic_variable("Chl", LinguisticVariable([C_1,C_2,C_3], concept="Cholesterol", universe_of_discourse=[0,350]))

    #Declaring Output Set

    #O_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=3), term="low_risk")
    #O_2 = FuzzySet(function=Triangular_MF(a=3, b=5, c=7), term="medium_risk")
    #O_3 = FuzzySet(function=Triangular_MF(a=7, b=10, c=10), term="high_risk")
    O_1 = FuzzySet(function=Crisp_MF(a=0, b=3), term="low_risk")
    O_2 = FuzzySet(function=Crisp_MF(a=3, b=6), term="medium_risk")
    O_3 = FuzzySet(function=Crisp_MF(a=7, b=10), term="high_risk")
    FS.add_linguistic_variable("Risk", LinguisticVariable([O_1,O_2,O_3], concept="Risk", universe_of_discourse=[0,10]))

    # Define output crisp values
    #FS.set_crisp_output_value("low_risk",3)
    #FS.set_crisp_output_value("medium_risk",5)
    #FS.set_crisp_output_value("high_risk",8)

    #Declaring Rule
    R1 = "IF (BMI IS low) OR (BP IS low) OR (BG IS low) OR (Chl IS low) THEN (Risk IS low_risk)"
    R2 = "IF (BMI IS medium) OR (BP IS medium) OR (BG IS medium) OR (Chl IS medium) THEN (Risk IS medium_risk)"
    R3 = "IF (BMI IS high) OR (BP IS high) OR (BG IS high) OR (Chl IS high) THEN (Risk IS high_risk)"
    R4 = "IF (Age IS young) AND (BG IS high) THEN (Risk IS high_risk)"

    FS.add_rules([R1,R2,R3,R4])

    FS.set_variable("Age", age)
    FS.set_variable("BMI", bmi)
    FS.set_variable("BP", blood_pressure)
    FS.set_variable("BG", blood_glucose)
    FS.set_variable("Chl", cholesterol)
    return FS.Mamdani_inference(["Risk"])['Risk']

