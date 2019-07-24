class AudiCar:
    def __init__(self):
        self.models = ['q7', 'a8', 'a3', '343']

    def out_models(self):
        print("Existing models are: ")
        for model in self.models:
            print(model)
        return ""

class AudiSubDealers:
    def __init__(self):
        self.dealers = ['1', '2', '3', '4']

    def out_dealers(self):
        print("Existing dealers are: ")
        for dealer in self.dealers:
            print("Dealer" + dealer)