from floyd_warshall import floyd_warshall
from graph import Graph
import time

def run_experiment(
        sizes=None,
        densities=None,
        trials=20,
        output_file="results.txt"
):
    if sizes is None:
        sizes = list(range(20, 201, 20))
    if densities is None:
        densities = [10, 30, 50, 70, 90]

    results = []
    total = len(sizes) * len(densities) * trials
    run_id = 0

    with open(output_file, "w") as f:
        f.write("n\tdensity\ttrial\ttime_sec\n")

        for density in densities:
            for n in sizes:
                for t in range(trials):
                    run_id += 1
                    print(f"[{run_id}/{total}] n={n}, density={density}%, trial={t+1}")

                    g = Graph.generate_random(n, density)

                    start = time.perf_counter()
                    floyd_warshall(g)
                    end = time.perf_counter()

                    elapsed = end - start
                    print(f"   час виконання = {elapsed:.6f} сек")

                    f.write(f"{n}\t{density}\t{t+1}\t{elapsed:.6f}\n")

                    results.append({
                        "n": n,
                        "density": density,
                        "trial": t + 1,
                        "time_sec": elapsed
                    })

    print("\nЕксперимент завершено!")
    return results

if __name__ == "__main__":
    res = run_experiment()
