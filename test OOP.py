class player:
    #Score = INTEGER
    #Category = STRING
    #PlayerID = STRING
    def __init__(self, InputPlayerID):
        self.__Score = 0
        self.__Category = 'Not Qualified'
        self.__PlayerID = InputPlayerID

    def SetScore(self, ScoreInput):
        if ScoreInput >= 0 and ScoreInput <= 150:
            self.__Score = ScoreInput
            return True
        else:
            print('score is invalid')
            return False

    def SetCategory(self, ScoreInput):
        if ScoreInput > 120:
            self.__Category = 'Advanced'
        elif ScoreInput > 80 and ScoreInput <= 120:
            self.__Category = 'Intermediate'
        elif ScoreInput >= 50 and ScoreInput <= 80:
            self.__Category = 'Beginner'
        else:
            self.__Category = 'Not Qualified'

    def SetPlayerID(self):
        idp = input('enter new player ID: ')
        count = 0
        for i in range(int(idp)):
            count = count + 1
        if count > 15 or count < 4:
            idp = input('enter new player ID: ')
        self.__PlayerID = idp
        print('your new player ID is', idp)

    def GetScore(self):
        return self.__Score
    def GetCategory(self):
        return self.__Category
    def GetPlayerID(self):
        return self.__PlayerID

def CreatePlayer():
    playerID = input('enter player ID: ')
    score = int(input('enter your score: '))
    JoahnnePlayer = player(playerID)
    JoahnnePlayer.SetScore(score)
    JoahnnePlayer.SetCategory(score)
    print(JoahnnePlayer.GetCategory())

#main
Player = CreatePlayer()
