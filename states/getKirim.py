from aiogram.dispatcher.filters import state
class GetKirim(state.StatesGroup):
    tur = state.State()
    nomi = state.State()
    qiymat= state.State()
    tasdiq = state.State()

class GetChiqim(state.StatesGroup):
    tur = state.State()
    nomi = state.State()
    qiymat= state.State()
    tasdiq = state.State()