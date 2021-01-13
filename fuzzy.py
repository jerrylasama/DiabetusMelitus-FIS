from simpful import *

def ping():
    return 'pong'

def get_mamdani_inference(age, bmi, blood_pressure, blood_glucose, cholesterol):
    FS = FuzzySystem()

    # Declaring Age Set

    A_1 = FuzzySet(function=Trapezoidal_MF(a=0,b=0,c=0,d=37), term="low")
    A_2 = FuzzySet(function=Triangular_MF(a=30,b=37,c=44), term="middle")
    A_3 = FuzzySet(function=Triangular_MF(a=37,b=48,c=59), term="old")
    A_4 = FuzzySet(function=Trapezoidal_MF(a=48,b=56,c=59,d=100), term="very_old")

    FS.add_linguistic_variable("AGE", LinguisticVariable([A_1, A_2, A_3, A_4], concept="Age", universe_of_discourse=[0,10]))

    # Declaring BMI Set

    BMI_1 = FuzzySet(function=Trapezoidal_MF(a=0,b=0,c=0, d=18), term="low")
    BMI_2 = FuzzySet(function=Triangular_MF(a=12,b=18,c=24), term="medium")
    BMI_3 = FuzzySet(function=Triangular_MF(a=18,b=28,c=34), term="high")
    BMI_4 = FuzzySet(function=Trapezoidal_MF(a=28,b=32,c=34,d=40), term="very_high")

    FS.add_linguistic_variable("BMI", LinguisticVariable([BMI_1, BMI_2, BMI_3, BMI_4], concept="BMI", universe_of_discourse=[0,40]))

    # Declaring Blood Pressure Set

    BP_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=139), term="low")
    BP_2 = FuzzySet(function=Triangular_MF(a=126, b=139,c=153), term="medium")
    BP_3 = FuzzySet(function=Triangular_MF(a=139,b=155,c=171), term="high")
    BP_4 = FuzzySet(function=Trapezoidal_MF(a=155,b=164,c=171,d=180), term="very_high")

    FS.add_linguistic_variable("BloodPressure", LinguisticVariable([BP_1,BP_2,BP_3,BP_4], concept="Blood Pressure", universe_of_discourse=[0,180]))

    # Declaring Blood Glucose Set

    BG_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=89), term="low")
    BG_2 = FuzzySet(function=Triangular_MF(a=84, b=111,c=139), term="medium")
    BG_3 = FuzzySet(function=Triangular_MF(a=111,b=155,c=199), term="high")
    BG_4 = FuzzySet(function=Trapezoidal_MF(a=155,b=179,c=200,d=250), term="very_high")

    FS.add_linguistic_variable("BloodGlucose", LinguisticVariable([BG_1,BG_2,BG_3,BG_4], concept="Blood Glucose", universe_of_discourse=[0,250]))

    # Declaring Cholesterol Set

    C_1 = FuzzySet(function=Triangular_MF(a=0,b=0,c=196), term="low")
    C_2 = FuzzySet(function=Triangular_MF(a=187, b=218,c=249), term="medium")
    C_3 = FuzzySet(function=Triangular_MF(a=218,b=262,c=306), term="high")
    C_4 = FuzzySet(function=Trapezoidal_MF(a=262,b=280,c=306,d=350), term="very_high")

    FS.add_linguistic_variable("Cholesterol", LinguisticVariable([C_1,C_2,C_3,C_4], concept="Cholesterol", universe_of_discourse=[0,350]))

    #Declaring Output Set

    O_1 = FuzzySet(function=Triangular_MF(a=1, b=2, c=4), term="low_risk")
    O_2 = FuzzySet(function=Triangular_MF(a=5, b=6, c=7), term="medium_risk")
    O_3 = FuzzySet(function=Triangular_MF(a=8, b=9, c=10), term="high_risk")

    FS.add_linguistic_variable("Risk", LinguisticVariable([O_1,O_2,O_3], concept="Risk", universe_of_discourse=[1,10]))


    RULE1 = "IF (AGE IS low) OR (AGE IS middle) AND (BMI IS low) OR (Cholesterol IS medium) AND (BloodGlucose IS low) OR (BloodPressure IS medium) THEN (Risk IS low_risk)"
    RULE2 = "IF (AGE IS low) OR (AGE IS middle) AND (BMI IS high) OR (Cholesterol IS medium) AND (BloodGlucose IS high) OR (BloodPressure IS very_high) THEN (Risk IS high_risk)"
    RULE3 = "IF (AGE IS low) OR (AGE IS middle) AND (BMI IS medium) OR (Cholesterol IS high) AND (BloodGlucose IS medium) OR (BloodPressure IS low) THEN (Risk IS medium_risk)"
    RULE4 = "IF (AGE IS low) OR (AGE IS middle) AND (BMI IS medium) OR (Cholesterol IS low) AND (BloodGlucose IS low) OR (BloodPressure IS medium) THEN (Risk IS low_risk)"
    RULE5 = "IF (AGE IS old) OR (AGE IS very_old) AND (BMI IS low) OR (Cholesterol IS high) AND (BloodGlucose IS medium) OR (BloodPressure IS medium) THEN (Risk IS medium_risk)"
    RULE6 = "IF (AGE IS old) OR (AGE IS very_old) AND (BMI IS very_high) OR (Cholesterol IS very_high) AND (BloodGlucose IS high) OR (BloodPressure IS very_high) THEN (Risk IS high_risk)"
    RULE7 = "IF (AGE IS middle) OR (AGE IS old) AND (BMI IS medium) OR (Cholesterol IS medium) AND (BloodGlucose IS medium) OR (BloodPressure IS low) THEN (Risk IS medium_risk)"
    RULE8 = "IF (AGE IS middle) OR (AGE IS old) AND (BMI IS very_high) OR (Cholesterol IS medium) AND (BloodGlucose IS high) OR (BloodPressure IS very_high) THEN (Risk IS high_risk)"
    RULE9 = "IF (AGE IS middle) OR (AGE IS old) AND (BMI IS low) OR (Cholesterol IS very_high) AND (BloodGlucose IS low) OR (BloodPressure IS low) THEN (Risk IS medium_risk)"  
    #RULE1 = "IF (AGE IS low) OR (AGE IS middle) AND (BMI IS low) AND (BloodGlucose IS low) THEN (Risk IS low_risk)"
    #RULE2 = "IF (AGE IS low) OR (AGE IS middle) AND (BMI IS high) AND (BloodGlucose IS high) THEN (Risk IS high_risk)"
    #RULE3 = "IF (AGE IS low) OR (AGE IS middle) AND (BMI IS medium) AND (BloodGlucose IS medium) THEN (Risk IS medium_risk)"
    #RULE4 = "IF (AGE IS low) OR (AGE IS middle) AND (BMI IS medium) AND (BloodGlucose IS low) THEN (Risk IS low_risk)"
    FS.add_rules([
    RULE1, RULE2, RULE3, RULE4, RULE5, RULE6, RULE7, RULE8, RULE9
    ])


    FS.set_variable("AGE", age)
    FS.set_variable("BMI", bmi)
    FS.set_variable("BloodPressure", blood_pressure)
    FS.set_variable("BloodGlucose", blood_glucose)
    FS.set_variable("Cholesterol", cholesterol)
    return FS.Mamdani_inference(["Risk"])['Risk']

