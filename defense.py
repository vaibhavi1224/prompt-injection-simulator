def is_prompt_safe(prompt: str) -> bool:
    risky_keywords = ["ignore", "bypass", "disregard", "override", "forget", "pretend", "jailbreak"]
    prompt_lower = prompt.lower()
    return not any(keyword in prompt_lower for keyword in risky_keywords)
