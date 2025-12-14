from floyd_warshall import floyd_warshall
from graph import Graph
import time

def run_experiment(
        sizes=None,
        densities=None,
        trials=20,
        output_file="results.txt",
        avg_output_file="results_avg.txt"
):
    if sizes is None:
        sizes = list(range(20, 201, 20))
    if densities is None:
        densities = [10, 30, 50, 70, 90]

    total = len(sizes) * len(densities) * trials
    run_id = 0

    with open(output_file, "w") as f_all, open(avg_output_file, "w") as f_avg:
        f_all.write("n\tdensity\ttrial\ttime_sec\n")
        f_avg.write("n\tdensity\tavg_time_sec\n")

        for density in densities:
            for n in sizes:
                times = []

                for t in range(trials):
                    run_id += 1
                    print(f"[{run_id}/{total}] n={n}, density={density}%, trial={t+1}")

                    g = Graph.generate_random(n, density)

                    start = time.perf_counter()
                    floyd_warshall(g)
                    end = time.perf_counter()

                    elapsed = end - start
                    times.append(elapsed)

                    f_all.write(f"{n}\t{density}\t{t+1}\t{elapsed:.6f}\n")

                avg_time = sum(times) / len(times)
                f_avg.write(f"{n}\t{density}\t{avg_time:.6f}\n")

                print(f"   СЕРЕДНІЙ ЧАС = {avg_time:.6f} сек\n")

    print("\nЕксперимент завершено!")

if __name__ == "__main__":
    run_experiment()
