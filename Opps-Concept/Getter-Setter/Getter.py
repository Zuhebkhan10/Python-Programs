class Student:
    def __init__(self, name, marks):
        self._name = name      # protected variable
        self._marks = marks

    # Getter
    def get_marks(self):
        return self._marks

    # Setter
    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative")
