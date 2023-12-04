class Allergies:

    def __init__(self, score):
        self.score = score ##Nueva lista para no modificar "score"
        if self.score >= 256 and self.score < 512: ##Anula alergias mayores a 256
            self.score -= 256
        if self.score >= 512 and self.score < 1024: ##Anula alergias mayores a 512
            self.score -= 512
            
        items = {"eggs":1,"peanuts":2,"shellfish":4,"strawberries":8,"tomatoes":16,"chocolate":32,"pollen":64,"cats":128,}
        self.allergies = []

        for i in reversed(sorted(items.values())): ##Revierte los valores para utilizarlos
            if self.score - i >= 0:           
                self.allergies.append(list(items.keys())[list(items.values()).index(i)]) ##Encuentra el "key" de ese valor
                self.score -= i
        
    def allergic_to(self, item): ##DEBE DEVOLVER TRUE O FALSE SI ES ALERGICO A "ITEM"
        if item in self.allergies:
            return True
        return False

    @property
    def lst(self): ##DEBE DEVOLVER UNA LISTA DE LAS ALERGIAS
        return self.allergies

print(Allergies(255).allergic_to("shellfish"))

print()
