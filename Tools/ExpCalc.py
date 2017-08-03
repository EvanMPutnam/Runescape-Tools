"""
Author: Evan Putnam
Description: Tools for level calculations in Runescape
Language: Python3
"""
import math


class Experience:
    """
    Class that allows you to calculate varying runescape levelings
    """
    def __init__(self):
        pass

    def calcLevel(self, attack, strength, range, magic, defence, constitution,
                  prayer, summoning):
        """
        Calculates the combat level from the given stats.
        :param attack: 
        :param strength: 
        :param range: 
        :param magic: 
        :param defence: 
        :param constitution: 
        :param prayer: 
        :param summoning: 
        :return: 
        """
        choice = 0
        if attack+strength > 2*magic and attack+strength > 2*range:
            choice = attack + strength
        elif 2*magic > attack+strength and 2*magic > 2*range:
            choice = 2*magic
        else:
            choice = 2*range

        return ((13/10)*choice+defence+constitution+math.floor((1/2)*prayer)
                +math.floor((1/2)*summoning))/4

    def calcExpNeededToLevel(self, level):
        """
        Calculates the experience needed to get to level x
        :param level 1-99 for which to achieve: 
        :return: 
        """
        total = 0
        for i in range(1,level):
            total += math.floor(i+300*math.pow(2, i/7))
        return math.floor(total/4)





if __name__ == '__main__':
    exp = Experience()
    print(exp.calcLevel(1,1,1, 1, 1, 99,99,99))
    print(exp.calcExpNeededToLevel(40))


