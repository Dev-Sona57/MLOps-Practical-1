from typing import List

class DataProcessor:
    def __init__(self, data: List[float]):
        """
        Initialize the processor with a dataset.
        
        Args:
            data (List[float]): A list of numerical values.
        """
        self.data = data

    def mean(self) -> float:
        """
        Returns the arithmetic mean of the dataset.

        Returns:
            float: Mean of the dataset.

        Raises:
            ValueError: If dataset is empty.
        """
        if not self.data:
            raise ValueError("Data is empty.")
        return sum(self.data) / len(self.data)

    def variance(self) -> float:
        """
        Returns the variance of the dataset.

        Returns:
            float: Variance of the dataset.
        """
        m = self.mean()
        return sum((x - m) ** 2 for x in self.data) / len(self.data)


# Quick sanity check
if __name__ == "__main__":
    p = DataProcessor([1, 2, 3])
    print("loaded:", p.data)
    print("mean:", p.mean())
    print("variance:", p.variance())

