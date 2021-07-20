import math
import time
import random
import graph

track = 0
n_fold = 10


def calc_distance(point1, point2):
    sum_result = 0
    dim1 = point1.split(",")
    dim2 = point2.split(",")
    for i in range(1, len(dim1)):
        temp = (float(dim1[i]) - float(dim2[i]))
        temp *= temp
        sum_result += temp

    return max(math.sqrt(sum_result), 0.001)


def prepare_array(array, n):
    global track

    for i in range(len(array)):
        if len(array[i]) == 0:
            array.pop(i)

    new_array = []
    times = math.ceil(len(array) / n)

    for i in range(times):
        # index = random.randint(0, len(array) - 1)
        index = track + i
        new_array.append(array[index])
        array.pop(index)
    track += 1

    return new_array


def one_of_n_fold_cross_val(train_array, n_fold, nn):
    validation_array = prepare_array(train_array, n_fold)
    correct, incorrect = 0, 0

    for new_point in validation_array:
        actual_class = (new_point.split(","))[0]

        predicted_class = predict_class(train_array, new_point, nn)

        if actual_class == predicted_class:
            correct += 1
        else:
            incorrect += 1

    return correct / (correct + incorrect)


def predict_class(array, new_point, nn):
    shortest_n = []
    for data_point in array:
        distance = calc_distance(new_point, data_point)
        """if distance >= 1:
            print("dp: " + data_point)"""
        element = {
            "d": distance,
            "point": data_point
        }
        insert_in_array(shortest_n, element, nn)
    predicted_class, confidence = take_poll(new_point, shortest_n)
    return predicted_class, confidence


def calc_weight(element, item_in_array, count_element):
    count_element["count"] += 1
    # count_element["count"] += (1/calc_distance(element, item_in_array))


def take_poll(element, array):
    count = []
    for item in array:
        temp = item["point"].split(",")
        flag = False
        for i in range(len(count)):
            if count[i]["class"] == temp[0]:
                # count[i]["count"] += 1
                calc_weight(element, item["point"], count[i])
                flag = True
        if not flag:
            new_item = {
                "class": temp[0],
                "count": 1
            }
            count.append(new_item)
            flag = True

    cl = ""
    cnt = 0
    sum = 0
    for item in count:
        sum += item["count"]
        if cnt < item["count"]:
            cl = item["class"]
            cnt = item["count"]

    return cl, cnt / sum


def insert_in_array(array, element, nn):
    if len(array) < nn:
        array.append(element)
        return True

    for i in range(len(array)):
        item = array[i]
        if item["d"] > element["d"]:
            array.insert(i, element)
            array.pop(len(array) - 1)
            return True
    return False


def get_all_data():
    file_in_array = []
    # file = open("data/iris.csv", "r")
    # file = open("data/mydata.csv", "r")
    file = open("data/covid.csv", "r")
    entire_file_string = file.read()
    file_in_array = entire_file_string.split("\n")
    if len(file_in_array[len(file_in_array) - 1]) == 0:
        file_in_array.pop()
    print(len(file_in_array))

    for i in range(len(file_in_array)):
        if len(file_in_array[i]) == 0:
            file_in_array.pop(i)

    return file_in_array


def n_fold_cross_validation(file_in_array):
    # random.shuffle(file_in_array)
    file_in_array = file_in_array[:1000]
    average_accuracy = 0
    for yo in range(n_fold):
        accuracy = one_of_n_fold_cross_val(file_in_array, n_fold, 5)
        average_accuracy += accuracy
        print(accuracy * 100)
    average_accuracy /= n_fold
    print("Accuracy: ", average_accuracy)


def input_point():
    pt = input("Enter new point (spO2, pulse, temperature): ")
    pt = "Negative," + pt
    return pt


def empty_at(pt):
    temp = pt.split(",")
    for i in range(len(temp)):
        if len(temp[i]) == 0:
            return i
    return -1


def fill_empty(pt, fill_value):
    temp = pt.split(",")
    ind = empty_at(pt)
    temp[ind] = str(fill_value)
    ans = ""
    for x in temp:
        ans += x + ","
    ans = ans[:-1]
    return ans


def partial_point(all_data, nn):
    x_values = []
    y_values = []
    y_values_2 = []

    pt = input_point()
    x = empty_at(pt)
    prog = 10
    mul = 1
    min_max_array = find_min_max(all_data)

    if x == 2:
        prog = 1
        mul = 10

    for i in range(min_max_array[x]["min"], min_max_array[x]["max"]):
        for j in range(prog):
            new_val = i+j/prog
            new_pt = fill_empty(pt, new_val)

            x_values.append(new_val)
            result, confidence = predict_class(all_data, new_pt, nn)
            y_values.append(result)
            y_values_2.append(confidence)
            print(new_pt)

    graph.plot_graph(x_values, y_values, mul, y_values_2)


def find_min_max(all_data):
    min_max_array = []
    for i in range(len(all_data[0].split(","))):
        element = {
            "min": 9999999,
            "max": -9999999
        }
        min_max_array.append(element)

    for data in all_data:
        temp = data.split(",")
        for i in range(1, len(temp)):
            if float(temp[i]) < min_max_array[i]["min"]:
                min_max_array[i]["min"] = math.floor(float(temp[i]))
            if float(temp[i]) > min_max_array[i]["max"]:
                min_max_array[i]["max"] = math.ceil(float(temp[i]))

    return min_max_array


if __name__ == "__main__":
    start = time.process_time()

    all_data = get_all_data()
    # n_fold_cross_validation(all_data)
    # for i in range(10):
    #     print(predict_class(all_data, input_point(), 5))
    partial_point(all_data, 10)

    print("Time: ", time.process_time() - start)
