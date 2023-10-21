import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

'''❗️✨Ссылка на бота: https://t.me/std_assist_bot✨❗️'''

state_storage = StateMemoryStorage()

bot = telebot.TeleBot("6560476325:AAHKO3tmz_yWUD9HrZQBQhXkUt1Xlp71iPs",
                      state_storage=state_storage, parse_mode='Markdown')
id_my = 6597025411
bot.send_message(id_my, '✅Бот запущен✅')

class PollState(StatesGroup):
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


text_poll = "Давай знакомиться"
text_button_1 = "Помощь в учёбе"
text_button_2 = "Лайтовый плейлист"
text_button_3 = "Хочу кушать"


text_b_1 = "🏫‍🎓📚*Вот 5 лайфхаков, которые помогут тебе лучше учиться и усваивать информацию:*\n\n"\
    "❇️️1️⃣ Разбейте материал на небольшие части: Пытаться запомнить большой объем информации сразу может быть сложно. " \
        "Разделите материал на более мелкие и усвояйте их постепенно. Это поможет вам лучше сосредоточиться и запомнить информацию.\n\n"\
    "❇️2️⃣ Создайте систему ассоциаций: Связывайте новую информацию с уже известными концепциями или картинками. " \
        "Это позволяет вам легче запоминать и восстанавливать информацию, удерживая связи между различными понятиями.\n\n"\
    "❇️3️⃣ Применяйте активные методы обучения: Вместо пассивного чтения статьи или учебника активно участвуйте в обучении. " \
        "Пишите свои заметки, обсуждайте материал с другими людьми или попробуйте преподавать изучаемый предмет самому себе.\n\n"\
    "❇️4️⃣ Используйте разнообразные источники информации: Разнообразие источников помогает лучше понять и запомнить информацию. " \
        "Включайте различные книги, видео, видеолекции и другие ресурсы, чтобы рассмотреть предмет с разных точек зрения.\n\n"\
    "❇️5️⃣ Организуйте регулярные повторения: Разделите время на регулярные сессии повторения изученного материала. " \
        "Повторение помогает закрепить информацию в памяти и предотвратить забывание.\n"\
    "Надеюсь, эти лайфхаки помогут тебе в учебе! Удачи!"
text_b_2 = "[✨🎧🎧🎧✨Тут](https://music.yandex.ru/users/Pchi.Hi/playlists/1029) ты найдёшь лайтовую [(лёгкую, спокойную) музыку](https://music.yandex.ru/users/Pchi.Hi/playlists/1029).\n" \
           "Её можно слушать во время выполнения дз.\n"
text_b_3 = "🍱Вот список из пяти простых, но очень интересных и вкусных блюд, которые можно приготовить студентам с ограниченными продуктами:\n\n"\
"💡1️⃣ Макароны с сыром:\n🧀🍝\n"\
"         - Приготовьте макароны согласно инструкции на упаковке.\n"\
"         - Отдельно нагрейте молоко и добавьте натертый сыр, чтобы получить соус.\n"\
"         - Полейте макароны готовым сырным соусом и перемешайте.\n\n"\
"💡2️⃣ Рисовая каша с тушёными овощами:\n🍚🥕🧅🍅\n"\
"         - Сварите рис по инструкции на упаковке.\n"\
"         - На сковороде нагрейте масло и обжарьте нарезанные овощи (морковь, лук, помидоры и т.д.) до мягкости.\n"\
"         - Добавьте овощи к рису, перемешайте и дайте прогреться.\n\n"\
"💡3️⃣ Омлет с овощами:\n🍳🧅🍅\n"\
"         - Взбейте яйца с солью и перцем в миске.\n"\
"         - На сковороде нагрейте масло и обжарьте мелко нарезанные овощи (паприку, помидоры, лук и т.д.) до мягкости.\n"\
"         - Влейте взбитые яйца на сковороду и готовьте омлет до готовности.\n\n"\
"💡4️⃣ Гречка с курицей:\n🍚🍖\n"\
"         - Сварите гречку по инструкции на упаковке.\n"\
"         - На сковороде нагрейте масло и обжарьте нарезанную куриную грудку до золотистой корочки.\n"\
"         - Добавьте готовую гречку и перемешайте с курицей.\n\n"\
"💡5️⃣ Тост с авокадо и яйцом:\n🥪🍳🥑\n"\
"         - Намажьте хлеб ломтиком авокадо.\n"\
"         - На сковороде нагрейте масложарьте яйцо (можно выбрать желательную степень прожарки).\n"\
"         - Положите яйцо на тост с авокадо."


menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    name = f'\nName:, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(id_my, str(message.chat.id) + name + ':\nНовый пользователь')
    bot.send_message(
        message.chat.id,
        'Привет! Я помощник-асистент для студентов.',
        reply_markup=menu_keyboard)

@bot.message_handler(func=lambda message: text_poll == message.text)
def first(message):
    bot.send_message(message.chat.id, 'Супер! Ваше имя?')
    bot.set_state(message.from_user.id, PollState.name, message.chat.id)


@bot.message_handler(state=PollState.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    bot.send_message(message.chat.id, 'Супер! Ваш возраст?')
    bot.set_state(message.from_user.id, PollState.age, message.chat.id)


@bot.message_handler(state=PollState.age)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text
    bot.send_message(message.chat.id, 'Спасибо за регистрацию!', reply_markup=menu_keyboard)
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, text_b_1, reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, text_b_2, reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, text_b_3, reply_markup=menu_keyboard)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()