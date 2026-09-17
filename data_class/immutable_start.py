from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval 

obj = ImmutableClass("Another value", 29)
print(obj.value1, obj.value2)

#try to change the value of an attribute
#obj.value1 = "New Value"  # This will raise a FrozenInstanceError

obj.some_func(15)

print(obj.value1, obj.value2)
