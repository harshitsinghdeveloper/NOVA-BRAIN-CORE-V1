"""

Module: Modality
Author: Harshit Singh 

___

General Function: 

- Helper class for non-text modality functions such as Speech, Sensor, etc

"""

from typing import Any, Optional

class Modality:
    class Speech:
        def _compute_speech_length(input: Any) -> float | None:
            # Placeholder
            return 0.0
        
        def _structure_raw_speech(input: Any):
            pass

    class Sensor:
        def _compute_sensor_duration(input: Any) -> float | None:
            # Placeholder 
            return 0.0
        
        def _structure_sensor_information(input: Any):
            pass