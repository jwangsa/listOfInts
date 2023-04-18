# listOfInts

This is a Python function designed to solve a problem that arose during tax season. The function takes a list of integers and a target number as inputs, and returns a list of integers from the original list that sum up to the target number, with each element occurring at most once. The motivation for creating this function was to determine the source of a wire transfer of $1344, given the numbers for each category and year. By using this function, the user can quickly identify which specific numbers contribute to the total sum of $1344.

<img width="860" alt="Screen Shot 2023-04-17 at 10 51 10 PM" src="https://user-images.githubusercontent.com/47044093/232658190-62831153-b3b6-43e6-ab3f-1353d98f1f34.png">

# Usage
Here's an example of how to use the combo function:
```
numbers = [24.94, 145, 296, 299, 306, 325, 333, 313, 316, 707, 875.6, 154, 373, 488]
target = 1344
print(combo(numbers, target))
```

This will output the following:
```
[325, 333, 313, 373]
```

This means that the numbers that sum up to 1344 are: <br />
2022 GST/HST Credit, 2018 Ontario Trillium Benefit, 2019 Ontario Trillium Benefit, 2021 Climate Action Incentive Payment.
