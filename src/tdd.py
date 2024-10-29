import re


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Check for custom delimiter
        if numbers.startswith("//"):
            delimiter, numbers = self._extract_delimiter(numbers)
        else:
            delimiter = ','  # Default delimiter is a comma

        # Replace new lines with the delimiter and split the string
        numbers = re.sub(r'[\n]', delimiter, numbers)
        number_list = numbers.split(delimiter)

        # Validate and sum the numbers
        total = 0
        negatives = []

        for num in number_list:
            if num.strip():  # Ignore empty strings
                n = int(num)
                if n < 0:
                    negatives.append(n)
                total += n

        if negatives:
            raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")

        return total

    def _extract_delimiter(self, numbers: str):
        parts = numbers.split('\n', 1)
        delimiter = parts[0][2:]  # Skip "//"
        return delimiter, parts[1]