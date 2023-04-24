from aiogram.dispatcher.filters import state
class infoState(state.StatesGroup):
    type = state.State()
    time = state.State()
