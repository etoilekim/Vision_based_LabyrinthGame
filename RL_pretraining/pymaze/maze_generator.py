
from __future__ import absolute_import
from src.maze_manager import MazeManager
from src.maze import Maze


if __name__ == "__main__":

    # The easiest way to use the library is through the Manager class. It acts as the glue between
    # The visualization, solver, and maze classes. Mazes inside the manager have unique ids that we use
    # to specify particular mazes.
    manager = MazeManager()

    # We can add mazes to the manager two different ways.
    # The first way, we specify the maze dimensions. The maze that is created gets returned back to you.
    maze = manager.add_maze(7, 7)

    # The second way is by creating a maze, and then adding it to the manager. Doing this will require you to add
    # from src.maze import Maze
    # to your imports. Because the ids need to be unique, the manager will ensure this happens. It may change the
    # id of the maze that was passed in, so we assign it to the return value to make sure we're using the updated maze.
    maze2 = Maze(7, 7)
    maze2 = manager.add_existing_maze(maze2)

    # Once we have a maze in the manager, we can tell the manager to solve it with a particular algorithm.
    #manager.solve_maze(maze.id, "BreadthFirst")
    #manager.solve_maze(maze.id, "BiDirectional")
    manager.solve_maze(maze.id, "DepthFirstBacktracker")

    # If we want to save the maze & maze solution images along with their animations, we need to let the manager know.
    manager.set_filename("myFileName")

    # To see the unsolved maze, call
    manager.show_maze(maze.id)

    # You can also set the size of the cell by passing show_maze's second argument. The default is 1.
    # manager.show_maze(maze.id, 2)

    # To show an animation of how the maze was generated, use the following line
    #manager.show_generation_animation(maze.id)

    # You can also see an animation of how the solver went about finding the end
    #manager.show_solution_animation(maze.id)

    # Finally, you can show an image of the maze with the solution path overlaid. All of these display
    # functions will save the figure if MazeManager::set_filename has been set.
    manager.show_solution(maze.id)








# from mazelib import Maze
# from mazelib.generate.Prims import Prims
# from mazelib.solve.BacktrackingSolver import BacktrackingSolver


# class MazeGenerator:
#     def __init__(self):
#         ''' '''

#     def maze(self):
    
#         m = Maze()
#         m.generator = Prims(4, 4)
#         m.generate()


#         m.solver = BacktrackingSolver()
#         m.generate_entrances(start_outer=False, end_outer=False)
#         m.solve()

#         print(m)

#         print(m.grid)

#     #def save(self, dir):





# if __name__=="__main__":
#     maze = MazeGenerator()
#     maze.maze()
    