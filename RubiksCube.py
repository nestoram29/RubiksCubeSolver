class RubiksCube:
    def __init__(self, startState = None):
        self.cube = [
            *range(0, 9), # Up
            *range(9, 18), # Down
            *range(18, 27), # Left
            *range(27, 36), # Right
            *range(36, 45), # Front
            *range(45, 54), # Back
        ] # Centers = [4, 13, 22, 31, 40, 49]

    def scramble(self):
        pass
    
    def checkInValidState(self):
        pass

    def makeMove(move):
        '''
        Notation

        Face Turns:
        U  D  R  L  F  B  (clockwise)
        U' D' R' L' F' B' (counterclockwise)
        U2 D2 R2 L2 F2 B2

        Wide Moves
        u  d  r  l  f  b
        u' d' r' l' f' b'

        Slice Moves
        M  E  S
        M' E' S'
        M2 E2 S2
        (M follows L)
        (E follows D)
        (S follows F)
        '''
        pass