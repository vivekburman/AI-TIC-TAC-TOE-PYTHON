import sys
import math
from app import *
from flask import Flask, request
from flask_restful import Resource
class FetchMoveController(Resource):
    AI_PLAYER='X'
    HU_PLAYER='O'
    def get(self):
        if endpoint == "testing":
            return "Successfull in testing."
    def post(self):
        if request.endpoint == "get_next_move":
            board=request.get_json(force=True)
            return self.main(board)
        if request.endpoint == "get_winner":
            board=request.get_json(force=True)
            return self.checkWinner(board)

    def isBoardFull(self,board):
        #if board is full declare winner
        if board.count(' ') >= 1:
            return False
        else:
            return True

    def isWinner(self,letter,board):
         return ((board[0]==letter and board[4]==letter and board[8]==letter) or
         (board[2]==letter and board[4]==letter and board[6]==letter) or
         (board[0]==letter and board[3]==letter and board[6]==letter) or
         (board[1]==letter and board[4]==letter and board[7]==letter) or
         (board[2]==letter and board[5]==letter and board[8]==letter) or
         (board[0]==letter and board[1]==letter and board[2]==letter) or
         (board[3]==letter and board[4]==letter and board[5]==letter) or
         (board[6]==letter and board[7]==letter and board[8]==letter))

    def minmax(self,board,player,depth):
        if self.isWinner(self.AI_PLAYER,board):
            return 10-depth
        if self.isWinner(self.HU_PLAYER,board):
            return -10-depth
        if self.isBoardFull(board):
            return 0-depth
        #set bestValue to 0
        bestValue=0
        availSpots= [i for i,letter in enumerate(board) if letter == ' ']
        #if currently its AI move
        if player == self.AI_PLAYER:
            #set bestValue to Integer.MIN_VALUE
            bestValue= -sys.maxsize-1
            #iterate through each possible place
            for i in availSpots:
                #mark it
                board[i]=player
                #check if it resulted in win
                bestValue=max(bestValue, self.minmax(board, player=self.HU_PLAYER,depth=depth+1))
                board[i]=' '

            #if currently its HU move
        else:
            #set bestValue to Integer.MAX_VALUE
            bestValue=sys.maxsize
            #iterate through each possible place
            for i in availSpots:
                #mark it
                board[i]=player
                #check if it resulted in win
                bestValue=min(bestValue, self.minmax(board, player=self.AI_PLAYER,depth=depth+1))
                board[i]=' '
        return bestValue

    def computeNextMove(self,board):
        availSpots= [i for i,letter in enumerate(board) if letter == ' ']
        pos=-1
        bestValue= -sys.maxsize-1
        moveValue=bestValue
        for i in availSpots:
            board[i]=self.AI_PLAYER
            moveValue= self.minmax(board,player=self.HU_PLAYER,depth=1)
            if moveValue > bestValue:
                bestValue=moveValue
                pos=i
            board[i]=' '
        return pos
    def winner(self,board):
        if self.isWinner(self.AI_PLAYER,board):
            return 1
            # return {'result':board,'winner':AI_PLAYER}
        if self.isWinner(self.HU_PLAYER,board):
            return 2
            # return {'result':board,'winner':HU_PLAYER}
        if self.isBoardFull(board):
            return 3
            # return {'result':board,'winner':'DRAW'}
        return -1
        # return {'result':board,'winner':'None'}
    def checkWinner(self,board):
        status=self.winner(board)
        if status == 1:
            return {'result':board,'winner':self.AI_PLAYER,'flag':2}
        elif status == 2:
            return {'result':board,'winner':self.HU_PLAYER,'flag':2}
        elif status == 3:
            return {'result':board,'winner':'DRAW','flag':2}
        return {'result':board,'winner':'None','flag':0}
    def main(self,board):
        status=self.winner(board)
        if status == 1:
            return {'result':board,'winner':self.AI_PLAYER,'flag':2}
        elif status == 2:
            return {'result':board,'winner':self.HU_PLAYER,'flag':2}
        elif status == 3:
            return {'result':board,'winner':'DRAW','flag':2}
        pos=self.computeNextMove(board)
        board[pos]=self.AI_PLAYER
        return {'result':board,'winner':'None','flag':1}
