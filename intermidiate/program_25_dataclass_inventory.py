"""Track items using dataclasses for readability."""

from dataclasses import dataclass


@dataclass
class InventoryItem:
    name: str
    quantity: int
    price: float

    def total_value(self) -> float:
        """Return the total value for this inventory item."""
        return self.quantity * self.price


if __name__ == "__main__":
    laptop = InventoryItem(name="Laptop", quantity=5, price=950.0)
    print(laptop)
    print(f"Total value: ${laptop.total_value():.2f}")
