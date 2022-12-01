import traceback
from typing import Any, List

import numpy as np

from generation.py_parser import getImport
from label_perturbation_attack.knn import prepare_data, calculate_k
from label_perturbation_attack.main import calculate_stat, repeat_experiment


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
                (None, None),
                (1, 2),
                (1.0, 2.0),
                ("NLP GROUP", "GROUP PROJECT"),
            ]
        ),
        (
            prepare_data, [
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
                (None, 0),
                (None, 1.0),
                (None, "SQA PROJECT"),
                (None, [None, None, None]),
                (None, np.zeros((1, 50))),
            ]
        ),
        (
            calculate_stat, [
                (None,),
                (0,),
                (1.0,),
                ([],),
                ("APPLE",),
            ]
        ),
        (
            repeat_experiment, [
                (0, 0, None,),
                (None, None, 0,),
                ("APPLE", "MACBOOK", 1.0,),
                (float("-inf"), float("inf"), [],),
                ([], [], "SQA PROJECT",),
            ]
        )

    ]
    for method, y in fuzz_targets:
        fuzz(method, y)

    