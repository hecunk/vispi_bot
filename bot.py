import aiogram
import logging

import aiogram.fsm
import aiogram.fsm.state

from states import *

logging.basicConfig(level=logging.INFO)

bt =  aiogram.Bot(token='YOUR-TOKEN')
dis = aiogram.Dispatcher()
aiogram.fsm.state.default_state = States.normal

class vikkipo_class:
    text = 'no text :('

from handlers.start import *