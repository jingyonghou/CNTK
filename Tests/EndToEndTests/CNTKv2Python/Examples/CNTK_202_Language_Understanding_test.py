# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

import os
import re
import numpy

abs_path = os.path.dirname(os.path.abspath(__file__))
notebook = os.path.join(abs_path, "..", "..", "..", "..", "Tutorials", "CNTK_202_Language_Understanding.ipynb")

def test_cntk_204_sequence_to_sequence_noErrors(nb):
    errors = [output for cell in nb.cells if 'outputs' in cell
              for output in cell['outputs'] if output.output_type == "error"]
    print(errors)
    assert errors == []

def test_cntk_204_sequence_to_sequence_trainerror(nb):
    metrics = []
    for cell in nb.cells:
        try:
           if cell.cell_type == 'code':
               m = re.search('\[Evaluation\].* metric = (?P<metric>\d+\.\d+)%', cell.outputs[0]['text'])
               if m:
                   metrics.append(float(m.group('metric')))
        except IndexError:
           pass
        except KeyError:
           pass
    expectedMetrics = [2.7, 2.2, 2.3, 2.1]
    assert numpy.allclose(expectedMetrics, metrics)
