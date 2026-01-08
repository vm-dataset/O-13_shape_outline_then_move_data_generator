"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           YOUR TASK PROMPTS                                   ║
║                                                                               ║
║  CUSTOMIZE THIS FILE to define prompts/instructions for your task.            ║
║  Prompts are selected based on task type and returned to the model.           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import random


# ══════════════════════════════════════════════════════════════════════════════
#  DEFINE YOUR PROMPTS
# ══════════════════════════════════════════════════════════════════════════════

PROMPTS = {
    "default": [
        "Show the outline-then-move transformation being applied to the second shape. First convert to outline style, then move up or down according to the established pattern.",
        "Animate the two-step transformation where the shape first becomes outline-only and then moves vertically. The question mark should smoothly transition through both steps.",
        "Complete the visual analogy by showing what the second shape becomes when the same outline-then-move transformation is applied.",
    ],
    
    "outline_then_move": [
        "Show the shape first becoming outline-only and then moving up or down. Both transformations should match the example pattern.",
        "Complete the analogy by revealing the shape with the correct outline style and position.",
        "Animate the two-step transformation: fill-to-outline conversion followed by vertical movement.",
    ],
}


def get_prompt(task_type: str = "default") -> str:
    """
    Select a random prompt for the given task type.
    
    Args:
        task_type: Type of task (key in PROMPTS dict)
        
    Returns:
        Random prompt string from the specified type
    """
    prompts = PROMPTS.get(task_type, PROMPTS["default"])
    return random.choice(prompts)


def get_all_prompts(task_type: str = "default") -> list[str]:
    """Get all prompts for a given task type."""
    return PROMPTS.get(task_type, PROMPTS["default"])
