# Imports
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

class display():
    def __init__(self):
        # Read CSV
        df = pd.read_csv('data/ data.csv')
        df1 = df["Polarity"]
        df2 = df["Subjectivity"]

        pPolarity = []
        nPolarity = []
        nuPolarity = []

        yes = []
        no = []

        # For Polarity
        for i in df1:
            if i < 0:
                nPolarity.append(i)
            elif i > 0:
                pPolarity.append(i)
            else:
                nuPolarity.append(i)

        # For Subjectivity
        for i in df2:
            if i > 0:
                yes.append(i)
            else:
                no.append(i)

        # Counting Polarity
        values1 = [len(pPolarity),len(nPolarity),len(nuPolarity)]
        values2 = [len(yes),len(no)]

        # To Plot graph
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.axis("equal")
        ax2.axis("equal")

        ax1.pie(values1,labels =["Positive","Negative","Neutral"], radius=1.5,autopct= '%.1f%%', shadow= True,colors = ["#42adf4","#f4414d","#9df441"] ,explode =[0,0.2,0])
        ax1.set_title("Polarity")
    
        ax2.pie(values2,labels = ["YES","NO"], radius=1.5,autopct= '%.1f%%', shadow= True,colors = ["#42adf4","#f4414d"], explode =[0.2,0])
        ax2.set_title("Subjectivity")
        
        plt.tight_layout(pad=5)
        plt.show()
