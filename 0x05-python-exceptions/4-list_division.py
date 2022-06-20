#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(list_length):
        try:
            div = 0
            div = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            break
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            newList.append(div)
    return newList
