from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
import random

from src.core.models.models import Translation, UserProgress, User


# Получение слов и вариантов перевода
async def get_word_for_training(session: AsyncSession, user_id: int):
    # Получаем все слова, которые пользователь не выучил
    result = await session.execute(
        select(UserProgress)
        .join(Translation, UserProgress.translation_id == Translation.id)
        .filter(UserProgress.user_id == user_id, UserProgress.is_learned == False)
    )
    unlearned_words = result.scalars().all()

    if not unlearned_words:
        return None, None

    # Выбираем случайное слово
    chosen_word = random.choice(unlearned_words)

    # Получаем правильный перевод
    correct_translation = chosen_word.translation.russian_word

    # Получаем другие случайные переводы (чтобы были варианты)
    result = await session.execute(
        select(Translation.russian_word)
        .filter(Translation.id != chosen_word.translation_id)
        .order_by(func.random())
        .limit(4)
    )
    incorrect_translation = result.scalars().all

    # Формируем список вариантов, включая правильный ответ
    options = [correct_translation] + incorrect_translation
    random.shuffle(options)

    return chosen_word.translation.english_word, options


async def check_user_answer(
    session: AsyncSession, user_id: int, english_word: str, selected_translation: str
):
    # Находим слово в базе
    result = await session.execute(
        select(UserProgress)
        .join(Translation, UserProgress.translation_id == Translation.id)
        .filter(
            UserProgress.user_id == user_id, Translation.english_word == english_word
        )
    )
    user_progress = result.scalars().first()

    if not user_progress:
        return False

    # Проверяем, правильный ли ответ
    if user_progress.translation.russian_word == selected_translation:
        user_progress.is_learned = True
        await session.commit()
        return True
    return False
