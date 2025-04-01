from gigachat import GigaChat
from langchain_core.prompts import PromptTemplate
import os
from getpass import getpass
from pathlib import Path

# Переменная с директорией для сохранения файлов
concepts_dir = Path("../../../KIDBOOK/life/career/concepts/")
concepts_dir.mkdir(parents=True, exist_ok=True)

# Список тем для генерации
concepts = [
    "Профессия", "Образование", "Специальность", "Навыки", "Опыт работы",
    "Резюме", "Карьерный рост", "Зарплата", "Предприниматель", "Работодатель",
    "Стажировка", "Профориентация", "Фриланс", "Трудовой договор", "Мечта"
]


def create_markdown_file(filename, content):
    """Создает MD-файл с заданным содержанием"""
    filepath = concepts_dir / filename
    filepath.write_text(content, encoding="utf-8")
    print(f"Файл создан: {filepath}")


# Подключаемся к GigaChat
llm = GigaChat(credentials=('ZGZjNWY2YzUtZDI3Yy00ODRmLWIzOGEtYzA5YjhkN2I1OTVkOjEwMjA5ODJmLTc1MmItNDU0MS05NTQ5LTBjNDFmOThmMTY4Mw=='), verify_ssl_certs=False, model='GigaChat-Pro')

template = """
    Представь, что ты специалист по работе с детьми. Ты очень хорошо умеешь объяснять сложные темы простыми словами. Так же ты очень хорошо знаешь тему работы и карьеры. 
    Твоя задача – тебе будут приходить понятия. Ты должен будешь написать дллинную, полную, яркую, веселую и познавательную статью по заданному понятию. Пиши для ребенка 7 лет.

    Все термины, относящиеся к перекрестным понятиям пометь. Вот все понятия, о которых пойдет речь:
    "Профессия", "Образование", "Специальность", "Навыки", "Опыт работы",
    "Резюме", "Карьерный рост", "Зарплата", "Предприниматель", "Работодатель",
    "Стажировка", "Профориентация", "Фриланс", "Трудовой договор", "Мечта"

    Правила:
    - На выходе должна быть markdown страница. 
    - Используй простые слова.
    - Приводи яркие примеры из жизни детей, которые будут раскрывать заданную тему.
    - Для всех терминов делай сноски с определениями.
    - В начале дай определение простыми словами, потом расскажи интересную историю или аналогию.
    - Сделай небольшой вывод, который поможет запомнить материал.
    - Старайся делать структурированно.

    Понятие: {query}
"""

# Проходим по списку тем и создаем MD-файлы
for concept_name in concepts:
    prompt = PromptTemplate(input_variables=['query'], template=template).format(query=concept_name)

    # Отправляем запрос в GigaChat
    response = llm.chat(prompt)

    # Создаем MD-файл с сгенерированным контентом
    create_markdown_file(f'{concept_name}.md', response.choices[0].message.content)