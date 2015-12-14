#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-13 01:07:49
# @Author  : killingwolf (killingwolf@qq.com)


class User(object):

    """用户类"""

    def __init__(self, car_name):
        self.__cars = {}  # 购物车名对应一个购物车
        self.__cars.update({car_name: Cart(car_name)})

    def add_car(self, car_name):  # 新增一个购物车car_name
        self.__cars.update({car_name: Cart(car_name)})

    def remove_car(self, car_name):  # 删除一个购物车car_name
        if car_name not in self.__cars:
            print "Error! No this Cart!"
            return -1
        self.__cars.pop(car_name)

    # 向购物车car_name里新增一个货物, 默认是向第一个购物车添加货物
    def add_Item(self, car_name, name, price):
        if car_name not in self.__cars:
            print "No this car_name!"
            return -1
        self.__cars[car_name].add_Item(name, price)

    # 删除一个购物车car_name里名为name的货物Item
    def remove_Item(self, car_name, name):
        self.__cars[car_name].remove_Item(name)

    def total_price(self):
        sum = 0
        for key in self.__cars:
            sum += self.__cars[key].total_price()
        return sum

    def __str__(self):
        return str(self.__cars)


class Item(object):

    """货物清单类"""

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__item = (name, price)

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def __str__(self):
        return str(self.__item)

    def __repr__(self):
        return repr(self.__item)


class Cart(object):

    """购物车类"""

    def __init__(self, name):  # name 为购物车的编号
        self.__name = name
        self.__items = []

    def add_Item(self, name, price):
        self.__items.append(Item(name, price))

    def remove_Item(self, name):
        list1 = [it for it in self.__items if it.get_name() != name]
        list2 = [it for it in self.__items if it.get_name() == name]
        self.__items = []
        self.__items.extend(list1)
        if len(list2) == 0:
            print "Error! No this Item!"
            return -1
        list2.pop()
        self.__items.extend(list2)

    def total_price(self):
        sum = 0
        for it in self.__items:
            sum += it.get_price()
        return sum

    def __str__(self):
        return str(self.__items)

    __repr__ = __str__


if __name__ == '__main__':
    user = User('1')
    user.add_Item('1', 'a', 111)
    user.add_Item('1', 'a', 111)
    user.add_Item('1', 'b', 222)
    user.add_Item('1', 'c', 333)
    print "user={0}".format(user)
    print "total price:", user.total_price()
    print "-" * 20
    print "新增购物车2"
    user.add_car('2')
    user.add_Item('2', 'c', 333)

    print "user={0}".format(user)
    print "total price:", user.total_price()

    print "-" * 20
    print "删除购物车1中的一个名为a的货物后："
    user.remove_Item('1', 'a')
    print "user={0}".format(user)
    print "total price:", user.total_price()

    print "-" * 20
    print "删除购物车2中的一个名为c的货物后："
    user.remove_Item('2', 'c')
    print "user={0}".format(user)
    print "total price:", user.total_price()

    print "-" * 20
    print "删除购物车2中的一个不存在的货物d："
    user.remove_Item('2', 'd')
    print "user={0}".format(user)
    print "total price:", user.total_price()

    print "-" * 20
    print "删除一个不存在的购物车4："
    user.remove_car('4')
    print "user={0}".format(user)
    print "total price:", user.total_price()
