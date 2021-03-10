print("How many Richters are you converting")
richter = float(input())
print("Richter scale Value:", richter)


def Conversions():
    joules = 10**((1.5*richter)+4.8)
    print("Amount of Joules:", joules)
    tnt = joules / (4.184*10**9)
    print("Amount of TNT:", tnt)


Conversions()
