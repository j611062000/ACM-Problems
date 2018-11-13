import re


def sorting(dic):
    temp = [(x, dic[x]) for x in dic]
    temp.sort()
    return temp

    for element in l:
        print(element, l[element])


class Ferry():

    def __init__(self):
        self.capacity = None
        self.cars = [0]  # zero is used as dummy variable


with open("10261_Ferry Loading.txt", "r") as file:
    data = file.readlines()
    ferries, ferry = [], 0
    for i in range(1, len(data)):

        if data[i] == "\n":
            ferries.append(Ferry())
            ferries[-1].capacity = int(data[i + 1][:-1]) * 100

        elif data[i] != '0\n' and data[i] != "0" and data[i - 1] != "\n":
            ferries[-1].cars.append(int(data[i][:-1]))

    # for i in range(len(ferries)):

    #     print(ferries[i].capacity)
    #     print(ferries[i].cars)


# dp[(i,j)] = True --> left lane can hold i cars, which length is j
# c: cth car
# print(ferries[0].cars)


def arrangement(Ferry):

    capacity = [0]
    path, dp = {}, {(0, 0): True}

    for c in range(len(Ferry.cars)):
        for cap in capacity:

            if dp.get((c, cap), False):

                if(cap + Ferry.cars[c + 1]) <= Ferry.capacity:
                    dp[(c + 1, cap + Ferry.cars[c + 1])] = True
                    path[(c + 1, cap + Ferry.cars[c + 1])] = True
                    capacity.append(cap + Ferry.cars[c + 1])

                if(sum(Ferry.cars[:c + 1]) - cap + Ferry.cars[c + 1]) <= Ferry.capacity:
                    dp[(c + 1, cap)] = True
                    path[(c + 1, cap)] = False
    # print(len(dp))
    print(sorting(path))

    def tracing(path, Ferry):
        cars = Ferry.cars
        start = max(path)
        count = start[0]
        print("{} cars can be loaded".format(count))
        while (count):
            print(cars[count], end=":")
            if path[start]:
                print("PORT")
                start = (start[0] - 1, start[1] - cars[start[0]])
            else:
                print("STARBORD")
                start = (start[0] - 1, start[1])
            count -= 1
    tracing(path, Ferry)

if __name__ == "__main__":
    arrangement(ferries[0])
