from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimizes the 3D printing queue according to priorities and printer constraints,
    using a greedy algorithm.

    Args:
        print_jobs: A list of print jobs as dictionaries.
        constraints: Printer constraints as a dictionary.

    Returns:
        A dict with the optimal print order and total time.
    """
    # Step 1: Convert input dictionaries to dataclass objects for convenience
    jobs = [PrintJob(**job) for job in print_jobs]
    printer_cons = PrinterConstraints(**constraints)

    # Step 2: Sort jobs by priority (greedy choice)
    # A lower priority number means a higher priority
    jobs.sort(key=lambda job: job.priority)

    print_order = []
    total_time = 0
    
    # Copy the list to safely remove items from it
    remaining_jobs = list(jobs)

    # Step 3: Form batches as long as there are unprinted jobs
    while remaining_jobs:
        current_batch = []
        current_volume = 0
        
        # A list for jobs that will be removed from remaining_jobs
        jobs_to_remove = []

        # Step 4: Greedily fill the batch
        for job in remaining_jobs:
            # Check if the job can be added to the current batch
            if (current_volume + job.volume <= printer_cons.max_volume and
                    len(current_batch) < printer_cons.max_items):
                
                # Add the job to the batch
                current_batch.append(job)
                current_volume += job.volume
                jobs_to_remove.append(job)

        # If the batch is empty but jobs remain, it means the next job
        # is too large for the printer. Print it alone.
        if not current_batch and remaining_jobs:
            job = remaining_jobs[0]
            # Check if a single job does not exceed constraints
            if job.volume > printer_cons.max_volume or printer_cons.max_items < 1:
                 print(f"Warning: Job {job.id} cannot be printed as it exceeds printer constraints.")
                 jobs_to_remove.append(job) # Remove to avoid an infinite loop
            else:
                current_batch.append(job)
                jobs_to_remove.append(job)

        # Step 5: Process the formed batch
        if current_batch:
            # The batch print time is the time of the longest job in it
            batch_time = max(job.print_time for job in current_batch)
            total_time += batch_time

            # Add job IDs to the final order
            for job in current_batch:
                print_order.append(job.id)

            # Remove the processed jobs from the waiting list
            remaining_jobs = [job for job in remaining_jobs if job not in jobs_to_remove]
        # If remaining_jobs is not empty after this, but current_batch is, 
        # it means we cannot process the rest of the jobs.
        elif remaining_jobs:
            print("Error: Could not process remaining jobs. They might be too large.")
            break

    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Testing
def test_printing_optimization():
    # Test 1: Same priority models
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Test 2: Different priority models
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # lab work
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # thesis
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # personal project
    ]

    # Test 3: Exceeding volume constraints
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Test 1 (same priority):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Print order: {result1['print_order']}")
    print(f"Total time: {result1['total_time']} minutes")

    print("\nTest 2 (different priorities):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Print order: {result2['print_order']}")
    print(f"Total time: {result2['total_time']} minutes")

    print("\nTest 3 (exceeding constraints):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Print order: {result3['print_order']}")
    print(f"Total time: {result3['total_time']} minutes")

if __name__ == "__main__":
    test_printing_optimization()