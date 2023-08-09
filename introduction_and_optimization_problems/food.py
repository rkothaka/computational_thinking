class Food:
    def __init__(self, name, value, calories):
        self._name = name
        self._value = value  # happiness
        self._calories = calories

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def cost(self):
        return self._calories

    @property
    def density(self):
        return self.value / self.cost

    def __str__(self):
        return f"Food: {self.name} (Value: {self.value}, Calories: {self.cost})"

    def __repr__(self):
        return f"Food(name='{self.name}', value={self.value}, calories={self.cost})"
