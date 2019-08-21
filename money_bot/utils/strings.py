try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


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
    "new_task": "Подпишись на группу {channel_name} и заработай " + str(config.MONEY_FOR_GROUP) + " монет!",
    "group_check_success": f"""Вам начислено {config.MONEY_FOR_GROUP} руб за успешно выполненое задание!
Если в течении 5-ти дней Вы отпишитесь от группы - бот проверит и оштрафует Вас на {config.MONEY_FOR_GROUP} руб
""",
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
