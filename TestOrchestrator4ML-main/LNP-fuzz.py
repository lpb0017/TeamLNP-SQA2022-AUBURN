import traceback
from typing import Any, List

import numpy as np

from generation.py_parser import getImport
from label_perturbation_attack.knn import predict, calculate_k
from label_perturbation_attack.main import calculate_stat, call_prob


def fuzz(method, fuzzer: List[Any]):
    for y in fuzzer:
        try:
            result = method(*y)
        except Exception as exc:
            print(f"FUZZ: {method.__name__} fail")
            traceback.print_exc()
        else:
            print(f"FUZZ: {method.__name__} pass ({result})")
  

if __name__ == "__main__":
    fuzz_targets = [
        (
            getImport, [
                (None),
                (1),
                (1.0),
                ("NLP GROUP", "GROUP PROJECT"),
            ]
        ),
        (
            predict, [
                (None, None),
                ("SQA", "FINAL"),
                ([], {}),
                (float("INF"), float("INF")),
                (float("-INF"), float("INF")),
                (1j, 1),
                (np.NAN, np.NAN)
            ]
        ),
        (
            calculate_k, [
                ([]),
                (None, 0, 0, 0),
                (None, 1.0, 2.0, 3.0),
                (None, "SQA PROJECT", "String 2", "String 3"),
                (None, [None, None, None], 1.2, "String 4"),
                (None, np.zeros((1, 50)), 0, 0),
            ]
        ),
        (
            calculate_stat, [
                (None, None),
                (0),
                (1.0, 2.0),
                ([], []),
                ("APPLE", "PIE"),
            ]
        ),
        (
            call_prob, [
                (0, 0, None),
                (None, None, 0),
                ("APPLE", "MACBOOK", 1.0),
                (float("-inf"), float("inf"), []),
                ([], [], "SQA PROJECT"),
            ]
        )

    ]
    for method, y in fuzz_targets:
        fuzz(method, y)

    