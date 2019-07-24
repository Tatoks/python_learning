class Bmw:
    def __init__(self):
        self.models = ['320d', '330d', 'bikes']

    def out_models(self):
        print("Existing models are: ")
        for model in self.models:
            print(model)