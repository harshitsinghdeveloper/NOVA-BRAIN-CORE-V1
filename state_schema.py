"""

Module: StateSchema
Author: Harshit Singh

___

General Function: 

- Global state utilized in architecture to allow for effective communication with modules; updating relevant
information about active context

- Global state allows for relay of information in an organized manner, with its finalized structured package/container
storing the active context in long term memory context

- Without this, the system is bound to fail with weak state continuity being the primary factor

___

Global State Update Flow:

Perception layer (excluding SensoryListener) --> Attention and Salience Layer
--> Working Memory Layer --> Executive Controller Layer (not updated) --> 
Reasoning / Planning Layer (not updated) --> Self Evaluation Layer (Begin updating again)
--> Output Layer --> Timing and Habit Layer --> Hippocampus Layer (Final storage of schema structured package)


Note: 

- The bridge fusion receives and maintains the active context
- From there, bridge fusion updates the active context in the global state container and 
  tags habitual/repetitive patterns

___ 

Benefits: 

1. Consistent structure - allowing for traceability when system scales
2. Unified state for all modules to allow for persistant updating
3. Organized container for storage in long term context memory

___

Why is it necessity? 

1. To migtate system unpredictability
2. Debugging becomes impossible / a nightmare without a persistant state
3. Modules conflict with each other, hindering coherence with the ContrexController 

CortexController - Main Orchestrator of Cognition for this system

"""

from copy import deepcopy

class StateSchema:
    min_content_length = 1

    def __init__(self) -> None:
        self.state = {
            "raw_input": None,
            "structured_input": None,
            "intent": None,
            "priority_score": None,
            "active_goal": None,
            "working_context": {},
            "retrieved_memory": [],
            "decision": None,
            "confidence": None,
            "final_output": None,
        }

    def get_global_state(self) -> dict:
        return deepcopy(self.state)

    def get_raw_input(self):
        return self.state["raw_input"]

    def get_structured_input(self):
        return self.state["structured_input"]

    def get_intent(self):
        return self.state["intent"]

    def get_priority_score(self):
        return self.state["priority_score"]

    def get_active_goal(self):
        return self.state["active_goal"]

    def get_working_context(self):
        return self.state["working_context"]

    def get_retrieved_memory(self):
        return self.state["retrieved_memory"]

    def get_decision(self):
        return self.state["decision"]

    def get_confidence(self):
        return self.state["confidence"]

    def get_final_output(self):
        return self.state["final_output"]

    def _is_valid_text(self, content: str) -> bool:
        return isinstance(content, str) and len(content.strip()) >= self.min_content_length

    def _is_valid_collection(self, content) -> bool:
        return isinstance(content, (dict, list)) and len(content) > 0

    def _is_valid_number(self, content) -> bool:
        return isinstance(content, (int, float))

    def set_raw_input(self, content: str) -> None:
        if(self._is_valid_text(content)):
            self.state["raw_input"] = content

    def set_structured_input(self, content: str) -> None:
        if(self._is_valid_text(content)):
            self.state["structured_input"] = content

    def set_intent(self, content: str) -> None:
        if(self._is_valid_text(content)):
            self.state["intent"] = content

    def set_priority_score(self, content: float | int) -> None:
        if(self._is_valid_number(content)):
            self.state["priority_score"] = content

    def set_active_goal(self, content: str) -> None:
        if(self._is_valid_text(content)):
            self.state["active_goal"] = content

    def set_working_context(self, content: dict) -> None:
        if(self._is_valid_collection(content)):
            self.state["working_context"] = content

    def set_retrieved_memory(self, content: list) -> None:
        if(self._is_valid_collection(content)):
            self.state["retrieved_memory"] = content

    def set_decision(self, content: str) -> None:
        if(self._is_valid_text(content)):
            self.state["decision"] = content

    def set_confidence(self, content: float | int) -> None:
        if(self._is_valid_number(content)):
            self.state["confidence"] = content

    def set_final_output(self, content: str) -> None:
        if(self._is_valid_text(content)):
            self.state["final_output"] = content

    def update_raw_input(self, new_content: str) -> None:
        self.set_raw_input(new_content)

    def update_structured_input(self, new_content: str) -> None:
        self.set_structured_input(new_content)

    def update_intent(self, new_content: str) -> None:
        self.set_intent(new_content)

    def update_priority_score(self, new_content) -> None:
        self.set_priority_score(new_content)

    def update_active_goal(self, new_content: str) -> None:
        self.set_active_goal(new_content)

    def update_working_context(self, new_content: dict) -> None:
        self.set_working_context(new_content)

    def update_retrieved_memory(self, new_content: list) -> None:
        self.set_retrieved_memory(new_content)

    def update_decision(self, new_content: str) -> None:
        self.set_decision(new_content)

    def update_confidence(self, new_content) -> None:
        self.set_confidence(new_content)

    def update_final_output(self, new_content: str) -> None:
        self.set_final_output(new_content)

    def reset_runtime_fields(self) -> None:
        self.state["raw_input"] = None
        self.state["structured_input"] = None
        self.state["intent"] = None
        self.state["priority_score"] = None
        self.state["active_goal"] = None
        self.state["working_context"] = {}
        self.state["retrieved_memory"] = []
        self.state["decision"] = None
        self.state["confidence"] = None
        self.state["final_output"] = None

    def __repr__(self) -> str:
        return (
            f"\nStateSchema(\n"
            f"  raw_input={self.state['raw_input']},\n"
            f"  structured_input={self.state['structured_input']},\n"
            f"  intent={self.state['intent']},\n"
            f"  priority_score={self.state['priority_score']},\n"
            f"  active_goal={self.state['active_goal']},\n"
            f"  working_context={self.state['working_context']},\n"
            f"  retrieved_memory={self.state['retrieved_memory']},\n"
            f"  decision={self.state['decision']},\n"
            f"  confidence={self.state['confidence']},\n"
            f"  final_output={self.state['final_output']}\n"
            f")"
        )