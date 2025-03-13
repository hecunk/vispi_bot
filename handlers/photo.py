from aiogram import types
import items
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.enums.parse_mode import ParseMode

normie_cards_message = MediaGroupBuilder()

normie_cards_message.add_photo(types.FSInputFile('handlers/media/1.jpg'), caption=f"{items.norm_cards}", parse_mode=ParseMode.HTML)
normie_cards_message.add_photo(types.FSInputFile('handlers/media/2.jpg'))
normie_cards_message.add_photo(types.FSInputFile('handlers/media/3.jpg'))
normie_cards_message.add_photo(types.FSInputFile('handlers/media/4.jpg'))
normie_cards_message.add_photo(types.FSInputFile('handlers/media/5.jpg'))
normie_cards_message.add_photo(types.FSInputFile('handlers/media/6.jpg'))
normie_cards_message.add_photo(types.FSInputFile('handlers/media/7.jpg'))
normie_cards_message.add_photo(types.FSInputFile('handlers/media/8.jpg'))
normie_cards_message.add_photo(types.FSInputFile('handlers/media/9.jpg'))