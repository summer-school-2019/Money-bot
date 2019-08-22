try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config

# START COMMAND MODULE STRINGS
START_COMMAND_TEXT = (
    "Для заработка по партнерской программе вам нужно пригласить {required_referees_amount} "
    "пользователей.\nВы пригласили пользователей: {user_referee_amount}.\nВаша ссылка для "
    "приглашения: {invite_link}\n\nВНИМАНИЕ!!! Бот полностью БЕСПЛАТНЫЙ и не требует никаких "
    "платежей!"
)

# MAIN MENU MODULE STRINGS
MAIN_MENU_BUTTONS_LABELS = {
    "earn": "🤑 Заработать",
    "play": "🎲 Играть",
    "balance": "💰 Баланс",
    "invite": "👥 Пригласить друзей",
    "withdrawal": "📬 Вывод",
    "rules": "📑 Правила",
}

# EARN MODULE STRINGS
EARN_MENU_TEXT = {
    "new_task": "Подпишись на группу {channel_name} и заработай " + str(config.JOIN_GROUP_REWARD) + " монет!",
    "group_check_success": f"Вам начислено {config.JOIN_GROUP_REWARD} руб за успешно выполненое задание!\nЕсли в "
                           f"течении 5-ти дней Вы отпишитесь от группы - бот проверит и оштрафует Вас на "
                           f"{config.JOIN_GROUP_REWARD} руб",
    "group_check_failed": "Вы не подписаны на группу",
    "task_cancelled": "✖️ задание удалено",
    "no_tasks": "Задания для вас закончились, попробуйте позже",
    "bad_group": "✖️ Возникла проблема с группой, попробуйте другое задание",
}

# BALANCE MODULE STRINGS
BALANCE_MENU_TEXT = {
    "balance_info": """💰 На вашем балансе: {money} руб.
📢 Вы пригласили: {invited_count}."""
}

# INVITE MODULE STRINGS
INVITE_BUTTON_TEXT = (
    "За приглашенного пользователя начисляется {referral_reward} руб.\nВы пригласили пользователей: {"
    "user_referees_amount}.\nВаша ссылка для приглашения: {referral_link}\n\nВНИМАНИЕ!!! Бот полностью БЕСПЛАТНЫЙ и "
    "не требует никаких платежей! "
)
INVITE_LINK = "https://t.me/{bot_name}?start=referrer_id_{referrer_id}"

# WITHDRAWAL MODULE STRINGS
WITHDRAWAL_TEXT = "❗ Вывод через QIWI ❗\n💰 На вашем балансе: {user_money_amount} руб.\n📢 Вы пригласили: {" \
                  "user_referee_amount}.\n📝 Минимальная сумма вывода: {money_amount_to_enable_withdrawal} руб.\nВаш " \
                  "статус: {user_status}.\n\n"

WITHDRAWAL_REFEREES_AMOUNT_PROBLEM_TEXT = "Чтобы пройти верификацию и выводить в дальнейшем заработанные средства, " \
                                          "пригласите по своей партнерской ссылке минимум {required_referees_amount} " \
                                          "человек.\nВаша ссылка для приглашения: {referral_link}"

WITHDRAWAL_MONEY_AMOUNT_PROBLEM_TEXT = "Чтобы пройти верификацию и выводить в дальнейшем заработанные средства, " \
                                       "вы должны накопить минимум {required_money_amount} руб.\nВыполняйте " \
                                       "задания и приглашайте друзей, чтобы сделать это быстрее."

WITHDRAWAL_ASK_NUMBER_TEXT = "Введите номер qiwi кошелька для вывода.\nПример - \"+79089860283\":"

WITHDRAWAL_ASK_MONEY_AMOUNT_TEXT = "Введите сумму, которую нужно вывести.\nПример - \"100\":"

WITHDRAWAL_ASK_PHONE_NUMBER_ERROR_TEXT = "Введите корректный номер!"

WITHDRAWAL_ASK_MONEY_AMOUNT_ERROR_TEXT = "Введите корректную сумму!"

# RULES MODULE STRINGS
RULES_BUTTON_TEXT = (
    "С помощью этого бота можно хорошо заработать! Выполняйте задания и зарабатывайте деньги!\n\nДля "
    "получения доступа к выводу средств, необходимо пригласить {required_referee_amount} "
    "пользователей.\nВы пригласили пользователей: {user_referee_amount}\nВаша ссылка для приглашения: "
    "{user_referral_link}\n\nБот полностью БЕСПЛАТНЫЙ и не требует никаких платежей!\n\nЗа "
    "приглашенного пользователя начисляется {referral_fee} руб.\nМинимум на вывод: "
    "{money_to_enable_withdrawal} руб.\nВаш текущий баланс: {user_money_amount} руб."
)

# REVIEW MODE MODULE STRINGS
REVIEW_MODE_WARNING_TEXT = "Данный функционал недоступен в режиме презентации."

# VERIFY MODE
VERIFIED_TRUE_LABEL = "Верифицирован"
VERIFIED_FALSE_LABEL = "Неверифицирован"