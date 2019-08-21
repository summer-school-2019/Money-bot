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

# RULES MODULE STRINGS
RULES_BUTTON_TEXT = (
    "С помощью этого бота можно хорошо заработать! Выполняйте задания и зарабатывайте деньги!\n\nДля "
    "получения доступа к выводу средств, необходимо пригласить {required_referee_amount} "
    "пользователей.\nВы пригласили пользователей: {user_referee_amount}\nВаша ссылка для приглашения: "
    "{user_referral_link}\n\nБот полностью БЕСПЛАТНЫЙ и не требует никаких платежей!\n\nЗа "
    "приглашенного пользователя начисляется {referral_fee} руб.\nМинимум на вывод: "
    "{money_to_enable_withdrawal} руб.\nВаш текущий баланс: {user_money_amount} руб."
)

# GAME MODULE STRING
GAME_MENU_TEXT = {
    "show_bet": "\U0001F4B8 you have {money} money and your bet is {bet} money \U0001F4B8",
    "rules": "Bitcoin rate is changing every second!\nSolve how it will change and win coins!\n" 
             "You can't bet more money than yot have.",
    "show_money": "\U0001F4B8 You have {money} money now! \U0001F4B8",
    "no_money_to_start": f"Необходимо как минимум {config.MONEY_TO_START_GAME} руб. чтобы начать игру"
}
