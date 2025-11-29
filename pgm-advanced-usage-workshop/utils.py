"""
Sample code to demonstrate tIme and memory Usage.

Disclaimer: 
The tools below except Timer are AI generated and not scrutinized adequately.
Their purpose is to demonstrate only possibilities.
"""

import psutil
import gc
import os

import psutil
import gc
import os
import pandas as pd

import threading
import time


class Timer:
    def __init__(self, name: str):
        self.name = name
        self.start = None

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, *args):
        print(
            f"Execution time for {self.name} is {(time.perf_counter() - self.start):0.6f} s"
        )


class MemoryMonitor:
    def __init__(self, name: str):
        self.name = name
        self.process = psutil.Process(os.getpid())
        self.start_memory = None
        self.peak_memory = None

    def __enter__(self):
        # Force garbage collection to get a clean starting point
        gc.collect()
        # Get initial memory usage
        self.start_memory = (
            self.process.memory_info().rss / 1024 / 1024
        )  # Convert to MB
        self.peak_memory = self.start_memory
        return self

    def __exit__(self, *args):
        # Force garbage collection before final measurement
        gc.collect()
        # Get final memory usage
        end_memory = self.process.memory_info().rss / 1024 / 1024  # Convert to MB
        memory_diff = end_memory - self.start_memory
        peak_diff = self.peak_memory - self.start_memory

        print(f"Memory usage for {self.name}:")
        print(f"  Start: {self.start_memory:.2f} MB")
        print(f"  End: {end_memory:.2f} MB")
        print(f"  Net change: {memory_diff:+.2f} MB")
        print(f"  Peak increase: {peak_diff:+.2f} MB")

    def update_peak(self):
        """Manually update peak memory usage during execution"""
        current_memory = self.process.memory_info().rss / 1024 / 1024
        if current_memory > self.peak_memory:
            self.peak_memory = current_memory


class PerformanceMonitor:
    """Combined timer and memory monitor for comprehensive performance analysis"""

    def __init__(self, name: str):
        self.name = name
        self.timer = Timer(name)
        self.memory_monitor = MemoryMonitor(name)

    def __enter__(self):
        self.timer.__enter__()
        self.memory_monitor.__enter__()
        return self

    def __exit__(self, *args):
        self.timer.__exit__(*args)
        self.memory_monitor.__exit__(*args)
        print(f"--- End of {self.name} performance report ---\n")


class PerfLogger:
    """Simple in-memory performance logger that stores records in a pandas DataFrame."""

    def __init__(self):
        self.records = []

    def log(
        self,
        name: str,
        start_time: float,
        end_time: float,
        start_mem: float,
        end_mem: float,
        peak_mem: float,
    ):
        self.records.append(
            {
                "name": name,
                "start_time": start_time,
                "end_time": end_time,
                "duration_s": end_time - start_time,
                "start_mem_mb": start_mem,
                "end_mem_mb": end_mem,
                "net_mem_change_mb": end_mem - start_mem,
                "peak_mem_mb": peak_mem,
                "peak_increase_mb": peak_mem - start_mem,
            }
        )

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self.records)


class LoggedPerformanceMonitor(PerformanceMonitor):
    """A PerformanceMonitor that logs results into a PerfLogger."""

    def __init__(self, name: str, logger: PerfLogger):
        super().__init__(name)
        self.logger = logger
        self._start_time = None
        self._start_mem = None

    def __enter__(self):
        # start timer and memory monitor
        self._start_time = time.perf_counter()
        self._start_mem = self.memory_monitor.process.memory_info().rss / 1024 / 1024
        self.timer.__enter__()
        self.memory_monitor.__enter__()
        return self

    def __exit__(self, *args):
        # capture end values and delegate to base
        end_time = time.perf_counter()
        self.timer.__exit__(*args)
        self.memory_monitor.__exit__(*args)
        end_mem = self.memory_monitor.process.memory_info().rss / 1024 / 1024
        peak_mem = self.memory_monitor.peak_memory
        # log the record
        self.logger.log(
            self.name, self._start_time, end_time, self._start_mem, end_mem, peak_mem
        )


class PollingLoggedPerformanceMonitor(LoggedPerformanceMonitor):
    """Poll process memory on a short interval in a background thread to catch transient peaks."""

    def __init__(self, name: str, logger: PerfLogger, poll_interval: float = 0.01):
        super().__init__(name, logger)
        self.poll_interval = poll_interval
        self._stop_event = threading.Event()
        self._thread = None

    def _poll(self):
        proc = self.memory_monitor.process
        while not self._stop_event.is_set():
            cur = proc.memory_info().rss / 1024 / 1024
            if cur > self.memory_monitor.peak_memory:
                self.memory_monitor.peak_memory = cur
            time.sleep(self.poll_interval)

    def __enter__(self):
        # start base enter first to initialize memory_monitor
        super().__enter__()
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._poll, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, *args):
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join()
        return super().__exit__(*args)
