

from telebot.types import LabeledPrice, ShippingOption




token = ""


wlc_msg1 = 'Здравствуйте. \n\n\
*Я — централизованая система телемедицины*, \n\
которая поможет Вам перепроверить диагноз врача \n\
и провести профилактическое обследование.'


wlc_msg2 = '*Учитывайте факт*, что я не являюсь заменой квалифицированного специалиста;\n*мои диагнозы носят ' \
           'рекомендательный характер*!'
wlc_msg3 = 'Какой вопрос Вас беспокоит?'

wlc_msg4 = 'Если вы не можете выбрать нужный вид заболевания, то отправьте мне четкую фотографию, я попытаюсь ' \
           'помочь Вам с этим.'

recomendations1 = 'Вам необходимо сфотографировать и отправить родинку, которая вас беспокоит.\n'\
'Будет лучше, если вы будете следовать небольшим рекомендациям:'
recomendations2 = '1) *Сфокусируйте камеру* на беспокоящей вас родинке'
recomendations3 = '2) Желательно чтобы эта *родинка была единственной* в кадре'
recomendations4 = '3) Расположите родинку примерно *по центру* фотографии'
recomendations5 = 'Пример фотографии, соответствующей условиям:'