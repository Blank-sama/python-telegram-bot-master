import TeleGenic.ext as tg


token = "5492050200:AAE_SMA0dgZA9-5UOjXTsI8CbSTGWlfuWEI"


updater = tg.Updater(api_key = token, use_context=True)

komi = updater.dispatcher

