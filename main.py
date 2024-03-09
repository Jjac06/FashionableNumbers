import csv


numbers = [1, 1/2]


for i in range(0, 25):
    numbers += [1 / (numbers[i] + numbers[i+1])]


with open("numbers.csv", "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["iteration", "a", "b", "new"])
    for i in range(0, len(numbers) - 2):
        csvwriter.writerow([i + 1, numbers[i], numbers[i+1], numbers[i+2]])