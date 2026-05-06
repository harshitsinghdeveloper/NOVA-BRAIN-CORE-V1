"""

Module: SensoryListener
Author: Harshit Singh

___

General Function: 

- Capture raw input and perform rough quality validation 
- Raw inputs can be in the following forms of modality:

1. Speech 
2. Text
3. Sensors

etc

But, for the sake of V1, we will only process text and keep all the other modalities on standby

___

Important:

- After capturing raw input and performing rough quality validation, the raw input
and its metadata is processed as a packet and transmitted to the central routing hub - ThalamusIO

___

Benefits: 

1. Packet transmission allows for simplified traceability at the initial stage of system runtime
2. Consistent design philosphy and strong state continuity - matching similarly to StateSchema's global container structure
3. Easier data verification (decision making) for ThalamusIO (Note: ThalamusIO does not further validate raw input)

"""

from modality import Modality
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Optional
from uuid import uuid4

@dataclass
class TransmissionPacket:
    packet_id: str
    timestamp: str
    source_type: str      # "text", "speech", "vision", "sensor"
    source_id: str         # "keyboard", "microphone_1", etc.

    raw_input: any         # untouched original input

    input_size: int | float
    is_empty: bool
    is_valid: bool

    # Packet quality criterion
    noise_level: float | None
    confidence: float | None 
    issues: list[str]

    status: str            # "accepted", "rejected", "warning"
    error: str | None

class SensoryListener:
    # Placeholders
    min_text_length = 1
    min_speech_length = 1
    min_sensor_duration = 1

    def __init__(self, input) -> None:
        self.input = input

    def _generate_packet(self) -> dict | None:
        source_type_generated = self._find_source_type(self.input)
        """
        Important: 

        - Don't generate packet information if source type is umambigious or text length is less than or equal to 1
        - Note: Input cannot be a floating point number or integer itself (has to be included in string i.e text content)

        """
        if(source_type_generated == None):
            return None
        
        packet = TransmissionPacket(
            packet_id= self._generate_packet_id(),
            timestamp= self._current_timestamp(),
            source_type = source_type_generated,
            source_id= self._find_source_id(self.input, source_type_generated),
            raw_input=self.input, 
            input_size= self._find_input_size(self.input, source_type_generated), 
            is_empty= self._is_empty(self.input, source_type_generated),
            is_valid= self._is_valid(self.input, source_type_generated),
            noise_level=self._validate_noise_level(self.input),
            confidence= self._find_confidence_score(self.input),
            issues= self._detected_issues(self.input),
            status= self._quality_status(self.input, source_type_generated),
            error= self._transmission_error(self.input, source_type_generated)
        )

        return asdict(packet)
    
    def _generate_packet_id(self) -> str:
        return f"raw-{uuid4()}"

    def _current_timestamp(self) -> str:
        return datetime.utcnow().isoformat()
    
    def _find_source_type(self, input: Any) -> str | None:
        source_type = ""
        
        if(isinstance(input, int) or isinstance(input, float) or input == None):
            return None
        
        elif(isinstance(input, str) and len(input) <= 1):
            # Normalization would not be considered since data quality would likely be of lower quality
            source_type = "text"

        elif(isinstance(input,str)):
            source_type = "text"

        elif(isinstance(input, Modality.Speech)):
            source_type = "speech"

        elif (isinstance(input, Modality.Sensor)):
            source_type = "sensor"

        # Can be expanded further with other modalities

        return source_type
            
    def _find_source_id(self, input: Any, source_type: str) -> str | None:
        if(source_type == "text"):
            pass

        elif(source_type == "speech"):
            Modality.Speech._find_source_id_speech(input)

        elif(source_type == "sensor"):
            Modality.Sensor._find_source_id_sensor(input)

        return "N/A"
    
    def _validate_raw_input(self, input: Any, source_type: str) -> tuple[bool, str]:    
        if(source_type == "text" and len(input.strip()) <=  1):
            return False, "Text quality is not satisfactory for normalization"
        
        elif(source_type == "text" and len(input.strip()) > 1):
            return True, "Text quality is satisfactory for normalization!"
        
        elif(source_type == "speech" and Modality.Speech._compute_speech_length(input) > self.min_speech_length):
            return True, "Speech quality is satisfactory for normalization!"

        # Defined placeholder threshold (above) for sensor duration: 1 second 
        elif(source_type == "sensor" and Modality.Sensor._compute_sensor_duration(input) > self.min_sensor_duration):
            return True, "Sensor information is satisfactory for normalization!"
        
        return False, "Input is not satisfactory for further processing!"

    def _find_input_size(self, input: Any, source_type: str) -> int | float | None:
        input_length = 0
        if(source_type == "text"):
            input_length = len(input)

        elif(source_type == "speech"):
            input_length = Modality.Speech._compute_speech_length(input)

        elif(source_type == "sensor"):
            input_length = Modality.Sensor._compute_sensor_duration(input)

        return input_length

    def _is_empty(self, input: Any, source_type: str) -> bool:
        return self._find_input_size(input, source_type) == 0 

    def _is_valid(self, input: Any, source_type: str) -> bool:
        validated, message = self._validate_raw_input(input, source_type)
        return validated
    
    def _validate_noise_level(self, input: Any) -> None:
        return None
    
    def _find_confidence_score(self, input: Any) -> float:
        # Baseline confidence score 
        # Add calculation for confidence in the future 
        baseline_confidence= 0.5
        return baseline_confidence

    def _detected_issues(self, input: Any) -> list[str]:
        return []

    def _quality_status(self, input: Any, source_type: str) -> str:
        if(self._is_valid(input, source_type)):
            return "accepted"
    
        # Edge Case - Text Content is of length 1 or less
        # Thalamus can handle low quality inputs for routing pipeline

        elif(not(self._is_valid(input, source_type)) and isinstance(input, str) and len(input.strip()) <= 1):
            return "warning"
        
        return "rejected"
    
    def _transmission_error(self, input: Any, source_type: str) -> str:
        if(self._quality_status(input, source_type) == "rejected"):
            return "Cannot transmit packet to Thalamus!"
        
        return "No transparent input errors!"

