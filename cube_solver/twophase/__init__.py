import time

from .solve import SolutionManager


def solve(cube_string, max_length=25, max_time=10):
   
    sm = SolutionManager(cube_string)
    solution = sm.solve(max_length, time.time() + max_time)
    if isinstance(solution, str):
        return solution
    elif solution == -2:
        raise RuntimeError("max_time exceeded, no solution found")
    elif solution == -1:
        raise RuntimeError("no solution found, try increasing max_length")
    raise RuntimeError(
        f"SolutionManager.solve: unexpected return value {solution}"
    )


def solve_best(cube_string, max_length=25, max_time=10):
   
    return list(solve_best_generator(cube_string, max_length, max_time))


def solve_best_generator(cube_string, max_length=25, max_time=10):
    
    sm = SolutionManager(cube_string)
    timeout = time.time() + max_time
    while True:
        solution = sm.solve(max_length, timeout)

        if isinstance(solution, str):
            yield solution
            max_length = len(solution.split(" ")) - 1
        elif solution == -2 or solution == -1:
            # timeout or no more solutions
            break
        else:
            raise RuntimeError(
                f"SolutionManager.solve: unexpected return value {solution}"
            )
