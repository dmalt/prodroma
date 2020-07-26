import pandas as pd
from pandas import CategoricalDtype


def load_dframe(sujb_num):
    fname = "prodroma.xlsx"
    subj_num = 0
    dframe = pd.read_excel(
        fname, sheet_name=subj_num, skiprows=10, usecols="B:CR", index_col=0
    ).T

    dframe = dframe.rename(
        columns={
            "день": "day",
            "Время заполнения ТП": "fillin_time",
            "ГБ новая": "ha_new",
            "ГБ продолжение": "ha_cont",
            "Начало боли": "ha_start",
            "Окончание боли": "ha_stop",
            "Обезболивающее": "painkiller",
            "Название": "painkiller_name",
            "аура": "aura",
            "Боль сейчас": "ha_now",
            "ВАШ макс": "your_max",
            "односторонняя": "onesided",
            "пульсация": "pulsation",
            "усиление движением": "intens_by_mov",
            "тошнота": "vomiting",
            "чувствительность к свету": "light_sens_bin",
            "чувствительность к звуку": "noise_sens_bin",
            "чувствительность к запахам": "smell_sens_bin",
            "заметил провокатор": "noticed_trigger",
            "какой триггер": "which_trigger",
            "Продолжительность сна": "sleep_duration",
            "Качество сна": "sleep_quality",
            "Свежесть после сна": "sleep_freshness",
            "Больше света, чем обычно": "a_lot_light",
            "Чувствительность к свету": "light_sens_cat",
            "Больше звука чем обычно": "a_lot_noise",
            "Чувствительность к звуку": "noise_sens_cat",
            "Были резкие запахи?": "strong_smells",
            "Чувствительность к запахам": "smell_sens_cat",
            "Пропуск приема пищи": "meal_skip",
            "Чувство голода": "hunger",
            "Воды достаточно?": "hydration",
            "Жажда": "thirst",
            "Алкоголь": "alcohol",
            "кофеин": "caffeine",
            "сыр, шоко, цитрус": "cheese_choco_citrus",
            "Хотелось шоколада": "wanted_choco",
            "Чувство усталости": "tiredness",
            "Сложность концентрации": "focus_difficulty",
            "Тревога": "anxiety",
            "Депрессия": "depression",
            "Работоспособность": "productivity",
            "Работосособность": "productivity",
            "Сонливость": "sleepiness",
            "Зевания": "yawning",
            "Напряжение глаз": "eye_strain",
            "боль в шее": "neck_pain",
            "Чувствит кожи головы": "scalp_sens",
            "Физическая ативность": "exercise",
            "какой день": "which_day",
            "Перелеты": "flights",
            "1 день менструации": "pms_1st_day",
            "подташнивает": "nausea",
            "вегетатика": "vegetatics",
            "мочеиспускание": "urination",
            "% заполнения дневника": "journal_completion_percentage",
            "комментарий": "comment",
            "дата": "date",
            "ТП": "TP",
        }
    )

    dframe = dframe.set_index(["date", "TP"])

    dframe.columns.rename(None, inplace=True)

    dframe.fillin_time = pd.to_datetime(dframe.fillin_time)

    dframe.replace(to_replace="да", value=True, inplace=True)
    dframe.replace(to_replace="нет", value=False, inplace=True)

    dframe["ha_new"] = dframe["ha_new"].fillna(False)
    dframe["ha_cont"] = dframe["ha_cont"].fillna(False)
    dframe["ha_now"] = dframe["ha_new"] | dframe["ha_cont"]

    dframe["painkiller"] = dframe["painkiller"].fillna(False)
    dframe["vomiting"] = dframe["vomiting"].fillna(False)
    dframe["intens_by_mov"] = dframe["intens_by_mov"].fillna(False)
    dframe["pulsation"] = dframe["pulsation"].fillna(False)
    dframe["light_sens_bin"] = dframe["light_sens_bin"].fillna(False)
    dframe["noise_sens_bin"] = dframe["noise_sens_bin"].fillna(False)
    dframe["smell_sens_bin"] = dframe["smell_sens_bin"].fillna(False)
    dframe["flights"] = dframe["flights"].fillna(False)
    dframe["pms_1st_day"] = dframe["pms_1st_day"].fillna(False)

    cat_type = CategoricalDtype([1, 2, 3, 4, 5], ordered=True)
    for col in [
        "anxiety",
        "depression",
        "tiredness",
        "productivity",
        "sleepiness",
        "light_sens_cat",
        "smell_sens_cat",
        "noise_sens_cat",
        "sleep_quality",
        "sleep_freshness",
        "hunger",
    ]:
        dframe[col] = dframe[col].astype(cat_type)
    # dframe["anxiety"] = dframe["depression"].astype(int).astype('category')
    return dframe
