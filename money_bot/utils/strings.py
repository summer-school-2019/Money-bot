try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


# MAIN MENU STRINGS
MAIN_MENU_BUTTONS_LABELS = {
    "earn": "🤑 Заработать",
    "play": "🎲 Играть",
    "balance": "💰 Баланс",
    "invite": "👥 Пригласить друзей",
    "withdrawal": "📬 Вывод",
    "rules": "📑 Правила",
}

# EARN MENU STRINGS
EARN_MENU_TEXT = {
    "new_task": "Подпишись на группу {channel_name} и заработай " + str(config.MONEY_FOR_GROUP) + " монет!",
    "group_check_success": f"""Вам начислено {config.MONEY_FOR_GROUP} руб за успешно выполненое задание!
Если в течении 5-ти дней Вы отпишитесь от группы - бот проверит и оштрафует Вас на {config.MONEY_FOR_GROUP} руб
""",
    "group_check_failed": "Вы не подписаны на группу",
    "task_cancelled": "✖️ задание удалено",
    "no_tasks": "Задания для вас закончились, попробуйте позже",
    "bad_group": "✖️ Возникла проблема с группой, попробуйте другое задание"
}

# BALANCE MENU STRINGS
BALANCE_MENU_TEXT = {
    "balance_info": """💰 На вашем балансе: {money} руб.
📢 Вы пригласили: {invited_count}."""
}

# INVITE MENU STRINGS
INVITE_BUTTON_STRING = "https://t.me/{bot_name}?start=referrer_id_{user_id}"
