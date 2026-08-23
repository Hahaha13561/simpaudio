from typing import Dict, Any

STRINGS: Dict[str, Dict[str, str]] = {
    "en" : {
        "app_title": "Simpaudio",
        "settings": "Settings",
        "language": "Language",
        "language_restart_notice": "Please restart Simpaudio for language changes to take full effect.",
        "tab_tts": "Text-to-Speech",
        "tab_blending": "Voice Blending",
        "tab_studio": "Audiobook Studio",
        "tab_stt": "Speech-to-Text",
        "engine": "Engine:",
        "preset": "Preset:",
        "save": "Save",
        "delete": "Delete",
        "ready": "Ready",
    }
}
_current_lang = "en"

def set_language(lang_code: str) -> None:
    global _current_lang
    if lang_code in STRINGS:
        _current_lang = lang_code


def get_language() -> str:
    return _current_lang

def get_available_languages() -> Dict[str, str]:
    return {
        "en": "English"
    }

def t(key: str, **kwargs: Any) -> str:
    lang_dict = STRINGS.get(_current_lang, STRINGS["en"])
    text = lang_dict.get(key) or STRINGS["en"].get(key, key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text