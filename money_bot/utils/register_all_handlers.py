from money_bot.handlers import balance_handlers, commands_handlers, earn_handlers, main_menu_buttons_handlers


def register_all_handlers(dp):
    commands_handlers.register_handlers(dp)
    main_menu_buttons_handlers.register_handlers(dp)
    earn_handlers.register_all_handlers(dp)
    balance_handlers.register_all_handlers(dp)
