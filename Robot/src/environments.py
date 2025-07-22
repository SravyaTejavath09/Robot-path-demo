from src.cell import Cell

start_cell = Cell(1, 1)

obstacles_1 = [
    Cell(row=2, column=3), 
    Cell(row=3, column=5), 
    Cell(row=2, column=1), 
    Cell(row=5, column=1), 
    Cell(row=6, column=6)
]

obstacles_2 = [
    Cell(row=2, column=3), 
    Cell(row=3, column=5), 
    Cell(row=2, column=1), 
    Cell(row=5, column=5), 
    Cell(row=5, column=1), 
    Cell(row=6, column=6)
]

obstacles_3 = [
    Cell(row=2, column=3), 
    Cell(row=3, column=5), 
    Cell(row=2, column=1), 
    Cell(row=5, column=5), 
    Cell(row=5, column=1), 
    Cell(row=3, column=3), 
    Cell(row=4, column=3), 
    Cell(row=5, column=3), 
    Cell(row=6, column=3), 
    Cell(row=7, column=3), 
    Cell(row=8, column=3), 
    Cell(row=6, column=6)
]

obstacles_4 = [
    Cell(row=2, column=3), 
    Cell(row=3, column=5), 
    Cell(row=2, column=1), 
    Cell(row=5, column=5), 
    Cell(row=5, column=1), 
    Cell(row=3, column=3), 
    Cell(row=4, column=3), 
    Cell(row=5, column=3), 
    Cell(row=6, column=3), 
    Cell(row=7, column=3), 
    Cell(row=8, column=3), 
    Cell(row=5, column=4), 
    Cell(row=6, column=6)
]

envs = {
    'env1': (8, obstacles_1, start_cell, Cell(7, 4)),
    'env2': (10, obstacles_2, start_cell, Cell(8, 4)),
    'env3': (10, obstacles_3, start_cell, Cell(8, 4)),
    'env4': (10, obstacles_4, start_cell, Cell(8, 4)),
}

