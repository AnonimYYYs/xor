from HiddenNeuronClass import HiddenNeuron
from InputNeuronClass import InputNeuron
from OutputNeuronClass import OutputNeuron
import random
import datetime

inputSet = [[0, 0], [1, 1], [1, 0], [0, 1]]
goodAnswSet = [0, 0, 1, 1]

# ideal
w = [[0.9871318808075782, 8.033279492210019], [0.9872050731896136, 8.033273749226312]]
w1 = [-90.28414438783109, 72.69013367402682]




INs = [InputNeuron(), InputNeuron()]
HNs = [HiddenNeuron(), HiddenNeuron()]
OuN = OutputNeuron()

errorValue = 0

E = 10

for z in range(300):
    # ----------------------------- начало обработки итерации --------------------------
    for k in range(4):
        # ---------------------------- начало обработки одного сета -------------------------------
        # для заполнения инпут нейрон
        # print("\n - START OF CALCULATE - \n")
        a, b = map(int, inputSet[k])
        if not (a == 0 and b == 0):
            a, b = round(a / (max(a, b)), 10), round(b / (max(a, b)), 10)
        INs[0].inp(a)
        INs[1].inp(b)
        print("input neurons:")
        for i in INs:
            i.outp()
            print(i.retInput(), " -> ", i.retOutput())
        # заполнили хидден нейрон
        for i in range(2):
            INs[0].outp()
            INs[1].outp()
            x1 = round(w[0][i] * INs[0].retOutput(), 10)
            x2 = round(w[1][i] * INs[1].retOutput(), 10)
            HNs[i].inp(x1 + x2)
        # print("hidden neurons:")
        for i in HNs:
            i.outp()
            print(i.retInput(), " -> ", i.retOutput())
        # заполнили оутпут нейрон
        x = float(0)
        for i in range(2):
            HNs[i].outp()
            x += round(w1[i] * HNs[i].retOutput(), 10)
        print("output neuron:")
        OuN.inp(x)
        OuN.outp()
        print(OuN.retInput(), " -> ", OuN.retOutput())
        errorValue += (OuN.retOutput() - goodAnswSet[k]) ** 2
        # print(f"\nerrorValue: {(errorValue ** (1 / 2)) / (k + 1)}")

        # print("\n - END OF CALCULATE - \n")
        # ---------------------------- конец обработки сета, начало изменения w ----------------------------
        # print(" - START OF LEARN - \n")
        OuN.delt(goodAnswSet[k])
        # print(f"delta of output neuron: {OuN.retDelt()}")

        for i in range(2):
            HNs[i].delt(w1[i], OuN.retDelt())
            # print(f"delta of hidden neuron {i + 1}: {HNs[i].retDelt()}")
            gradient = OuN.retDelt() * HNs[i].retOutput()
            # print(f"gradient is {gradient}")
            w1[i] += E * gradient

        for i in range(2):
            for j in range(2):
                gradient = HNs[j].retDelt() * INs[i].retOutput()
                # print(f"gradient is {gradient}")
                w[i][j] += E * gradient

        print("w = [[", w[0][0], ", ", w[0][1], "], [", w[1][0], ", ", w[1][1], "]]")
        print("w1 = [", w1[0], ", ", w1[1], "]")
        # print("\n - END OF SET - \n")
    errorValue = (errorValue / 4 ** (1 / 2))
    # print("errorValue:", errorValue)
    print("\n  --  END OF ITERATION  --  \n\n")
    # ------------------------------------- конец обработки итерации ---------------------------
