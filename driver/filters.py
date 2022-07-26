from pyrogram import filters
from typing import List, Union
from config import COMMAND_PREFIXES


other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)
other_filters3 = filters.group & ~filters.edited & ~filters.private

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
