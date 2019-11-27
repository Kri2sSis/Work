import csv
import itertools

count = 0
file_buffer = []

with open("car.csv") as csv_fd:
    reader = csv.reader(csv_fd, delimiter=';')
    next(reader)  # пропускаем заголовок
    for row in reader:
        file_buffer.append(row)



print(file_buffer)