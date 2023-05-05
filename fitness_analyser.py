# Run this file in the Terminal
from datahandler import importCSV, getAll
#from converters import *


class Fitness_Analyser():
    def __init__(self) -> None:
        pass

    def run_app(self) -> None:
        print("Welcome to the fitness analyser program.")
        is_importing = self.questioner("Do you want to import csv data")
        is_metric = self.questioner("Is this data in metric")
        if is_importing:
            filename = input("What is the name of the file you are importing? ")
            importCSV(filename, is_metric)
        graph_q = "Do you want to graph the data"
        is_graphing = self.questioner(graph_q)
        while is_graphing:
            # Step 1 grab data from db
            data = getAll()
            print(data)
            # Step 2 graph data
            # need to actually do some graphing here
            is_graphing = self.questioner(graph_q)
        print("Thank you for using the fitness analyser.\nGood Bye!")

    def questioner(self, question: str) -> bool:
        answer = input(f"{question} (y/n)? ")
        if answer == 'y':
            return True
        else:
            return False


if __name__ == '__main__':
    app = Fitness_Analyser()
    app.run_app()
