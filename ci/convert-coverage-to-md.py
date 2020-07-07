#!/usr/bin/env python

# example
example = '''
============================= test session starts ==============================
platform linux -- Python 3.7.7, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /home/runner/work/Tx-MeshMeasure/Tx-MeshMeasure/MeasureMesh
plugins: cov-2.10.0
collected 13 items

MeasureMesh/MeasureMesh/tests/e2e/test_master.py .                       [  7%]
MeasureMesh/MeasureMesh/tests/unit/test_config.py .                      [ 15%]
MeasureMesh/MeasureMesh/tests/unit/test_filters2d.py .                   [ 23%]
MeasureMesh/MeasureMesh/tests/unit/test_seat_calculator.py .             [ 30%]
MeasureMesh/MeasureMesh/tests/unit/test_waist_calculator.py ...          [ 53%]
MeasureMesh/MeasureMesh/tests/unit/MeasurementTypes/test_measurement.py . [ 61%]
..                                                                       [ 76%]
MeasureMesh/MeasureMesh/tests/unit/MeasurementTypes/test_measurement_json.py . [ 84%]
..                                                                       [100%]

=============================== warnings summary ===============================
/opt/hostedtoolcache/Python/3.7.7/x64/lib/python3.7/site-packages/svg/path/path.py:3
  /opt/hostedtoolcache/Python/3.7.7/x64/lib/python3.7/site-packages/svg/path/path.py:3: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working
    from collections import MutableSequence

MeasureMesh/tests/e2e/test_master.py::test_calculation_master
MeasureMesh/tests/e2e/test_master.py::test_calculation_master
MeasureMesh/tests/unit/test_seat_calculator.py::test_with_trousers
MeasureMesh/tests/unit/test_waist_calculator.py::test_with_trousers
  /opt/hostedtoolcache/Python/3.7.7/x64/lib/python3.7/site-packages/trimesh/graph.py:556: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
    result = np.array(split)

MeasureMesh/tests/unit/test_waist_calculator.py::test_with_cube
  /opt/hostedtoolcache/Python/3.7.7/x64/lib/python3.7/site-packages/trimesh/exchange/ply.py:573: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
    for i in lines])

-- Docs: https://docs.pytest.org/en/latest/warnings.html

----------- coverage: platform linux, python 3.7.7-final-0 -----------
Name                                                                           Stmts   Miss  Cover   Missing
------------------------------------------------------------------------------------------------------------
MeasureMesh/MeasureMesh/CalculationMaster.py                                      21      3    86%   22-24
MeasureMesh/MeasureMesh/MeasurementCalculators/InseamCalculator.py                67      2    97%   88, 117
MeasureMesh/MeasureMesh/MeasurementCalculators/MeasurementCalculatorBase.py       42      4    90%   38, 48, 70, 82
MeasureMesh/MeasureMesh/MeasurementCalculators/SeatCalculator.py                  17      0   100%
MeasureMesh/MeasureMesh/MeasurementCalculators/WaistCalculator.py                 44      3    93%   70-72
MeasureMesh/MeasureMesh/MeasurementCalculators/__init__.py                         4      0   100%
MeasureMesh/MeasureMesh/MeasurementTypes/Measurement.py                           41      5    88%   34, 42, 52, 58, 71
MeasureMesh/MeasureMesh/MeasurementTypes/Measurement1D.py                         22      8    64%   32-40, 44-45
MeasureMesh/MeasureMesh/MeasurementTypes/Measurement2D.py                         53     32    40%   39-53, 59-70, 77-90, 95-108
MeasureMesh/MeasureMesh/MeasurementTypes/__init__.py                               4      0   100%
MeasureMesh/MeasureMesh/__init__.py                                                3      0   100%
MeasureMesh/MeasureMesh/config.py                                                 20      0   100%
MeasureMesh/MeasureMesh/defs.py                                                   24      3    88%   28, 32, 40
MeasureMesh/MeasureMesh/helpers/__init__.py                                        0      0   100%
MeasureMesh/MeasureMesh/helpers/file_helpers.py                                    9      9     0%   4-19
MeasureMesh/MeasureMesh/helpers/filters2d.py                                      29      2    93%   37, 48
MeasureMesh/MeasureMesh/helpers/helpers.py                                         2      2     0%   5-9
MeasureMesh/MeasureMesh/helpers/matrix_helpers.py                                 55     40    27%   12-17, 21-30, 34-42, 46-51, 55-58, 62-67, 72, 78, 84, 91, 95, 99
MeasureMesh/MeasureMesh/helpers/mesh_creators.py                                 104     96     8%   14-31, 40-88, 99-132, 143-176
MeasureMesh/MeasureMesh/helpers/mesh_helpers.py                                   50     30    40%   21-24, 35, 39, 43-46, 53-55, 62-65, 72-75, 82-83, 91, 95, 104-110
MeasureMesh/MeasureMesh/tests/__init__.py                                          0      0   100%
MeasureMesh/MeasureMesh/tests/e2e/test_master.py                                   9      0   100%
MeasureMesh/MeasureMesh/tests/test_helpers.py                                      8      2    75%   11, 19
MeasureMesh/MeasureMesh/tests/unit/MeasurementTypes/__init__.py                    0      0   100%
MeasureMesh/MeasureMesh/tests/unit/MeasurementTypes/test_measurement.py           15      0   100%
MeasureMesh/MeasureMesh/tests/unit/MeasurementTypes/test_measurement_json.py      45      0   100%
MeasureMesh/MeasureMesh/tests/unit/__init__.py                                     0      0   100%
MeasureMesh/MeasureMesh/tests/unit/test_config.py                                 14      0   100%
MeasureMesh/MeasureMesh/tests/unit/test_filters2d.py                              21      0   100%
MeasureMesh/MeasureMesh/tests/unit/test_seat_calculator.py                        19      0   100%
MeasureMesh/MeasureMesh/tests/unit/test_waist_calculator.py                       35      0   100%
------------------------------------------------------------------------------------------------------------
TOTAL                                                                            777    241    69%

======================= 13 passed, 6 warnings in 19.22s ========================


'''

import re
import sys


# text = example

def get_badge_color(value, lookup):
    value = float(value)
    color = "white"
    for k, v in sorted(list(lookup.items())):
        if value > k:
            color = v
    return color


badge = "[![](https://img.shields.io/static/v1?label={label}&message={message}&color={color})]()"

badge_colors = {0: "E60000", 60: "FF7800", 85: "4CBB17"}

blocks = {"execution": [], "warnings": [], "result": []}

template = """
# Result of pytest with coverage

{badge}

<details>
  <summary>Execution</summary>

  ```
    {execution}
  ```
</details>

<details>
  <summary>Warnings</summary>

  ```
    {warnings}
  ```
</details>

```
{result}
```


"""

current_block = None
for line in sys.stdin:
    if "== test session starts ==" in line:
        current_block = "execution"
    elif "== warnings summary ==" in line:
        current_block = "warnings"
    elif "-- coverage" in line:
        current_block = "result"
    elif current_block:
        blocks[current_block].append(line)
        if "TOTAL" in line:
            numbers = re.findall("\d+", line)
            percentage = numbers[-1]

for block in blocks:
    blocks[block] = "\n".join(blocks[block])

badge = badge.format(label="coverage", message=f"{percentage}%", color=get_badge_color(percentage, badge_colors))
new_text = template.format(**blocks, badge=badge)

sys.stdout.write(new_text)
