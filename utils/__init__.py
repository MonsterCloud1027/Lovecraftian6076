"""Utils package for CoC Solo module"""
# Streamlit is optional - only needed for Streamlit UI
try:
    import streamlit as st
    _HAS_STREAMLIT = True
except ImportError:
    _HAS_STREAMLIT = False
    st = None

from .logging import init_logger, get_logger, log_message, stop_logger, log_system, log_tool_call


def initialize_session_state() -> None:
	"""Initialize Streamlit session state variables"""
	if not _HAS_STREAMLIT:
		raise ImportError("streamlit is required for initialize_session_state")
	if "character" not in st.session_state:
		st.session_state["character"] = None
	if "messages" not in st.session_state:
		st.session_state["messages"] = []
	if "current_scene" not in st.session_state:
		st.session_state["current_scene"] = "arrival_village"
	if "_debug_mode" not in st.session_state:
		st.session_state["_debug_mode"] = False


def save_character(
	name: str,
	str_attr: int, int_attr: int, pow_attr: int,
	spot: int, listen: int, stealth: int, charm: int, luck: int,
	san: int,
	avatar: str = None,
	background_story: str = ""
) -> None:
	"""Save character data to session state"""
	if not _HAS_STREAMLIT:
		raise ImportError("streamlit is required for save_character")
	st.session_state["character"] = {
		"name": name.strip(),
		"str": int(str_attr),
		"int": int(int_attr),
		"pow": int(pow_attr),
		"spot": int(spot),
		"listen": int(listen),
		"stealth": int(stealth),
		"charm": int(charm),
		"luck": int(luck),
		"san": int(san),
		"avatar": avatar,
		"background_story": background_story.strip() if background_story else "",
	}


__all__ = [
	'initialize_session_state',
	'save_character',
	'init_logger',
	'get_logger',
	'log_message',
	'stop_logger',
	'log_system',
	'log_tool_call',
]

