class Calculator:
    def __init__(self,monitor,mouse,tastatura):
        self.monitor = monitor
        self.mouse = mouse
        self.tastatura = tastatura
    def infoCalculator(self):
        print("Informatii despre calcul "+self.monitor+
            " "+self.mouse+" "+self.tastatura)

c1=Calculator("LCD","Microsoft","DELL")
c1.infoCalculator()
