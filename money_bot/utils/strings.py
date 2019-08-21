try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


# main menu strings
MAIN_MENU_BUTTONS_LABELS = {
    "earn": "🤑 Заработать",
    "play": "🎲 Играть",
    "balance": "💰 Баланс",
    "invite": "👥 Пригласить друзей",
    "withdrawal": "📬 Вывод",
    "rules": "📑 Правила",
}

# earn menu strings
EARN_MENU_TEXT = {
    "new_task": "Подпишись на группу {} и заработай " + str(config.JOIN_GROUP_REWARD) + " монет!",
    "group_check_success": f"""Вам начислено {config.JOIN_GROUP_REWARD} руб за успешно выполненое задание!
Если в течении 5-ти дней Вы отпишитесь от группы - бот проверит и оштрафует Вас на {config.JOIN_GROUP_REWARD} руб 
""",
    "group_check_failed": "Вы не подписаны на группу",
    "task_cancelled": "✖️ задание удалено",
    "no_tasks": "Задания для вас закончились, попробуйте позже",
}

# invite button strings
INVITE_LINK = "https://t.me/{bot_name}?start=referrer_id_{referrer_id}"

# rules button strings
RULES_BUTTON_TEXT = (
    "С помощью этого бота можно хорошо заработать! Выполняйте задания и зарабатывайте деньги!\n\nДля "
    "получения доступа к выводу средств, необходимо пригласить {required_referee_amount} "
    "пользователей.\nВы пригласили пользователей: {user_referee_amount}\nВаша ссылка для приглашения: "
    "{user_referral_link}\n\nБот полностью БЕСПЛАТНЫЙ и не требует никаких платежей!\n\nЗа "
    "приглашенного пользователя начисляется {referral_fee} руб.\nМинимум на вывод: "
    "{money_to_enable_withdrawal} руб.\nВаш текущий баланс: {user_money_amount} руб."
)
