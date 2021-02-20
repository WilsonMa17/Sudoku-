class Board:
    """create a prepopulated Sudoku game board"""

    def __init__(self):
        self._board = [

            [1, 'X', 'X', 9, 'X', 4, 'X', 8, 2],
            ['X', 5, 2, 6, 8, 'X', 3, 'X', 'X'],
            [8, 6, 4, 2, 'X', 'X', 9, 1, 'X'],
            ['X', 1, 'X', 'X', 4, 9, 8, 'X', 6],
            [4, 9, 8, 3, 'X', 'X', 7, 'X', 1],
            [6, 'X', 7, 'X', 1, 'X', 'X', 9, 3],
            ['X', 8, 6, 'X', 3, 5, 2, 'X', 9],
            [5, 'X', 9, 'X', 'X', 2, 1, 3, 'X'],
            ['X', 3, 'X', 4, 9, 7, 'X', 'X', 8],
        ]

    def mark(self,row ,column ,n):
        """Inserts number into specified row and column of the board"""

        if row > 9 or row < 1:
            print("Out of bounds")
            return
        if column > 9 or column < 1:
            print("Out of bounds")
            return
        if n > 9 or n < 1:
            print("Number should be between 1 and 9")
            return
        # prevents row 1 starting numbers from being replaced
        if (row == 1 and column == 1) or (row == 1 and column == 4) or (row == 1 and column == 6) or (row == 1 and column == 8)\
            or (row == 1 and column == 9):
            print("CANNOT REPLACE STARTING NUMBERS ")
            return
        # prevents row 2 starting numbers from being replaced
        if (row == 2 and column == 2) or (row == 2 and column == 3) or (row == 2 and column == 4) or (row == 2 and column == 5)\
            or (row == 2 and column == 7):
            print("CANNOT REPLACE STARTING NUMBERS ")
            return
        # prevents row 3 starting numbers from being replaced
        if (row == 3 and column == 1) or (row == 3 and column == 2) or (row == 3 and column == 3) or (row == 3 and column == 4)\
            or (row == 3 and column == 7) or (row == 3 and column == 8):
            print("CANNOT REPLACE STARTING NUMBERS")
            return
        # prevents row 4 starting numbers from being replaced
        if (row == 4 and column == 2) or (row == 4 and column == 5) or (row == 4 and column == 6) or (row == 4 and column == 7) \
            or (row == 4 and column == 9):
            print("CANNOT REPLACE STARTING NUMBERS ")
            return
        # prevents row 5 starting numbers from being replaced
        if (row == 5 and column == 1) or (row == 5 and column == 2) or (row == 5 and column == 3) or (row == 5 and column == 4) \
            or (row == 5 and column == 7) or (row == 5 and column == 9):
            print("CANNOT REPLACE STARTING NUMBERS ")
            return
        # prevents row 6 starting numbers from being replaced
        if (row == 6 and column == 1) or (row == 6 and column == 3) or (row == 6 and column == 5) or (row == 6 and column == 8) \
            or (row == 6 and column == 9):
            print("CANNOT REPLACE STARTING NUMBERS ")
            return
        # prevents row 7 starting numbers from being replaced
        if (row == 7 and column == 2) or (row == 7 and column == 3) or (row == 7 and column == 5) or (row == 7 and column == 6) \
            or (row == 7 and column == 7) or (row == 7 and column == 9):
            print("CANNOT REPLACE STARTING NUMBERS ")
            return
        # prevents row 8 starting numbers from being replaced
        if (row == 8 and column == 1) or (row == 8 and column == 3) or (row == 8 and column == 6) or (row == 8 and column == 7) \
            or (row == 8 and column == 8):
            print("CANNOT REPLACE STARTING NUMBERS ")
            return
        # prevents row 9 starting numbers from being replaced
        if (row == 9 and column == 2) or (row == 9 and column == 4) or (row == 9 and column == 5) or (row == 9 and column == 6) \
            or (row == 9 and column == 9):
            print("CANNOT REPLACE STARTING NUMBERS ")
            return
        else:
            # inserts specified value into board at specified location and prints out the current board state
            self._board[row - 1][column - 1] = n
            print("-------------------------------")
            for i in self._board:
                print(i)
            print("-------------------------------")
            print("MOVE SUCCESSFUL")

    def reset(self):
        """reset the puzzle back to the original state"""
        self._board = [

            [1, 'X', 'X', 9, 'X', 4, 'X', 8, 2],
            ['X', 5, 2, 6, 8, 'X', 3, 'X', 'X'],
            [8, 6, 4, 2, 'X', 'X', 9, 1, 'X'],
            ['X', 1, 'X', 'X', 4, 9, 8, 'X', 6],
            [4, 9, 8, 3, 'X', 'X', 7, 'X', 1],
            [6, 'X', 7, 'X', 1, 'X', 'X', 9, 3],
            ['X', 8, 6, 'X', 3, 5, 2, 'X', 9],
            [5, 'X', 9, 'X', 'X', 2, 1, 3, 'X'],
            ['X', 3, 'X', 4, 9, 7, 'X', 'X', 8],
        ]

        print("Sudoku puzzle has been reset ")
        print("-------------------------------")
        for i in self._board:
            print(i)
        print("-------------------------------")
        return

    def exit(self):
        """quits the game"""
        print("EXITING GAME")
        exit()

    def insertionSort(self,arr):
        """insertion sort"""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def binarySearch(self,arr, x):
        """binary search"""
        low = 0
        high = len(arr) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            # checks if x is present at mid
            if arr[mid] < x:
                low = mid + 1
            # If x is greater, ignore left half
            elif arr[mid] > x:
                high = mid - 1
            # If x is smaller, ignore right half
            else:
                return mid
        else:
            print("A ROW OR COLUMN DOES NOT HAVE DISTINCT 1-9 VALUES")
            return

    def verify(self):
        """check conditions to see if board solution is viable """
        column = []
        columns = []
        k = 0
        try:
            # create a new list of columns
            for i in range(9):
                for i in range(len(self._board)):
                    column.append(self._board[i][k])
                k += 1
                columns.append(column)
                column = []
            # checks if the row adds up to 45
            for i in self._board:
                if sum(i) != 45:
                    print("Solution does not work: a row is not correct")
                    return
            # checks if the columns add up to 45
            for i in columns:
                if sum(i) != 45:
                    print("Solution does not work: a column is not correct")
                    return
            t = 0
            # sorts the rows in ascending order
            for i in range(len(self._board)):
                self.insertionSort((self._board[i]))
                t += 1
            k = 0
            t = 1
            # searches for numbers 1-9 in each row, returns false if distinct values not found
            for i in range(9):
                for i in range(len(self._board)):
                    self.binarySearch(self._board[i], t)
                t += 1
                k += 1
            else:
                print("Your solution is viable")
                exit()
        except TypeError:
            # if TypeError is raised, board still contains unfilled numbers
            print("Solution does not work: Not all numbers are filled")

    def solution(self):
        """fills board with correct solution"""
        self._board = [
            [1, 7, 3, 9, 5, 4, 6, 8, 2],
            [9, 5, 2, 6, 8, 1, 3, 7, 4],
            [8, 6, 4, 2, 7, 3, 9, 1, 5],
            [3, 1, 5, 7, 4, 9, 8, 2, 6],
            [4, 9, 8, 3, 2, 6, 7, 5, 1],
            [6, 2, 7, 5, 1, 8, 4, 9, 3],
            [7, 8, 6, 1, 3, 5, 2, 4, 9],
            [5, 4, 9, 8, 6, 2, 1, 3, 7],
            [2, 3, 1, 4, 9, 7, 5, 6, 8],
        ]
        print("-------------------------------")
        for i in fb._board:
            print(i)
        print("-------------------------------")


fb = Board()
print("-------------------------------")
for i in fb._board:
    print(i)
print("-------------------------------")

# continuously runs the game until exit
while True:
    try:
        print(" ")
        # retrieves user input
        x, y, z = [(x) for x in input("MAKE YOUR MOVE [ROW] [COLUMN] [NUMBER] OR TYPE [OTHER] FOR OPTIONS \n").split()]
        x = int(x)
        y = int(y)
        z = int(z)
        fb.mark(x, y, z)
    except ValueError:
        print("TYPE [EXIT] TO QUIT GAME [RESET] TO RESET PUZZLE OR [VERIFY] TO CHECK SOLUTION \n")
        n = input()
        if n == "EXIT":
            fb.exit()
        if n == "RESET":
            fb.reset()
        if n == "VERIFY":
            fb.verify()
        if n == "SOLUTION":
            fb.solution()


