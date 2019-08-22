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
    "add_tasks": "➕ Прорекламировать группу",
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
    "subscribe": "Подписаться",
    "get_award": "Забрать награду",
    "skip_task": "Пропустить задание",
    "more_tasks": "Еще задания",
}

# BALANCE MODULE STRINGS
BALANCE_MENU_TEXT = {
    "balance_info": """💰 На вашем балансе: {money} руб.
📢 Вы пригласили: {invited_count}."""
}

# INVITE MODULE STRINGS
INVITE_LINK = "https://t.me/{bot_name}?start=referrer_id_{referrer_id}"

# RULES MODULE STRINGS
RULES_MENU_TEXT = (
    "С помощью этого бота можно хорошо заработать! Выполняйте задания и зарабатывайте деньги!\n\nДля "
    "получения доступа к выводу средств, необходимо пригласить {required_referee_amount} "
    "пользователей.\nВы пригласили пользователей: {user_referee_amount}\nВаша ссылка для приглашения: "
    "{user_referral_link}\n\nБот полностью БЕСПЛАТНЫЙ и не требует никаких платежей!\n\nЗа "
    "приглашенного пользователя начисляется {referral_fee} руб.\nМинимум на вывод: "
    "{money_to_enable_withdrawal} руб.\nВаш текущий баланс: {user_money_amount} руб."
)

# ADD TASKS MODULE STRINGS
ADD_TASKS_MENU_TEXT = {
    "welcome": "Напишите id группы, которую вы хотите прорекламировать",
    "incorrect_group_id": "Некорректный id группы, попробуйте еще раз",
    "check_admin": "Проверить права",
    "give_me_admin": "Теперь дайте мне права администратора в группе, чтобы я смог автоматически "
    "проверять вступления в вашу группу",
    "add_successful": "Ваша группа успешно добавлена для рекламы",
    "admin_failed": "Вы не добавили меня в группу или не сделали администратором, попробуйте снова",
    "task_exists": "Эта группа уже рекламируется, введите другой id",
}
