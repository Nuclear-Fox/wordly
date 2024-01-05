# -*- coding: utf-8 -*-

import random
import json
from flask import Response

unactive = 0
no_place = 1
wrong_place = 2
right_place = 3

def get_word():
    return words[random.randint(0, len(words) - 1)]

def check_word(word, result_word):
    if (result_word not in words):
        return Response("Такого слова не существует!", status=400)
    elif (word == result_word):
        return Response(json.dumps([right_place, right_place, right_place, right_place, right_place]), status=200)
    else:
        result = []
        for i in range(0, len(word)):
            if (result_word[i] == word[i]):
                result.append(right_place)
            else:
                find_res = word.find(result_word[i])
                if (find_res == -1):
                    result.append(no_place)
                elif (find_res == i):
                    result.append(right_place)
                else:
                    result.append(wrong_place)
        #print(result)
        return Response(json.dumps(result), status=444)


words = [
  'аббат',
  'абзац',
  'аборт',
  'аванс',
  'аврал',
  'автор',
  'миска',
  'кокос',
  'сонет',
  'бугор',
  'агент',
  'адрес',
  'азарт',
  'айран',
  'актер',
  'актив',
  'акула',
  'акциз',
  'акция',
  'алиби',
  'аллея',
  'алмаз',
  'амбал',
  'амбар',
  'амеба',
  'ампер',
  'ангел',
  'арбуз',
  'арена',
  'арест',
  'ариец',
  'армия',
  'архив',
  'аршин',
  'аскет',
  'астма',
  'астра',
  'атака',
  'атлас',
  'атлет',
  'атолл',
  'аудит',
  'афера',
  'афиша',
  'ацена',
  'багаж',
  'багги',
  'багет',
  'базар',
  'базис',
  'байка',
  'балда',
  'балет',
  'балка',
  'балык',
  'банан',
  'банда',
  'банка',
  'барак',
  'баран',
  'баржа',
  'барин',
  'басня',
  'батат',
  'батон',
  'батут',
  'бахча',
  'бачок',
  'башня',
  'бегун',
  'бедро',
  'бекас',
  'бекон',
  'белка',
  'белок',
  'белье',
  'беляш',
  'берег',
  'берет',
  'бетон',
  'билет',
  'бинго',
  'биржа',
  'бирка',
  'битва',
  'бланк',
  'блеск',
  'блоха',
  'блуза',
  'блюдо',
  'бляха',
  'бобер',
  'бобик',
  'богач',
  'бойня',
  'бокал',
  'болид',
  'бомба',
  'бонус',
  'бочка',
  'брань',
  'брасс',
  'бремя',
  'бренд',
  'брешь',
  'бровь',
  'бронь',
  'броня',
  'брошь',
  'брюки',
  'брюхо',
  'бубен',
  'будка',
  'буква',
  'букет',
  'булка',
  'буран',
  'бутик',
  'бутон',
  'буфер',
  'буфет',
  'быдло',
  'валет',
  'валик',
  'валун',
  'вагон',
  'вальс',
  'варан',
  'варяг',
  'вафля',
  'вброс',
  'вдова',
  'ведро',
  'велюр',
  'веник',
  'венок'
  'вепрь',
  'верба',
  'верфь',
  'весло',
  'весна',
  'ветвь',
  'ветер',
  'ветка',
  'вечер',
  'взвод',
  'вздох',
  'взлет',
  'взлом',
  'взмах',
  'взрыв',
  'видео',
  'визаж',
  'визир',
  'визит',
  'визор',
  'вилка',
  'вилла',
  'вираж',
  'вирус',
  'висок',
  'виток',
  'вихор',
  'вихрь',
  'вишня',
  'вклад',
  'вобла',
  'водка',
  'вожак',
  'вождь',
  'возня',
  'война',
  'вокал',
  'волна',
  'волос',
  'волхв',
  'вольт',
  'вопль',
  'ворон',
  'ворот',
  'ворох',
  'вотум',
  'вояка',
  'время',
  'вуаль',
  'въезд',
  'выбор',
  'вывих',
  'вывод',
  'выгул',
  'выдох',
  'выдра',
  'выезд',
  'вызов',
  'выкат',
  'выкуп',
  'вылет',
  'вылов',
  'вынос',
  'выпад',
  'выпас',
  'вырез',
  'выход',
  'вычет',
  'вьюга',
  'вязка',
  'газон',
  'гайка',
  'галка',
  'галон',
  'гараж',
  'гарем',
  'гелий',
  'герой',
  'гетто',
  'гжель',
  'гидра',
  'гиена',
  'гирло',
  'глава',
  'глина',
  'глист',
  'глубь',
  'глушь',
  'глыба',
  'гнида',
  'гниль',
  'говор',
  'гогот',
  'голем',
  'голод',
  'голос',
  'гольф',
  'голяк',
  'гонец',
  'гонка',
  'гопак',
  'горка',
  'горло',
  'город',
  'горох',
  'гость',
  'грамм',
  'грант',
  'грань',
  'графа',
  'гриль',
  'грипп',
  'гроза',
  'груда',
  'грудь',
  'грунт',
  'груша',
  'грыжа',
  'грязь',
  'гуашь',
  'губка',
  'гудок',
  'гуляш',
  'гусар',
  'давка',
  'дамба',
  'дартс',
  'дверь',
  'дебош',
  'дебют',
  'девиз',
  'девка',
  'декан',
  'декор',
  'демон',
  'дефис',
  'джинн',
  'дзюдо',
  'диван',
  'диета',
  'диско',
  'длань',
  'длина',
  'днище',
  'добро',
  'довод',
  'догма',
  'дождь',
  'дозор',
  'дойка',
  'долма',
  'домен',
  'домик',
  'домна',
  'домра',
  'донор',
  'донос',
  'доска',
  'досуг',
  'досье',
  'доход',
  'дочка',
  'драже',
  'драка',
  'дрель',
  'дрифт',
  'дробь',
  'дрова',
  'дрожь',
  'дрозд',
  'дрофа',
  'дубль',
  'дупло',
  'дурак',
  'душка',
  'дуэль',
  'дымка',
  'дюшес',
  'дятел',
  'евнух',
  'еврей',
  'егерь',
  'ездок',
  'ересь',
  'ершик',
  'есаул',
  'жажда',
  'жакет',
  'жарка',
  'жатва',
  'желоб',
  'желчь',
  'жених',
  'жердь',
  'жерло',
  'жесть',
  'жетон',
  'живот',
  'жизнь',
  'жилет',
  'жираф',
  'жокей',
  'жрица',
  'жулик',
  'забег',
  'забой',
  'забор',
  'завал',
  'завет',
  'завод',
  'загар',
  'загиб',
  'загон',
  'задел',
  'задор',
  'заезд',
  'зажим',
  'зазор',
  'заика',
  'заказ',
  'закал',
  'закат',
  'закон',
  'закуп',
  'залив',
  'залог',
  'залом',
  'замах',
  'замер',
  'замес',
  'замок',
  'замша',
  'занос',
  'запад',
  'запал',
  'запас',
  'запах',
  'запор',
  'зарин',
  'заруб',
  'заряд',
  'засор',
  'засос',
  'затея',
  'затон',
  'затор',
  'зацеп',
  'звено',
  'зверь',
  'зебра',
  'зевок',
  'зелье',
  'земля',
  'зенит',
  'зерно',
  'зефир',
  'злоба',
  'знамя',
  'знать',
  'игрок',
  'идеал',
  'идиот',
  'изгиб',
  'изгой',
  'излив',
  'излом',
  'износ',
  'изъян',
  'икона',
  'икота',
  'имидж',
  'ингуш',
  'индус',
  'индюк',
  'инжир',
  'интим',
  'инуит',
  'иприт',
  'искра',
  'ислам',
  'испуг',
  'истец',
  'исток',
  'исход',
  'кабак',
  'кабан',
  'кадет',
  'кадык',
  'казак',
  'казан',
  'казах',
  'казна',
  'казнь',
  'казус',
  'какао',
  'калач',
  'калаш',
  'камео',
  'камка',
  'камыш',
  'канал',
  'канат',
  'канон',
  'каноэ',
  'канун',
  'капля',
  'капот',
  'каппа',
  'карат',
  'касса',
  'каста',
  'катер',
  'каток',
  'кашпо',
  'квант',
  'кварц',
  'квест',
  'квота',
  'кегля',
  'кепка',
  'кефир',
  'кинза',
  'киоск',
  'кисет',
  'кисть',
  'кишка',
  'кирка',
  'класс',
  'клатч',
  'клерк',
  'клоун',
  'книга',
  'кница',
  'князь',
  'коала',
  'кобра',
  'кодек',
  'кожух',
  'козел',
  'койка',
  'койот',
  'колье',
  'комар',
  'комик',
  'комод',
  'комок',
  'конец',
  'конус',
  'копия',
  'копна',
  'корма',
  'короб',
  'кость',
  'косяк',
  'котел',
  'кофта',
  'кочан',
  'кочка',
  'кошка',
  'кража',
  'кредо',
  'кровь',
  'кроль',
  'крона',
  'кросс',
  'кроха',
  'круиз',
  'крупа',
  'крыло',
  'крыса',
  'крыша',
  'кубок',
  'кузов',
  'кукла',
  'кулак',
  'кулик',
  'кулич',
  'кулон',
  'культ',
  'купец',
  'купол',
  'купон',
  'кураж',
  'курок',
  'кусок',
  'кухня',
  'кучер',
  'кювет',
  'лаваш',
  'лавка',
  'ладья',
  'лазер',
  'лакей',
  'лампа',
  'лапка',
  'лапша',
  'ларек',
  'ларец',
  'ласка',
  'лассо',
  'лафет',
  'левша',
  'лежак',
  'лейка',
  'лемур',
  'лента',
  'леска',
  'летун',
  'леший',
  'лимит',
  'линза',
  'литий',
  'лихач',
  'лицей',
  'ловец',
  'ловля',
  'лодка',
  'ложка',
  'ломка',
  'лопух',
  'лорум',
  'лоток',
  'лотос',
  'магия',
  'магма',
  'мадам',
  'мажор',
  'мазня',
  'мазут',
  'майка',
  'майор',
  'макет',
  'малец',
  'малыш',
  'маляр',
  'манго',
  'манеж',
  'манту',
  'манул',
  'маржа',
  'марка',
  'маска',
  'масло',
  'масон',
  'масса',
  'масть',
  'матка',
  'мафия',
  'мачта',
  'медик',
  'место',
  'месть',
  'месяц',
  'метан',
  'метка',
  'метла',
  'метод',
  'метро',
  'мечта',
  'мешок',
  'мидия',
  'мираж',
  'мойка',
  'молот',
  'монах',
  'мопед',
  'мороз',
  'моряк',
  'моток',
  'мотор',
  'мошка',
  'музей',
  'муляж',
  'мумия',
  'мусор',
  'муфта',
  'мысок',
  'мышца',
  'мэрия',
  'мякиш',
  'мятеж',
  'набат',
  'набег',
  'набор',
  'навес',
  'навоз',
  'навык',
  'надел',
  'надой',
  'наезд',
  'нажим',
  'налет',
  'налив',
  'налог',
  'намаз',
  'намек',
  'нанос',
  'напев',
  'нарды',
  'народ',
  'нарыв',
  'наряд',
  'насос',
  'наука',
  'нахал',
  'нация',
  'недуг',
  'нерпа',
  'нефть',
  'нимфа',
  'нитка',
  'ничья',
  'нищий',
  'ножка',
  'ножны',
  'нойон',
  'норка',
  'норма',
  'носок',
  'нубук',
  'нужда',
  'нутро',
  'нырок',
  'нытик',
  'нытье',
  'оазис',
  'обвал',
  'обвес',
  'обвод',
  'обгон',
  'обжим',
  'обзор',
  'обида',
  'облет',
  'облик',
  'обман',
  'обмен',
  'образ',
  'обрез',
  'оброк',
  'обруч',
  'обрыв',
  'обряд',
  'обувь',
  'обход',
  'объем',
  'обыск',
  'огонь',
  'озеро',
  'озноб',
  'океан',
  'оклад',
  'оклик',
  'окрас',
  'окрик',
  'округ',
  'окунь',
  'олимп',
  'олово',
  'ольха',
  'омлет',
  'опека',
  'опера',
  'опись',
  'оплот',
  'опора',
  'опрос',
  'оптик',
  'опция',
  'орден',
  'ордер',
  'ореол',
  'орлан',
  'осень',
  'осетр',
  'осина',
  'оскал',
  'ослик',
  'особа',
  'особь',
  'остов',
  'отбой',
  'отбор',
  'отвал',
  'отвар',
  'ответ',
  'отгиб',
  'отгул',
  'отдел',
  'отдых',
  'отель',
  'отжим',
  'отзыв',
  'отказ',
  'откат',
  'отпор',
  'отрок',
  'отрыв',
  'отряд',
  'отсев',
  'отсек',
  'отсос',
  'отток',
  'отход',
  'отчим',
  'отшиб',
  'офшор',
  'охват',
  'охота',
  'падеж',
  'падре',
  'пайка',
  'пакет',
  'палач',
  'палаш',
  'палец',
  'палка',
  'панда',
  'панно',
  'папка',
  'парад',
  'парка',
  'паром',
  'парта',
  'парус',
  'парча',
  'паста',
  'пасть',
  'пасха',
  'пауза',
  'пафос',
  'пацан',
  'пачка',
  'пашня',
  'певец',
  'пегас',
  'пекло',
  'пемза',
  'пенал',
  'пение',
  'пепел',
  'перец',
  'песец',
  'песня',
  'песок',
  'песто',
  'петля',
  'петух',
  'пешка',
  'пиала',
  'пижма',
  'пижон',
  'пикап',
  'пикет',
  'пилот',
  'пинта',
  'пират',
  'пирог',
  'пирон',
  'питон',
  'питта',
  'пихта',
  'пицца',
  'пламя',
  'плата',
  'плато',
  'плаха',
  'плеер',
  'племя',
  'плеск',
  'плечо',
  'плита',
  'плоть',
  'побег',
  'повар',
  'повод',
  'подол',
  'поезд',
  'пожар',
  'позор',
  'позыв',
  'поиск',
  'пойло',
  'пойма',
  'показ',
  'покер',
  'покой',
  'покос',
  'полаз',
  'полба',
  'полет',
  'полив',
  'полип',
  'полис',
  'полка',
  'полюс',
  'помет',
  'помол',
  'помпа',
  'пончо',
  'попса',
  'порез',
  'порог',
  'порок',
  'порох',
  'порча',
  'порыв',
  'посев',
  'посол',
  'посох',
  'посыл',
  'поток',
  'потоп',
  'поход',
  'почва',
  'почет',
  'почка',
  'почта',
  'пошив',
  'поэма',
  'право',
  'прайд',
  'пресс',
  'прием',
  'прима',
  'принц',
  'приют',
  'проба',
  'проем',
  'проза',
  'просо',
  'профи',
  'прыск',
  'прыть',
  'прядь',
  'пряжа',
  'псарь',
  'псина',
  'птаха',
  'птица',
  'пугач',
  'пудра',
  'пульс',
  'пульт',
  'пункт',
  'пупок',
  'пурга',
  'пучок',
  'пушка',
  'пчела',
  'пшено',
  'пытка',
  'пышка',
  'пьеса',
  'пятак',
  'пятка',
  'пятно',
  'пяток',
  'радар',
  'радио',
  'разум',
  'район',
  'ралли',
  'рамен',
  'рамка',
  'рампа',
  'ранец',
  'ранчо',
  'расса',
  'раунд',
  'рвота',
  'ребро',
  'ребус',
  'регби',
  'редис',
  'редут',
  'режим',
  'резак',
  'резня',
  'резон',
  'релиз',
  'рельс',
  'репей',
  'репер',
  'решка',
  'рифма',
  'робот',
  'ровня',
  'рогоз',
  'родео',
  'родня',
  'рожок',
  'розга',
  'рокот',
  'роман',
  'ропот',
  'ротор',
  'рояль',
  'ртуть',
  'рубеж',
  'рубин',
  'рубль',
  'ружье',
  'руина',
  'рукав',
  'рулет',
  'рулон',
  'рупор',
  'русло',
  'ручей',
  'ручка',
  'рыбак',
  'рывок',
  'рыжик',
  'рында',
  'рынок',
  'рысак',
  'рычаг',
  'рюмка',
  'сабля',
  'саван',
  'сазан',
  'сайра',
  'салат',
  'салон',
  'салют',
  'самбо',
  'самец',
  'самка',
  'самса',
  'санки',
  'сапог',
  'сарай',
  'сатин',
  'сауна',
  'сахар',
  'сачок',
  'сброд',
  'сброс',
  'сбруя',
  'свеча',
  'свист',
  'свита',
  'свора',
  'свояк',
  'связь',
  'сглаз',
  'сдача',
  'сдвиг',
  'сдоба',
  'сеанс',
  'север',
  'седан',
  'седло',
  'сезон',
  'секта',
  'селфи',
  'семга',
  'семья',
  'сенат',
  'серия',
  'сетка',
  'сибас',
  'силач',
  'силок',
  'силос',
  'синод',
  'синяк',
  'сироп',
  'ситец',
  'скала',
  'скарб',
  'скаут',
  'сквер',
  'сквош',
  'скейт',
  'скетч',
  'скирд',
  'склад',
  'склеп',
  'склон',
  'скоба',
  'скотч',
  'скрип',
  'скука',
  'скула',
  'скунс',
  'слава',
  'слайд',
  'слеза',
  'сленг',
  'слива',
  'слизь',
  'слово',
  'слуга',
  'слюда',
  'слюна',
  'смена',
  'смерч',
  'смесь',
  'смета',
  'смола',
  'смотр',
  'смрад',
  'смузи',
  'смута',
  'смысл',
  'снедь',
  'сноха',
  'собор',
  'совет',
  'совок',
  'содом',
  'созыв',
  'сойка',
  'сокет',
  'сокол',
  'сонар',
  'сопка',
  'сопло',
  'сорок',
  'сосед',
  'соска',
  'сосна',
  'сосок',
  'сосуд',
  'сотка',
  'сотня',
  'софит',
  'сошка',
  'спазм',
  'спесь',
  'спина',
  'спирт',
  'спица',
  'сплав',
  'спонж',
  'спора',
  'спорт',
  'спрей',
  'спрос',
  'спрус',
  'спурт',
  'спуск',
  'среда',
  'ссора',
  'ссуда',
  'стадо',
  'сталь',
  'станс',
  'старт',
  'старь',
  'стать',
  'ствол',
  'створ',
  'стезя',
  'стейк',
  'стела',
  'стена',
  'стенд',
  'степь',
  'стиль',
  'столб',
  'стопа',
  'стояк',
  'страж',
  'страх',
  'стриж',
  'строй',
  'стужа',
  'ступа',
  'судак',
  'судно',
  'судья',
  'суета',
  'сукно',
  'сумка',
  'сумма',
  'сусек',
  'сусло',
  'суфле',
  'сучок',
  'схема',
  'схрон',
  'сцена',
  'съезд',
  'сырец',
  'сырок',
  'сырть',
  'сырье',
  'сыщик',
  'сюжет',
  'табак',
  'табло',
  'табор',
  'табун',
  'тазик',
  'тайга',
  'тайна',
  'такси',
  'талия',
  'талон',
  'танго',
  'танец',
  'тапок',
  'тапир',
  'таран',
  'тариф',
  'тахта',
  'тачка',
  'тварь',
  'твист',
  'театр',
  'тезис',
  'текст',
  'телец',
  'телка',
  'телок',
  'тембр',
  'тенор',
  'тепло',
  'терма',
  'терно',
  'теска',
  'тесто',
  'тесть',
  'тиара',
  'типаж',
  'тираж',
  'тиски',
  'титан',
  'титул',
  'ткань',
  'товар',
  'токен',
  'толпа',
  'толща',
  'томат',
  'тонна',
  'топаз',
  'топка',
  'топор',
  'топот',
  'торба',
  'торец',
  'тоска',
  'тосол',
  'тотем',
  'точка',
  'трава',
  'тракт',
  'транс',
  'транш',
  'траст',
  'трата',
  'траур',
  'трель',
  'тренд',
  'тренч',
  'треск',
  'трест',
  'треть',
  'трико',
  'тромб',
  'тропа',
  'труба',
  'труха',
  'трюмо',
  'тубус',
  'тумба',
  'тунец',
  'турка',
  'турне',
  'туфля',
  'тушка',
  'тыква',
  'тюбик',
  'тюфяк',
  'тягач',
  'тяпка',
  'убыль',
  'уголь',
  'угорь',
  'удача',
  'узник',
  'уклад',
  'уклон',
  'укроп',
  'уксус',
  'улика',
  'улица',
  'умник',
  'умора',
  'унция',
  'упрек',
  'упырь',
  'успех',
  'устав',
  'усташ',
  'устой',
  'уступ',
  'устье',
  'утеря',
  'утеха',
  'утиль',
  'ухват',
  'учеба',
  'ущерб',
  'фагот',
  'фазан',
  'факел',
  'факир',
  'фанат',
  'фасад',
  'фаска',
  'фасон',
  'фатин',
  'фатум',
  'фауна',
  'фаянс',
  'фенол',
  'феном',
  'ферзь',
  'ферма',
  'фетиш',
  'фибра',
  'физик',
  'филин',
  'фильм',
  'финал',
  'финик',
  'финиш',
  'финка',
  'фирма',
  'фишка',
  'фланг',
  'флирт',
  'флора',
  'флюид',
  'фляга',
  'фобия',
  'фокус',
  'фомка',
  'фондю',
  'форма',
  'форум',
  'фотон',
  'фраза',
  'франк',
  'франт',
  'фрахт',
  'фреза',
  'френч',
  'фронт',
  'фрукт',
  'фугас',
  'фужер',
  'фураж',
  'фурия',
  'фурор',
  'футон',
  'фьорд',
  'хакер',
  'халат',
  'халва',
  'хамон',
  'ханжа',
  'харчо',
  'хаски',
  'хвала',
  'хвост',
  'химик',
  'химия',
  'хинди',
  'хиппи',
  'хлыст',
  'хмель',
  'хмурь',
  'хобби',
  'хобот',
  'ходок',
  'холка',
  'холод',
  'холоп',
  'холст',
  'хомут',
  'хомяк',
  'хорда',
  'хохма',
  'хохот',
  'хруст',
  'хумус',
  'хурма',
  'хутор',
  'цапля',
  'цедра',
  'центр',
  'цинга',
  'цифра',
  'цокот',
  'цукат',
  'цыган',
  'чайка',
  'часть',
  'чашка',
  'челка',
  'червь',
  'череп',
  'черта',
  'честь',
  'чехол',
  'чечен',
  'чечил',
  'чешка',
  'чешуя',
  'чибис',
  'чижик',
  'чипсы',
  'число',
  'чокер',
  'чтиво',
  'чугун',
  'чудак',
  'чудик',
  'чужак',
  'чуйка',
  'чукур',
  'чулан',
  'чулок',
  'чушка',
  'шабаш',
  'шайба',
  'шайка',
  'шакал',
  'шалаш',
  'шалун',
  'шаман',
  'шапка',
  'шасси',
  'шатен',
  'шаттл',
  'шатун',
  'шахта',
  'шашка',
  'шейка',
  'шельф',
  'шериф',
  'ширма',
  'шифер',
  'шихта',
  'шишка',
  'шкала',
  'шквал',
  'школа',
  'шкура',
  'шланг',
  'шлейф',
  'шляпа',
  'шмель',
  'шнапс',
  'шокер',
  'шорох',
  'шорты',
  'шоссе',
  'шпага',
  'шпала',
  'шпиль',
  'шпион',
  'шпора',
  'шприц',
  'шпрот',
  'шрифт',
  'штамп',
  'штаны',
  'штиль',
  'штифт',
  'штора',
  'шторм',
  'штраф',
  'штрих',
  'штука',
  'штурм',
  'штырь',
  'шулер',
  'шуруп',
  'шутка',
  'щебет',
  'щегол',
  'щенок',
  'щепка',
  'щипцы',
  'щиток',
  'эгида',
  'эклер',
  'экран',
  'элита',
  'эмаль',
  'эпоха',
  'эскиз',
  'эстет',
  'этика',
  'этнос',
  'юката',
  'юниор',
  'юнкер',
  'юноша',
  'юрист',
  'ябеда',
  'ягода',
  'ягуар',
  'якорь',
  'ярлык',
  'ясень',
  'яство',
  'яхонт'
]