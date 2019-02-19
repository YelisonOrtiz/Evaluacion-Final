def Cartas(sml):
    return ({
        '1': ['A', sml], '2': [2, sml], '3': [3, sml],
        '4': [4, sml], '5': [5, sml], '6': [6, sml],
        '7': [7, sml], '8': [8, sml], '9': [9, sml],
        '10': [10, sml], '11': [11, sml], '12': [12, sml],
        '13': [13, sml]
    })

cartas = {
    'picas': Cartas('♠'),
    'corazones': Cartas('♥'),
    'diamantes': Cartas('♦'),
    'treboles': Cartas('♣')
}

# class Players:

#     def _init__(self, playerOne, playerTwo, playerThree, playerFour):
#         self.playerOne = playerOne
#         self.playerTwo = playerTwo
#         self.playerThree = playerThree
#         self.playerFour = playerFour


print (cartas['picas'])

    

