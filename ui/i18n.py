from typing import Dict, Any

STRINGS: Dict[str, Dict[str, str]] = {
    "en-us" : {
        "tab_tts": "Text to Speech",
        "tab_blending": "Voice Blending",
        "tab_studio": "Studio",
        "tab_stt": "Transcribe",
        "engine": "Engine:",
        "preset": "Preset:",
        "language": "Language:",
        "save": "Save",
        "delete": "Delete",
        "toggle_theme": "Toggle Theme",
        "ready": "Ready",
        "engine_status": "Engine: {engine}",
        "error_loading_engine": "Error loading engine: {error}",
        "save_preset_title": "Save Preset",
        "preset_name_prompt": "Preset name:",
        "preset_saved": "Preset saved: {name}",
        "delete_preset_title": "Delete Preset",
        "delete_preset_confirm": "Delete preset '{name}'?",
        "preset_deleted": "Preset deleted: {name}",
        "restart_notice_title": "Language Changed",
        "restart_notice_msg": "Please restart Simpaudio for language changes to take full effect.",
        "voice": "Voice:",
        "format": "Format:",
        "speed": "Speed:",
        "volume": "Volume:",
        "import_text_file": "Import Text File",
        "ssml_editor": "SSML Editor",
        "ssml_mode": "SSML Mode",
        "chars_words_count": "Chars: {chars}  |  Words: {words}",
        "choose_save_location": "Choose Save Location",
        "no_location_selected": "No location selected",
        "srt": "SRT",
        "preview": "Preview",
        "generate_audio": "Generate Audio",
        "generating_audio": "Generating audio...",
        "finished": "Finished!",
        "success": "Success",
        "audio_saved": "Audio saved successfully!\n{path}",
        "srt_exported": "\nSRT subtitles exported.",
        "no_text_title": "No Text",
        "no_text_msg": "Please enter some text to convert to speech.",
        "no_location_title": "No Location",
        "no_location_msg": "Please choose a save location first.",
        "no_voice_title": "No Voice",
        "no_voice_msg": "No voice available for this engine/language.",
        "no_preview_title": "No Preview",
        "no_preview_msg": "Generate audio first, then preview it.",
        "playback_error_title": "Playback Error",
        "generation_error_title": "Generation Error",
        "generation_error_msg": "An error occurred:\n\n{error}",
    },

    "en-gb": {
        "tab_tts": "Text to Speech",
        "tab_blending": "Voice Blending",
        "tab_studio": "Studio",
        "tab_stt": "Transcribe",
        "engine": "Engine:",
        "preset": "Preset:",
        "language": "Language:",
        "save": "Save",
        "delete": "Delete",
        "toggle_theme": "Toggle Theme",
        "ready": "Ready",
        "engine_status": "Engine: {engine}",
        "error_loading_engine": "Error loading engine: {error}",
        "save_preset_title": "Save Preset",
        "preset_name_prompt": "Preset name:",
        "preset_saved": "Preset saved: {name}",
        "delete_preset_title": "Delete Preset",
        "delete_preset_confirm": "Delete preset '{name}'?",
        "preset_deleted": "Preset deleted: {name}",
        "restart_notice_title": "Language Changed",
        "restart_notice_msg": "Please restart Simpaudio for language changes to take full effect.",
        "voice": "Voice:",
        "format": "Format:",
        "speed": "Speed:",
        "volume": "Volume:",
        "import_text_file": "Import Text File",
        "ssml_editor": "SSML Editor",
        "ssml_mode": "SSML Mode",
        "chars_words_count": "Chars: {chars}  |  Words: {words}",
        "choose_save_location": "Choose Save Location",
        "no_location_selected": "No location selected",
        "srt": "SRT",
        "preview": "Preview",
        "generate_audio": "Generate Audio",
        "generating_audio": "Generating audio...",
        "finished": "Finished!",
        "success": "Success",
        "audio_saved": "Audio saved successfully!\n{path}",
        "srt_exported": "\nSRT subtitles exported.",
        "no_text_title": "No Text",
        "no_text_msg": "Please enter some text to convert to speech.",
        "no_location_title": "No Location",
        "no_location_msg": "Please choose a save location first.",
        "no_voice_title": "No Voice",
        "no_voice_msg": "No voice available for this engine/language.",
        "no_preview_title": "No Preview",
        "no_preview_msg": "Generate audio first, then preview it.",
        "playback_error_title": "Playback Error",
        "generation_error_title": "Generation Error",
        "generation_error_msg": "An error occurred:\n\n{error}",
    }
}
_CURRENT_LANG = "en-us"

LANG_MAP = {
    "en-us": "English (US)",
    "en-gb": "English (UK)",
    "es": "Español",
    "fr-fr": "Français",
    "it": "İtaliano",
    "pt-br": "Português",
    "zh": "中国人",
    "ja": "日本語"
}

def set_language(lang_code: str) -> None:
    global _CURRENT_LANG
    if lang_code in STRINGS:
        _CURRENT_LANG = lang_code


def get_language() -> str:
    return _CURRENT_LANG

def get_available_languages() -> Dict[str, str]:
    return LANG_MAP.copy()

def t(key: str, **kwargs: Any) -> str:
    lang_dict = STRINGS.get(_CURRENT_LANG, STRINGS["en-us"])
    template = lang_dict.get(key) or STRINGS["en-us"].get(key, key)
    if kwargs:
        try:
            return template.format(**kwargs)
        except KeyError:
            return template
    return template